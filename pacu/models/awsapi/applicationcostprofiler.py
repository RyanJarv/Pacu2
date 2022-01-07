# generated by datamodel-codegen:
#   filename:  openapi.yaml
#   timestamp: 2021-12-31T02:45:07+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Annotated, Any, List, Optional

from pydantic import BaseModel, Field


class InternalServerException(BaseModel):
    __root__: Any


class ThrottlingException(InternalServerException):
    pass


class ValidationException(InternalServerException):
    pass


class AccessDeniedException(InternalServerException):
    pass


class S3Bucket(BaseModel):
    __root__: Annotated[
        str,
        Field(
            max_length=63,
            min_length=3,
            regex='(?=^.{3,63}$)(?!^(\\d+\\.)+\\d+$)(^(([a-z0-9]|[a-z0-9][a-z0-9\\-]*[a-z0-9])\\.)*([a-z0-9]|[a-z0-9][a-z0-9\\-]*[a-z0-9])$)',
        ),
    ]


class S3Key(BaseModel):
    __root__: Annotated[str, Field(max_length=512, min_length=1, regex='.*\\S.*')]


class S3BucketRegion(Enum):
    ap_east_1 = 'ap-east-1'
    me_south_1 = 'me-south-1'
    eu_south_1 = 'eu-south-1'
    af_south_1 = 'af-south-1'


class S3Prefix(S3Key):
    pass


class ServiceQuotaExceededException(InternalServerException):
    pass


class ReportId(BaseModel):
    __root__: Annotated[
        str, Field(max_length=255, min_length=1, regex='^[0-9A-Za-z\\.\\-_]+$')
    ]


class DeleteReportDefinitionRequest(BaseModel):
    pass


class Format(Enum):
    CSV = 'CSV'
    PARQUET = 'PARQUET'


class GetReportDefinitionRequest(BaseModel):
    pass


class ReportDescription(BaseModel):
    __root__: Annotated[str, Field(max_length=1024, min_length=1, regex='.*\\S.*')]


class ReportFrequency(Enum):
    MONTHLY = 'MONTHLY'
    DAILY = 'DAILY'
    ALL = 'ALL'


class S3Location(BaseModel):
    """
    Represents the Amazon Simple Storage Service (Amazon S3) location where AWS Application Cost Profiler reports are generated and then written to.
    """

    bucket: S3Bucket
    prefix: S3Prefix


class Timestamp(BaseModel):
    __root__: datetime


class SourceS3Location(BaseModel):
    """
    Represents the Amazon Simple Storage Service (Amazon S3) location where usage data is read from.
    """

    bucket: S3Bucket
    key: S3Key
    region: Optional[S3BucketRegion] = None


class ImportApplicationUsageRequest(BaseModel):
    sourceS3Location: SourceS3Location


class ImportId(BaseModel):
    __root__: Annotated[
        str, Field(max_length=255, min_length=1, regex='[0-9A-Za-z\\.\\-_]*')
    ]


class Integer(BaseModel):
    __root__: Annotated[int, Field(ge=1.0, le=100.0)]


class Token(BaseModel):
    __root__: Annotated[
        str,
        Field(
            max_length=102400,
            min_length=1,
            regex='^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$',
        ),
    ]


class ListReportDefinitionsRequest(BaseModel):
    pass


class PutReportDefinitionRequest(BaseModel):
    reportId: ReportId
    reportDescription: ReportDescription
    reportFrequency: ReportFrequency
    format: Format
    destinationS3Location: S3Location


class ReportDefinition(BaseModel):
    """
    The configuration of a report in AWS Application Cost Profiler.
    """

    reportId: Optional[ReportId] = None
    reportDescription: Optional[ReportDescription] = None
    reportFrequency: Optional[ReportFrequency] = None
    format: Optional[Format] = None
    destinationS3Location: Optional[S3Location] = None
    createdAt: Optional[Timestamp] = None
    lastUpdatedAt: Optional[Timestamp] = None


class UpdateReportDefinitionRequest(BaseModel):
    reportDescription: ReportDescription
    reportFrequency: ReportFrequency
    format: Format
    destinationS3Location: S3Location


class DeleteReportDefinitionResult(BaseModel):
    reportId: Optional[ReportId] = None


class GetReportDefinitionResult(BaseModel):
    reportId: ReportId
    reportDescription: ReportDescription
    reportFrequency: ReportFrequency
    format: Format
    destinationS3Location: S3Location
    createdAt: Timestamp
    lastUpdated: Timestamp


class ImportApplicationUsageResult(BaseModel):
    importId: ImportId


class PutReportDefinitionResult(DeleteReportDefinitionResult):
    pass


class UpdateReportDefinitionResult(DeleteReportDefinitionResult):
    pass


class ReportDefinitionList(BaseModel):
    __root__: List[ReportDefinition]


class ListReportDefinitionsResult(BaseModel):
    reportDefinitions: Optional[ReportDefinitionList] = None
    nextToken: Optional[Token] = None