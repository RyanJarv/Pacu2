"""Currently this is mostly just an example of using the @for_each_region decorator."""
import boto3
import typer

from pacu.config import Config
from pacu.aws import for_each_region

app = typer.Typer()


@app.command(name='list', help='list ec2 instances.')
def _list():
    _list_ec2()


@for_each_region(profile_name=Config().profile)
def _list_ec2(sess: boto3.Session, region: str):
    ec2 = sess.resource('ec2')
    print('Region: ' + region)
    for inst in ec2.instances.all():
        print(inst)


if __name__ == "__main__":
    app()
