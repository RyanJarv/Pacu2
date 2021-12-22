"""A sample module."""
import os
from typing import List

import boto3

from pacu.settings import profile_path


def get_all_regions() -> List[str]:
    region = os.getenv('AWS_REGION') or os.getenv('AWS_DEFAULT_REGION') or 'us-east-1'
    sess = boto3.session.Session(profile_name=get_profile())
    resp = sess.client('ec2', region_name=region).describe_regions()
    regions = [r['RegionName'] for r in resp['Regions']]
    return regions

def set_profile_env(profile: str):
    os.putenv('AWS_PROFILE', profile)
    os.putenv('AWS_DEFAULT_PROFILE', profile)


def get_profile():
    if profile_path.is_file():
        return profile_path.read_text()
    else:
        return "default"


def get_config_path():
    p = os.getenv('AWS_CONFIG_FILE') or os.path.expanduser('~/.aws/config')
    return p



