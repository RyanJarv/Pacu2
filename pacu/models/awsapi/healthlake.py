# generated by datamodel-codegen:
#   filename:  openapi.yaml
#   timestamp: 2021-12-31T02:50:17+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Annotated, Any, List, Optional

from pydantic import BaseModel, Field


class ValidationException(BaseModel):
    __root__: Any


class ThrottlingException(ValidationException):
    pass


class AccessDeniedException(ValidationException):
    pass


class InternalServerException(ValidationException):
    pass


class ConflictException(ValidationException):
    pass


class ResourceNotFoundException(ValidationException):
    pass


class TagResourceResponse(BaseModel):
    pass


class UntagResourceResponse(TagResourceResponse):
    pass


class AmazonResourceName(BaseModel):
    __root__: Annotated[
        str,
        Field(
            max_length=1011,
            min_length=1,
            regex='^arn:aws((-us-gov)|(-iso)|(-iso-b)|(-cn))?:healthlake:[a-z0-9-]+:\\d{12}:datastore\\/fhir\\/.{32}',
        ),
    ]


class BoundedLengthString(BaseModel):
    __root__: Annotated[
        str, Field(max_length=5000, min_length=1, regex='[\\P{M}\\p{M}]{1,5000}')
    ]


class ClientTokenString(BaseModel):
    __root__: Annotated[
        str, Field(max_length=64, min_length=1, regex='^[a-zA-Z0-9-]+$')
    ]


class CmkType(Enum):
    CUSTOMER_MANAGED_KMS_KEY = 'CUSTOMER_MANAGED_KMS_KEY'
    AWS_OWNED_KMS_KEY = 'AWS_OWNED_KMS_KEY'


class DatastoreName(BaseModel):
    __root__: Annotated[
        str,
        Field(
            max_length=256, min_length=1, regex='^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-%@]*)$'
        ),
    ]


class FHIRVersion(Enum):
    R4 = 'R4'


class DatastoreId(BaseModel):
    __root__: Annotated[
        str,
        Field(
            max_length=32, min_length=1, regex='^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-%@]*)$'
        ),
    ]


class DatastoreArn(BaseModel):
    __root__: Annotated[
        str,
        Field(
            regex='^arn:aws((-us-gov)|(-iso)|(-iso-b)|(-cn))?:healthlake:[a-zA-Z0-9-]+:[0-9]{12}:datastore/.+?'
        ),
    ]


class DatastoreStatus(Enum):
    CREATING = 'CREATING'
    ACTIVE = 'ACTIVE'
    DELETING = 'DELETING'
    DELETED = 'DELETED'


class Timestamp(BaseModel):
    __root__: datetime


class DatastoreFilter(BaseModel):
    """
    The filters applied to Data Store query.
    """

    DatastoreName: Optional[DatastoreName] = None
    DatastoreStatus: Optional[DatastoreStatus] = None
    CreatedBefore: Optional[Timestamp] = None
    CreatedAfter: Optional[Timestamp] = None


class String(BaseModel):
    __root__: Annotated[str, Field(max_length=10000, regex='[\\P{M}\\p{M}]{0,10000}')]


class JobId(DatastoreId):
    pass


class EncryptionKeyID(BaseModel):
    __root__: Annotated[
        str,
        Field(
            max_length=400,
            min_length=1,
            regex='(arn:aws((-us-gov)|(-iso)|(-iso-b)|(-cn))?:kms:)?([a-z]{2}-[a-z]+(-[a-z]+)?-\\d:)?(\\d{12}:)?(((key/)?[a-zA-Z0-9-_]+)|(alias/[a-zA-Z0-9:/_-]+))',
        ),
    ]


class JobName(BaseModel):
    __root__: Annotated[
        str,
        Field(
            max_length=64, min_length=1, regex='^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-%@]*)$'
        ),
    ]


class JobStatus(Enum):
    SUBMITTED = 'SUBMITTED'
    IN_PROGRESS = 'IN_PROGRESS'
    COMPLETED_WITH_ERRORS = 'COMPLETED_WITH_ERRORS'
    COMPLETED = 'COMPLETED'
    FAILED = 'FAILED'


class IamRoleArn(BaseModel):
    __root__: Annotated[
        str,
        Field(
            max_length=2048,
            min_length=20,
            regex='arn:aws(-[^:]+)?:iam::[0-9]{12}:role/.+',
        ),
    ]


class Message(BaseModel):
    __root__: Annotated[
        str,
        Field(
            max_length=2048, min_length=1, regex='^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-%@]*)$'
        ),
    ]


class S3Uri(BaseModel):
    __root__: Annotated[
        str,
        Field(max_length=1024, regex='s3://[a-z0-9][\\.\\-a-z0-9]{1,61}[a-z0-9](/.*)?'),
    ]


class KmsEncryptionConfig(BaseModel):
    """
    The customer-managed-key(CMK) used when creating a Data Store. If a customer owned key is not specified, an AWS owned key will be used for encryption.
    """

    CmkType: CmkType
    KmsKeyId: Optional[EncryptionKeyID] = None


class NextToken(BaseModel):
    __root__: Annotated[str, Field(max_length=8192, regex='\\p{ASCII}{0,8192}')]


class MaxResultsInteger(BaseModel):
    __root__: Annotated[int, Field(ge=1.0, le=500.0)]


class S3Configuration(BaseModel):
    """
    The configuration of the S3 bucket for either an import or export job. This includes assigning permissions for access.
    """

    S3Uri: S3Uri
    KmsKeyId: EncryptionKeyID


class PreloadDataType(Enum):
    SYNTHEA = 'SYNTHEA'


class TagKey(BaseModel):
    __root__: Annotated[
        str,
        Field(
            max_length=128, min_length=1, regex='^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-@]*)$'
        ),
    ]


class TagValue(BaseModel):
    __root__: Annotated[
        str,
        Field(
            max_length=256, min_length=0, regex='^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-@]*)$'
        ),
    ]


class Tag(BaseModel):
    """
    A tag is a label consisting of a user-defined key and value. The form for tags is {"Key", "Value"}
    """

    Key: TagKey
    Value: TagValue


class TagKeyList(BaseModel):
    __root__: Annotated[List[TagKey], Field(max_items=200, min_items=0)]


class CreateFHIRDatastoreResponse(BaseModel):
    DatastoreId: DatastoreId
    DatastoreArn: DatastoreArn
    DatastoreStatus: DatastoreStatus
    DatastoreEndpoint: BoundedLengthString


class DeleteFHIRDatastoreResponse(CreateFHIRDatastoreResponse):
    pass


class DeleteFHIRDatastoreRequest(BaseModel):
    DatastoreId: Optional[DatastoreId] = None


class DescribeFHIRDatastoreRequest(BaseModel):
    DatastoreId: Optional[DatastoreId] = None


class DescribeFHIRExportJobRequest(BaseModel):
    DatastoreId: DatastoreId
    JobId: JobId


class DescribeFHIRImportJobRequest(BaseModel):
    DatastoreId: DatastoreId
    JobId: JobId


class ListFHIRDatastoresRequest(BaseModel):
    Filter: Optional[DatastoreFilter] = None
    NextToken: Optional[NextToken] = None
    MaxResults: Optional[MaxResultsInteger] = None


class ListFHIRExportJobsRequest(BaseModel):
    DatastoreId: DatastoreId
    NextToken: Optional[NextToken] = None
    MaxResults: Optional[MaxResultsInteger] = None
    JobName: Optional[JobName] = None
    JobStatus: Optional[JobStatus] = None
    SubmittedBefore: Optional[Timestamp] = None
    SubmittedAfter: Optional[Timestamp] = None


class ListFHIRImportJobsRequest(BaseModel):
    DatastoreId: DatastoreId
    NextToken: Optional[NextToken] = None
    MaxResults: Optional[MaxResultsInteger] = None
    JobName: Optional[JobName] = None
    JobStatus: Optional[JobStatus] = None
    SubmittedBefore: Optional[Timestamp] = None
    SubmittedAfter: Optional[Timestamp] = None


class ListTagsForResourceRequest(BaseModel):
    ResourceARN: AmazonResourceName


class StartFHIRExportJobResponse(BaseModel):
    JobId: JobId
    JobStatus: JobStatus
    DatastoreId: Optional[DatastoreId] = None


class StartFHIRImportJobResponse(StartFHIRExportJobResponse):
    pass


class UntagResourceRequest(BaseModel):
    ResourceARN: AmazonResourceName
    TagKeys: TagKeyList


class SseConfiguration(BaseModel):
    """
    The server-side encryption key configuration for a customer provided encryption key.
    """

    KmsEncryptionConfig: KmsEncryptionConfig


class PreloadDataConfig(BaseModel):
    """
    The input properties for the preloaded Data Store. Only data preloaded from Synthea is supported.
    """

    PreloadDataType: PreloadDataType


class TagList(BaseModel):
    __root__: Annotated[List[Tag], Field(max_items=200, min_items=0)]


class DatastoreProperties(BaseModel):
    """
    Displays the properties of the Data Store, including the ID, Arn, name, and the status of the Data Store.
    """

    DatastoreId: DatastoreId
    DatastoreArn: DatastoreArn
    DatastoreName: Optional[DatastoreName] = None
    DatastoreStatus: DatastoreStatus
    CreatedAt: Optional[Timestamp] = None
    DatastoreTypeVersion: FHIRVersion
    DatastoreEndpoint: String
    SseConfiguration: Optional[SseConfiguration] = None
    PreloadDataConfig: Optional[PreloadDataConfig] = None


class DatastorePropertiesList(BaseModel):
    __root__: List[DatastoreProperties]


class OutputDataConfig(BaseModel):
    """
    The output data configuration that was supplied when the export job was created.
    """

    S3Configuration: Optional[S3Configuration] = None


class InputDataConfig(BaseModel):
    """
    The input properties for an import job.
    """

    S3Uri: Optional[S3Uri] = None


class CreateFHIRDatastoreRequest(BaseModel):
    DatastoreName: Optional[DatastoreName] = None
    DatastoreTypeVersion: FHIRVersion
    SseConfiguration: Optional[SseConfiguration] = None
    PreloadDataConfig: Optional[PreloadDataConfig] = None
    ClientToken: Optional[ClientTokenString] = None
    Tags: Optional[TagList] = None


class DescribeFHIRDatastoreResponse(BaseModel):
    DatastoreProperties: DatastoreProperties


class ListFHIRDatastoresResponse(BaseModel):
    DatastorePropertiesList: DatastorePropertiesList
    NextToken: Optional[NextToken] = None


class ListTagsForResourceResponse(BaseModel):
    Tags: Optional[TagList] = None


class StartFHIRExportJobRequest(BaseModel):
    JobName: Optional[JobName] = None
    OutputDataConfig: OutputDataConfig
    DatastoreId: DatastoreId
    DataAccessRoleArn: IamRoleArn
    ClientToken: ClientTokenString


class StartFHIRImportJobRequest(BaseModel):
    JobName: Optional[JobName] = None
    InputDataConfig: InputDataConfig
    JobOutputDataConfig: OutputDataConfig
    DatastoreId: DatastoreId
    DataAccessRoleArn: IamRoleArn
    ClientToken: ClientTokenString


class TagResourceRequest(BaseModel):
    ResourceARN: AmazonResourceName
    Tags: TagList


class ExportJobProperties(BaseModel):
    """
    The properties of a FHIR export job, including the ID, ARN, name, and the status of the job.
    """

    JobId: JobId
    JobName: Optional[JobName] = None
    JobStatus: JobStatus
    SubmitTime: Timestamp
    EndTime: Optional[Timestamp] = None
    DatastoreId: DatastoreId
    OutputDataConfig: OutputDataConfig
    DataAccessRoleArn: Optional[IamRoleArn] = None
    Message: Optional[Message] = None


class ImportJobProperties(BaseModel):
    """
    Displays the properties of the import job, including the ID, Arn, Name, and the status of the Data Store.
    """

    JobId: JobId
    JobName: Optional[JobName] = None
    JobStatus: JobStatus
    SubmitTime: Timestamp
    EndTime: Optional[Timestamp] = None
    DatastoreId: DatastoreId
    InputDataConfig: InputDataConfig
    JobOutputDataConfig: Optional[OutputDataConfig] = None
    DataAccessRoleArn: Optional[IamRoleArn] = None
    Message: Optional[Message] = None


class ExportJobPropertiesList(BaseModel):
    __root__: List[ExportJobProperties]


class ImportJobPropertiesList(BaseModel):
    __root__: List[ImportJobProperties]


class DescribeFHIRExportJobResponse(BaseModel):
    ExportJobProperties: ExportJobProperties


class DescribeFHIRImportJobResponse(BaseModel):
    ImportJobProperties: ImportJobProperties


class ListFHIRExportJobsResponse(BaseModel):
    ExportJobPropertiesList: ExportJobPropertiesList
    NextToken: Optional[NextToken] = None


class ListFHIRImportJobsResponse(BaseModel):
    ImportJobPropertiesList: ImportJobPropertiesList
    NextToken: Optional[NextToken] = None
