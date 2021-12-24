import os
import typing
from functools import wraps
from typing import List

import boto3

from pacu.config import Config


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
    def _decr_args(func: typing.Callable):
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
    def _decr_args(func: typing.Callable):
        @wraps(func)
        def _wrapper(*args, **kwargs):
            region = Config().regions[0]
            sess = boto3.Session(*pargs, region_name=region, **pkwargs)
            return func(*args, sess=sess, region=region, **kwargs)
        return _wrapper
    return _decr_args
