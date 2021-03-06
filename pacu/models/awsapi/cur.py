# generated by datamodel-codegen:
#   filename:  openapi.yaml
#   timestamp: 2021-12-31T02:47:08+00:00

from __future__ import annotations

from enum import Enum
from typing import Annotated, Any, List, Optional

from pydantic import BaseModel, Field


class InternalErrorException(BaseModel):
    __root__: Any


class ValidationException(InternalErrorException):
    pass


class ModifyReportDefinitionResponse(BaseModel):
    pass


class PutReportDefinitionResponse(ModifyReportDefinitionResponse):
    """
    If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.
    """

    pass


class DuplicateReportNameException(InternalErrorException):
    pass


class ReportLimitReachedException(InternalErrorException):
    pass


class AWSRegion(Enum):
    """
    The region of the S3 bucket that AWS delivers the report into.
    """

    af_south_1 = 'af-south-1'
    ap_east_1 = 'ap-east-1'
    ap_south_1 = 'ap-south-1'
    ap_southeast_1 = 'ap-southeast-1'
    ap_southeast_2 = 'ap-southeast-2'
    ap_northeast_1 = 'ap-northeast-1'
    ap_northeast_2 = 'ap-northeast-2'
    ap_northeast_3 = 'ap-northeast-3'
    ca_central_1 = 'ca-central-1'
    eu_central_1 = 'eu-central-1'
    eu_west_1 = 'eu-west-1'
    eu_west_2 = 'eu-west-2'
    eu_west_3 = 'eu-west-3'
    eu_north_1 = 'eu-north-1'
    eu_south_1 = 'eu-south-1'
    me_south_1 = 'me-south-1'
    sa_east_1 = 'sa-east-1'
    us_east_1 = 'us-east-1'
    us_east_2 = 'us-east-2'
    us_west_1 = 'us-west-1'
    us_west_2 = 'us-west-2'
    cn_north_1 = 'cn-north-1'
    cn_northwest_1 = 'cn-northwest-1'


class AdditionalArtifact(Enum):
    """
    The types of manifest that you want AWS to create for this report.
    """

    REDSHIFT = 'REDSHIFT'
    QUICKSIGHT = 'QUICKSIGHT'
    ATHENA = 'ATHENA'


class AdditionalArtifactList(BaseModel):
    """
    A list of additional artifacts.
    """

    __root__: Annotated[
        List[AdditionalArtifact], Field(description='A list of additional artifacts.')
    ]


class BillingViewArn(BaseModel):
    __root__: Annotated[
        str,
        Field(
            max_length=128,
            regex='(arn:aws(-cn)?:billing::[0-9]{12}:billingview/)?[a-zA-Z0-9_\\+=\\.\\-@].{1,30}',
        ),
    ]


class CompressionFormat(Enum):
    """
    The compression format that AWS uses for the report.
    """

    ZIP = 'ZIP'
    GZIP = 'GZIP'
    Parquet = 'Parquet'


class ReportName(BaseModel):
    __root__: Annotated[
        str,
        Field(
            description="The name of the report that you want to create. The name must be unique, is case sensitive, and can't include spaces. ",
            max_length=256,
            regex="[0-9A-Za-z!\\-_.*\\'()]+",
        ),
    ]


class DeleteResponseMessage(BaseModel):
    __root__: Annotated[
        str, Field(description='Whether the deletion was successful or not.')
    ]


class MaxResults(BaseModel):
    __root__: Annotated[
        int,
        Field(
            description='The maximum number of results that AWS returns for the operation.',
            ge=5.0,
            le=5.0,
        ),
    ]


class GenericString(BaseModel):
    __root__: Annotated[
        str,
        Field(
            description='A generic string.',
            max_length=256,
            regex='[A-Za-z0-9_\\.\\-=]*',
        ),
    ]


class RefreshClosedReports(BaseModel):
    __root__: bool


class TimeUnit(Enum):
    """
    The length of time covered by the report.
    """

    HOURLY = 'HOURLY'
    DAILY = 'DAILY'
    MONTHLY = 'MONTHLY'


class ReportFormat(Enum):
    """
    The format that AWS saves the report in.
    """

    textORcsv = 'textORcsv'
    Parquet = 'Parquet'


class S3Bucket(BaseModel):
    __root__: Annotated[
        str,
        Field(
            description='The S3 bucket where AWS delivers the report.',
            max_length=256,
            regex='[A-Za-z0-9_\\.\\-]+',
        ),
    ]


class S3Prefix(BaseModel):
    __root__: Annotated[
        str,
        Field(
            description="The prefix that AWS adds to the report name when AWS delivers the report. Your prefix can't include spaces.",
            max_length=256,
            regex="[0-9A-Za-z!\\-_.*\\'()/]*",
        ),
    ]


class ReportVersioning(Enum):
    CREATE_NEW_REPORT = 'CREATE_NEW_REPORT'
    OVERWRITE_REPORT = 'OVERWRITE_REPORT'


class SchemaElement(Enum):
    """
    Whether or not AWS includes resource IDs in the report.
    """

    RESOURCES = 'RESOURCES'


class DeleteReportDefinitionResponse(BaseModel):
    """
    If the action is successful, the service sends back an HTTP 200 response.
    """

    ResponseMessage: Optional[DeleteResponseMessage] = None


class DeleteReportDefinitionRequest(BaseModel):
    """
    Deletes the specified report.
    """

    ReportName: Optional[ReportName] = None


class DescribeReportDefinitionsRequest(BaseModel):
    """
    Requests a list of AWS Cost and Usage reports owned by the account.
    """

    MaxResults: Optional[MaxResults] = None
    NextToken: Optional[GenericString] = None


class SchemaElementList(BaseModel):
    """
    A list of strings that indicate the content that is included in the report, such as service or usage type.
    """

    __root__: Annotated[
        List[SchemaElement],
        Field(
            description='A list of strings that indicate the content that is included in the report, such as service or usage type.'
        ),
    ]


class ReportDefinition(BaseModel):
    """
    The definition of AWS Cost and Usage Report. You can specify the report name, time unit, report format, compression format, S3 bucket, additional artifacts, and schema elements in the definition.
    """

    ReportName: ReportName
    TimeUnit: TimeUnit
    Format: ReportFormat
    Compression: CompressionFormat
    AdditionalSchemaElements: SchemaElementList
    S3Bucket: S3Bucket
    S3Prefix: S3Prefix
    S3Region: AWSRegion
    AdditionalArtifacts: Optional[AdditionalArtifactList] = None
    RefreshClosedReports: Optional[RefreshClosedReports] = None
    ReportVersioning: Optional[ReportVersioning] = None
    BillingViewArn: Optional[BillingViewArn] = None


class ModifyReportDefinitionRequest(BaseModel):
    ReportName: ReportName
    ReportDefinition: ReportDefinition


class PutReportDefinitionRequest(BaseModel):
    """
    Creates a Cost and Usage Report.
    """

    ReportDefinition: ReportDefinition


class ReportDefinitionList(BaseModel):
    """
    A list of report definitions.
    """

    __root__: Annotated[
        List[ReportDefinition], Field(description='A list of report definitions.')
    ]


class DescribeReportDefinitionsResponse(BaseModel):
    """
    If the action is successful, the service sends back an HTTP 200 response.
    """

    ReportDefinitions: Optional[ReportDefinitionList] = None
    NextToken: Optional[GenericString] = None
