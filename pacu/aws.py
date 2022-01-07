import json
import os
from typing import Dict, Generator, List, Callable, TYPE_CHECKING
from functools import wraps

import boto3
import botocore.exceptions

from pacu.config import Config
from pacu.utils import limit_requests, pcache


if TYPE_CHECKING:
    import mypy_boto3_cloudformation
    import mypy_boto3_cloudcontrol

    from mypy_boto3_cloudformation import type_defs as cfn_t
    from mypy_boto3_cloudcontrol import type_defs as ctl_t


def get_all_regions() -> List[str]:
    region = os.getenv('AWS_REGION') or os.getenv('AWS_DEFAULT_REGION') or 'us-east-1'
    sess = boto3.session.Session(profile_name=Config().profile)
    resp = sess.client('ec2', region_name=region).describe_regions()
    regions = [r['RegionName'] for r in resp['Regions']]
    return regions


def set_profile_env(profile: str):
    os.putenv('AWS_PROFILE', profile)
    os.putenv('AWS_DEFAULT_PROFILE', profile)


def shared_config_path():
    p = os.getenv('AWS_CONFIG_FILE') or os.path.expanduser('~/.aws/config')
    return p


def shared_credential_path():
    p = os.getenv('AWS_CREDENTIAL_FILE') or os.path.expanduser('~/.aws/credentials')
    return p


def for_each_region(*pargs, **pkwargs):
    """Similar to the default_region but the wrapped function get's invoked for each region set in the config."""
    def _decr_args(func: Callable):
        @wraps(func)
        def _wrapper(*args, **kwargs):
            ret = []
            for region in Config().regions:
                sess = boto3.Session(*pargs, region_name=region, **pkwargs)
                ret.append(func(*args, sess=sess, region=region, **kwargs))
            return ret
        return _wrapper
    return _decr_args


def default_region(*pargs, **pkwargs):
    """Passes a session object using the default region and the region name to the wrapped function.

    The session is passed to the sess argument and the region string is passed to the 'region' argument of the
    wrapped function.
    """
    def _decr_args(func: Callable):
        @wraps(func)
        def _wrapper(*args, **kwargs):
            region = Config().regions[0]
            sess = boto3.Session(*pargs, region_name=region, **pkwargs)
            return func(*args, sess=sess, region=region, **kwargs)
        return _wrapper
    return _decr_args


def throttle_session(sess: 'boto3.Session', per_second: int):
    sess.events.register('before-send.*.*', limit_requests(per_second))

def _list_resources(ctl: 'mypy_boto3_cloudcontrol.Client', t) -> 'ctl_t.ListResourcesOutputTypeDef':
    try:
        if not t.get('NextToken', False):
            return ctl.list_resources(TypeName=t['TypeName'])
        else:
            return ctl.list_resources(TypeName=t['TypeName'], NextToken=t['NextToken'])
    except botocore.exceptions.ClientError as e:
        if not e.response['Error']['Code'] in ['UnsupportedActionException', 'GeneralServiceException',
                                               'AccessDeniedException', 'InvalidRequestException',
                                               'ResourceNotFoundException', 'HandlerInternalFailureException']:
            raise e
    return {}


def get_types(sess) -> Generator['cfn_t.TypeSummaryTypeDef', None, None]:
    cfn: 'mypy_boto3_cloudformation.Client' = sess.client('cloudformation')

    # The API seems to start rejecting requests if run any faster.
    # throttle_session(sess, 30)

    paginator = cfn.get_paginator('list_types')
    types: List['cfn_t.TypeSummaryTypeDef'] = []

    for page in paginator.paginate(Visibility='PUBLIC', Filters={'Category': 'AWS_TYPES'},
                                   Type='RESOURCE', DeprecatedStatus='LIVE'):
        types.extend(page['TypeSummaries'])
        for t in page['TypeSummaries']:
            # These types have required parameters which are not reflected in the schema.
            #   AWS::Route53RecoveryControl::SafetyRule: 'ControlPanelArn'
            #   AWS::AmplifyUIBuilder::Component: 'appId'
            if t['TypeName'] in ['AWS::Route53RecoveryControl::SafetyRule', 'AWS::AmplifyUIBuilder::Component']:
                continue

            schema: Dict[str, any] = get_schema(cfn, t)
            if 'required' in schema.keys() or "list" not in schema.get("handlers", {}).keys():
                continue

            yield t


def get_schemas(sess) -> Generator['dict', None, None]:
    cfn: 'mypy_boto3_cloudformation.Client' = sess.client('cloudformation')

    paginator = cfn.get_paginator('list_types')
    types: List['cfn_t.TypeSummaryTypeDef'] = []

    for page in paginator.paginate(Visibility='PUBLIC', Filters={'Category': 'AWS_TYPES'},
                                   Type='RESOURCE', DeprecatedStatus='LIVE'):
        types.extend(page['TypeSummaries'])
        for t in page['TypeSummaries']:
            yield get_schema(cfn, t)


@pcache(ignore_args=[0])
def get_schema(cfn, t):
    resp = cfn.describe_type(Type='RESOURCE', TypeName=t['TypeName'])
    schema = json.loads(resp['Schema'], default=str)
    return schema