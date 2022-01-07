"""Currently this is mostly just an example of using the @for_each_region decorator."""
import boto3
import typer

from pacu.config import Config
from pacu.aws import for_each_region

app = typer.Typer()

from pacu.models.awsapi.ec2 import DescribeInstancesResult

@app.command(name='list', help='list ec2 instances.')
def _list():
    _list_ec2()


@for_each_region(profile_name=Config().profile)
def _list_ec2(sess: boto3.Session, region: str):
    ec2 = sess.client('ec2')
    print('Region: ' + region)
    resp = ec2.describe_instances()
    result = DescribeInstancesResult(**resp).Reservations.__root__[0].
    result.Reservations[0]

if __name__ == "__main__":
    app()
