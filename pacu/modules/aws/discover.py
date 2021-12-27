"""Currently this is mostly just an example of using the @for_each_region decorator."""
import json
import queue
import concurrent.futures

import boto3
import botocore.exceptions
import typer

from typing import TYPE_CHECKING, List, Generator, Dict

from pacu.config import Config
from pacu.aws import default_region, throttle_session
from pacu.data import ResourceDB, Resource
from pacu.utils import pcache

MAX_WORKERS = 10
MAX_PER_SECOND = 4

app = typer.Typer()

if TYPE_CHECKING:
    import mypy_boto3_cloudformation
    import mypy_boto3_cloudcontrol

    from mypy_boto3_cloudformation import type_defs as cfn_t
    from mypy_boto3_cloudcontrol import type_defs as ctl_t

WORKERS = 1


@app.command()
def main():
    run()


@default_region(profile_name=Config().profile)
def run(sess: boto3.Session, region):
    q = queue.Queue()
    for _t in get_types(sess):
        q.put(_t)

    throttle_session(sess, 3)  # We seem to get throttling exceptions if this is set any higher
    ctrl: 'mypy_boto3_cloudcontrol.Client' = sess.client('cloudcontrol')
    pool = concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS)
    pool.daemon = True

    tasks = []

    while not q.empty():
        _t = q.get()
        tasks.append(pool.submit(_list_resources, ctrl, _t))

    rdb = ResourceDB()
    while tasks:
        reschedule = []
        for f in concurrent.futures.as_completed(tasks):
            result = f.result()

            for r in result.get('ResourceDescriptions', []):
                props = json.loads(r['Properties'])
                rdb.insert(Resource(props, doc_id=r['Identifier']))

            if result.get('NextToken', False):
                reschedule.append(pool.submit(_list_resources, ctrl, result))
            else:
                q.task_done()
        tasks = reschedule

    q.join()


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


@pcache(ignore_args=[0])
def get_schema(cfn, t):
    resp = cfn.describe_type(Type='RESOURCE', TypeName=t['TypeName'])
    schema = json.loads(resp['Schema'], default=str)
    return schema


if __name__ == "__main__":
    app()
