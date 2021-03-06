# generated by datamodel-codegen:
#   filename:  openapi.yaml
#   timestamp: 2021-12-31T02:49:29+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Annotated, Any, Optional

from pydantic import BaseModel, Extra, Field


class StringMapValue(BaseModel):
    __root__: str


class ResourceNotFoundException(BaseModel):
    __root__: Any


class InternalServerException(ResourceNotFoundException):
    pass


class ValidationException(ResourceNotFoundException):
    pass


class ThrottlingException(ResourceNotFoundException):
    pass


class AccessDeniedException(ResourceNotFoundException):
    pass


class ChangeType(Enum):
    REPLACE = 'REPLACE'
    APPEND = 'APPEND'
    MODIFY = 'MODIFY'


class IdType(BaseModel):
    __root__: Annotated[str, Field(max_length=26, min_length=1)]


class Arn(BaseModel):
    __root__: Annotated[str, Field(max_length=2048, min_length=20)]


class SourceType(Enum):
    S3 = 'S3'


class StringMap(BaseModel):
    pass

    class Config:
        extra = Extra.allow


class FormatType(Enum):
    CSV = 'CSV'
    JSON = 'JSON'
    PARQUET = 'PARQUET'
    XML = 'XML'


class Timestamp(BaseModel):
    __root__: datetime


class ChangesetStatus(Enum):
    PENDING = 'PENDING'
    FAILED = 'FAILED'
    SUCCESS = 'SUCCESS'
    RUNNING = 'RUNNING'
    STOP_REQUESTED = 'STOP_REQUESTED'


class StringValue(StringMapValue):
    pass


class CreateChangesetRequest(BaseModel):
    changeType: ChangeType
    sourceType: SourceType
    sourceParams: StringMap
    formatType: Optional[FormatType] = None
    formatParams: Optional[StringMap] = None
    tags: Optional[StringMap] = None


class StringValueLength1to255(BaseModel):
    __root__: Annotated[str, Field(max_length=255, min_length=1)]


class StringValueMaxLength1000(BaseModel):
    __root__: Annotated[str, Field(max_length=1000)]


class Credentials(BaseModel):
    """
    Set short term API credentials.
    """

    accessKeyId: Optional[StringValueLength1to255] = None
    secretAccessKey: Optional[StringValueMaxLength1000] = None
    sessionToken: Optional[StringValueMaxLength1000] = None


class ErrorCategory(Enum):
    The_inputs_to_this_request_are_invalid = 'The_inputs_to_this_request_are_invalid'
    Service_limits_have_been_exceeded = 'Service_limits_have_been_exceeded'
    Missing_required_permission_to_perform_this_request = (
        'Missing_required_permission_to_perform_this_request'
    )
    One_or_more_inputs_to_this_request_were_not_found = (
        'One_or_more_inputs_to_this_request_were_not_found'
    )
    The_system_temporarily_lacks_sufficient_resources_to_process_the_request = (
        'The_system_temporarily_lacks_sufficient_resources_to_process_the_request'
    )
    An_internal_error_has_occurred = 'An_internal_error_has_occurred'
    Cancelled = 'Cancelled'
    A_user_recoverable_error_has_occurred = 'A_user_recoverable_error_has_occurred'


class SessionDuration(BaseModel):
    __root__: Annotated[int, Field(ge=60.0, le=720.0)]


class GetProgrammaticAccessCredentialsRequest(BaseModel):
    pass


class LocationType(Enum):
    INGESTION = 'INGESTION'
    SAGEMAKER = 'SAGEMAKER'


class GetWorkingLocationRequest(BaseModel):
    locationType: Optional[LocationType] = None


class StringValueLength1to1024(BaseModel):
    __root__: Annotated[str, Field(max_length=1024, min_length=1, regex='.*\\S.*')]


class StringValueLength1to63(BaseModel):
    __root__: Annotated[str, Field(max_length=63, min_length=1, regex='.*\\S.*')]


class StringMapKey(StringMapValue):
    pass


class GetProgrammaticAccessCredentialsResponse(BaseModel):
    credentials: Optional[Credentials] = None
    durationInMinutes: Optional[SessionDuration] = None


class GetWorkingLocationResponse(BaseModel):
    s3Uri: Optional[StringValueLength1to1024] = None
    s3Path: Optional[StringValueLength1to1024] = None
    s3Bucket: Optional[StringValueLength1to63] = None


class ErrorInfo(BaseModel):
    """
    Error message.
    """

    errorMessage: Optional[StringValueMaxLength1000] = None
    errorCategory: Optional[ErrorCategory] = None


class ChangesetInfo(BaseModel):
    """
    A changeset is unit of data in a dataset.
    """

    id: Optional[IdType] = None
    changesetArn: Optional[Arn] = None
    datasetId: Optional[IdType] = None
    changeType: Optional[ChangeType] = None
    sourceType: Optional[SourceType] = None
    sourceParams: Optional[StringMap] = None
    formatType: Optional[FormatType] = None
    formatParams: Optional[StringMap] = None
    createTimestamp: Optional[Timestamp] = None
    status: Optional[ChangesetStatus] = None
    errorInfo: Optional[ErrorInfo] = None
    changesetLabels: Optional[StringMap] = None
    updatesChangesetId: Optional[StringValue] = None
    updatedByChangesetId: Optional[StringValue] = None


class CreateChangesetResponse(BaseModel):
    changeset: Optional[ChangesetInfo] = None
