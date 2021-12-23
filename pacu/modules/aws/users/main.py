import typing

import typer

import boto3
import botocore.errorfactory

app = typer.Typer()

if typing.TYPE_CHECKING:
    import mypy_boto3_iam


@app.command()
def create(name: str = typer.Argument(default=False)):
    iam = boto3.resource('iam')
    user = iam.User(name)
    try:
        user.create()
    except botocore.errorfactory.ClientError as e:
        if e.response['Error']['Code'] == 'EntityAlreadyExists':
            print(f"[ERROR] The user {name} already exists.")
            return
        else:
            raise e


    user.attach_policy(PolicyArn='arn:aws:iam::aws:policy/AdministratorAccess')
    try:
        access_key = user.create_access_key_pair()
    except botocore.errorfactory.ClientError as e:
        if e.response['Error']['Code'] == 'LimitExceeded':
            print(f"[ERROR] Two access key pairs are already attached to the user.")
            return
        else:
            raise e
    print(f"export AWS_ACCESS_KEY_ID={access_key.access_key_id}")
    print(f"export AWS_SECRET_ACCESS_KEY={access_key.access_key_id}")

@app.command()
def delete(name: str = typer.Argument(default=False)):
    iam = boto3.resource('iam')
    user = iam.User(name)

    for policy in user.attached_policies.all():
        policy.detach_user(UserName=user.name)

    for key in user.access_keys.all():
        key.delete()

    user.delete()
    print(f"User {name} successfully deleted.")