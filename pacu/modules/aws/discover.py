"""Currently this is mostly just an example of using the @for_each_region decorator."""
import json
from datetime import datetime

import boto3
import botocore.exceptions
import typer

from typing import TYPE_CHECKING, List, Generator

from pacu.config import Config
from pacu.aws import for_each_region, default_region, throttle_session
from pacu.utils import limit_requests, pcache

from ratelimit import limits, sleep_and_retry



app = typer.Typer()

if TYPE_CHECKING:
    import mypy_boto3_cloudformation
    import mypy_boto3_cloudcontrol

    from mypy_boto3_cloudformation import type_defs as cfn_t
    from mypy_boto3_cloudcontrol import type_defs as ctrl_t


@app.command()
def main():
    run()


@default_region(profile_name=Config().profile)
def run(sess: boto3.Session, region: str):
    types = get_types(sess)

    ctrl: 'mypy_boto3_cloudcontrol.Client' = sess.client('cloudcontrol')
    for t in types:
        try:
            resp: 'ctrl_t.ListResourcesOutputTypeDef' = ctrl.list_resources(TypeName=t['TypeName'])
            for resource in resp['ResourceDescriptions']:
                print(f"{resource['Identifier']} -- {resource['Properties']}")
        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] in ['UnsupportedActionException', 'GeneralServiceException',
                                               'AccessDeniedException']:
                continue
            else:
                raise e

        while resp.get('NextToken', False):
            try:
                resp: 'ctrl_t.ListResourcesOutputTypeDef' = ctrl.list_resources(
                    TypeName=t['TypeName'],
                    NextToken=resp['NextToken'],
                )
                for resource in resp['ResourceDescriptions']:
                    print(f"{resource['Identifier']} -- {resource['Properties']}")
            except botocore.exceptions.ClientError as e:
                if e.response['Error']['Code'] in ['UnsupportedActionException', 'GeneralServiceException',
                                                   'AccessDeniedException']:
                    continue
                else:
                    raise e


def get_types(sess) -> Generator['cfn_t.TypeSummaryTypeDef', None, None]:
    cfn: 'mypy_boto3_cloudformation.Client' = sess.client('cloudformation')
    throttle_session(sess, 30)
    paginator = cfn.get_paginator('list_types')
    types: List['cfn_t.TypeSummaryTypeDef'] = []
    for page in paginator.paginate(
            Visibility='PUBLIC',
            Filters={'Category': 'AWS_TYPES'},
            Type='RESOURCE',
            DeprecatedStatus='LIVE',
    ):
        types.extend(page['TypeSummaries'])
        for t in page['TypeSummaries']:
            # This has the required parameter 'ControlPanelArn' which is not reflected in the schema.
            if t['TypeName'] == 'AWS::Route53RecoveryControl::SafetyRule':
                continue

            schema = get_schema(cfn, t)
            if schema.get('required', True):
                continue
            if not schema.get("handlers", {}).get("list", False):
                continue
            yield t


@pcache(ignore_args=[0])
def get_schema(cfn, t):
    resp = cfn.describe_type(Type='RESOURCE', TypeName=t['TypeName'])
    schema = json.loads(resp['Schema'])
    return schema


if __name__ == "__main__":
    app()
