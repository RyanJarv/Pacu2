
import typing
import typer
import boto3

from pacu.aws import for_each_region
from pacu.config import Config

app = typer.Typer()

if typing.TYPE_CHECKING:
    import mypy_boto3_ec2

