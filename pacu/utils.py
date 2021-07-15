"""A sample module."""
import os
from typing import List

import boto3


def get_all_regions() -> List[str]:
    region = os.getenv('AWS_REGION') or os.getenv('AWS_DEFAULT_REGION') or 'us-east-1'
    resp = boto3.client('ec2', region_name=region).describe_regions()
    regions = [r['RegionName'] for r in resp['Regions']]
    return regions
