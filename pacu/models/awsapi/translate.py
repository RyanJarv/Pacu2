# generated by datamodel-codegen:
#   filename:  openapi.yaml
#   timestamp: 2021-12-31T02:59:19+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Annotated, Any, List, Optional

from pydantic import BaseModel, Field, SecretStr


class InvalidParameterValueException(BaseModel):
    __root__: Any


class InvalidRequestException(InvalidParameterValueException):
    pass


class LimitExceededException(InvalidParameterValueException):
    pass


class TooManyRequestsException(InvalidParameterValueException):
    pass


class ConflictException(InvalidParameterValueException):
    pass


class InternalServerException(InvalidParameterValueException):
    pass


class ConcurrentModificationException(InvalidParameterValueException):
    pass


class ResourceNotFoundException(InvalidParameterValueException):
    pass


class InvalidFilterException(InvalidParameterValueException):
    pass


class UnsupportedLanguagePairException(InvalidParameterValueException):
    pass


class TextSizeLimitExceededException(InvalidParameterValueException):
    pass


class DetectedLanguageLowConfidenceException(InvalidParameterValueException):
    pass


class ServiceUnavailableException(InvalidParameterValueException):
    pass


class ResourceName(BaseModel):
    __root__: Annotated[
        str, Field(max_length=256, min_length=1, regex='^([A-Za-z0-9-]_?)+$')
    ]


class BoundedLengthString(BaseModel):
    __root__: Annotated[
        str, Field(max_length=5000, min_length=1, regex='[\\P{M}\\p{M}]{1,5000}')
    ]


class ClientTokenString(BaseModel):
    __root__: Annotated[
        str, Field(max_length=64, min_length=1, regex='^[a-zA-Z0-9-]+$')
    ]


class ContentType(BaseModel):
    __root__: Annotated[str, Field(max_length=256, regex='^[-\\w.]+\\/[-\\w.+]+$')]


class Description(BaseModel):
    __root__: Annotated[str, Field(max_length=256, regex='[\\P{M}\\p{M}]{0,256}')]


class ParallelDataStatus(Enum):
    CREATING = 'CREATING'
    UPDATING = 'UPDATING'
    ACTIVE = 'ACTIVE'
    DELETING = 'DELETING'
    FAILED = 'FAILED'


class JobId(BaseModel):
    __root__: Annotated[
        str,
        Field(
            max_length=32, min_length=1, regex='^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-%@]*)$'
        ),
    ]


class EncryptionKeyType(Enum):
    KMS = 'KMS'


class EncryptionKeyID(BaseModel):
    __root__: Annotated[
        str,
        Field(
            max_length=400,
            min_length=1,
            regex='(arn:aws((-us-gov)|(-iso)|(-iso-b)|(-cn))?:kms:)?([a-z]{2}-[a-z]+(-[a-z]+)?-\\d:)?(\\d{12}:)?(((key/)?[a-zA-Z0-9-_]+)|(alias/[a-zA-Z0-9:/_-]+))',
        ),
    ]


class TerminologyDataFormat(Enum):
    CSV = 'CSV'
    TMX = 'TMX'


class IamRoleArn(BaseModel):
    __root__: Annotated[
        str,
        Field(
            max_length=2048,
            min_length=20,
            regex='arn:aws(-[^:]+)?:iam::[0-9]{12}:role/.+',
        ),
    ]


class MergeStrategy(Enum):
    OVERWRITE = 'OVERWRITE'


class S3Uri(BaseModel):
    __root__: Annotated[
        str,
        Field(max_length=1024, regex='s3://[a-z0-9][\\.\\-a-z0-9]{1,61}[a-z0-9](/.*)?'),
    ]


class InputDataConfig(BaseModel):
    """
    The input configuration properties for requesting a batch translation job.
    """

    S3Uri: S3Uri
    ContentType: ContentType


class Integer(BaseModel):
    __root__: int


class JobDetails(BaseModel):
    """
    The number of documents successfully and unsuccessfully processed during a translation job.
    """

    TranslatedDocumentsCount: Optional[Integer] = None
    DocumentsWithErrorsCount: Optional[Integer] = None
    InputDocumentsCount: Optional[Integer] = None


class JobName(BaseModel):
    __root__: Annotated[
        str,
        Field(
            max_length=256, min_length=1, regex='^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-%@]*)$'
        ),
    ]


class JobStatus(Enum):
    SUBMITTED = 'SUBMITTED'
    IN_PROGRESS = 'IN_PROGRESS'
    COMPLETED = 'COMPLETED'
    COMPLETED_WITH_ERROR = 'COMPLETED_WITH_ERROR'
    FAILED = 'FAILED'
    STOP_REQUESTED = 'STOP_REQUESTED'
    STOPPED = 'STOPPED'


class LanguageCodeString(BaseModel):
    __root__: Annotated[str, Field(max_length=5, min_length=2)]


class LanguageCodeStringList(BaseModel):
    __root__: List[LanguageCodeString]


class NextToken(BaseModel):
    __root__: Annotated[str, Field(max_length=8192, regex='\\p{ASCII}{0,8192}')]


class MaxResultsInteger(BaseModel):
    __root__: Annotated[int, Field(ge=1.0, le=500.0)]


class Long(Integer):
    pass


class OutputDataConfig(BaseModel):
    """
    The output configuration properties for a batch translation job.
    """

    S3Uri: S3Uri


class ParallelDataArn(BaseModel):
    __root__: Annotated[str, Field(max_length=512, min_length=1)]


class ParallelDataFormat(Enum):
    TSV = 'TSV'
    CSV = 'CSV'
    TMX = 'TMX'


class String(BaseModel):
    __root__: Annotated[str, Field(max_length=10000, regex='[\\P{M}\\p{M}]{0,10000}')]


class UnboundedLengthString(BaseModel):
    __root__: str


class Timestamp(BaseModel):
    __root__: datetime


class ResourceNameList(BaseModel):
    __root__: List[ResourceName]


class TargetLanguageCodeStringList(BaseModel):
    __root__: Annotated[List[LanguageCodeString], Field(max_items=1, min_items=1)]


class Term(BaseModel):
    """
    The term being translated by the custom terminology.
    """

    SourceText: Optional[String] = None
    TargetText: Optional[String] = None


class TerminologyArn(ParallelDataArn):
    pass


class TerminologyFile(BaseModel):
    __root__: Annotated[SecretStr, Field(max_length=10485760)]


class CreateParallelDataResponse(BaseModel):
    Name: Optional[ResourceName] = None
    Status: Optional[ParallelDataStatus] = None


class DeleteParallelDataResponse(CreateParallelDataResponse):
    pass


class DeleteParallelDataRequest(BaseModel):
    Name: ResourceName


class DeleteTerminologyRequest(BaseModel):
    Name: ResourceName


class DescribeTextTranslationJobRequest(BaseModel):
    JobId: JobId


class GetParallelDataRequest(BaseModel):
    Name: ResourceName


class GetTerminologyRequest(BaseModel):
    Name: ResourceName
    TerminologyDataFormat: TerminologyDataFormat


class ListParallelDataRequest(BaseModel):
    NextToken: Optional[NextToken] = None
    MaxResults: Optional[MaxResultsInteger] = None


class ListTerminologiesRequest(BaseModel):
    NextToken: Optional[NextToken] = None
    MaxResults: Optional[MaxResultsInteger] = None


class StartTextTranslationJobResponse(BaseModel):
    JobId: Optional[JobId] = None
    JobStatus: Optional[JobStatus] = None


class StartTextTranslationJobRequest(BaseModel):
    JobName: Optional[JobName] = None
    InputDataConfig: InputDataConfig
    OutputDataConfig: OutputDataConfig
    DataAccessRoleArn: IamRoleArn
    SourceLanguageCode: LanguageCodeString
    TargetLanguageCodes: TargetLanguageCodeStringList
    TerminologyNames: Optional[ResourceNameList] = None
    ParallelDataNames: Optional[ResourceNameList] = None
    ClientToken: ClientTokenString


class StopTextTranslationJobResponse(StartTextTranslationJobResponse):
    pass


class StopTextTranslationJobRequest(BaseModel):
    JobId: JobId


class TranslateTextRequest(BaseModel):
    Text: BoundedLengthString
    TerminologyNames: Optional[ResourceNameList] = None
    SourceLanguageCode: LanguageCodeString
    TargetLanguageCode: LanguageCodeString


class UpdateParallelDataResponse(BaseModel):
    Name: Optional[ResourceName] = None
    Status: Optional[ParallelDataStatus] = None
    LatestUpdateAttemptStatus: Optional[ParallelDataStatus] = None
    LatestUpdateAttemptAt: Optional[Timestamp] = None


class TermList(BaseModel):
    __root__: List[Term]


class AppliedTerminology(BaseModel):
    """
    The custom terminology applied to the input text by Amazon Translate for the translated text response. This is optional in the response and will only be present if you specified terminology input in the request. Currently, only one terminology can be applied per TranslateText request.
    """

    Name: Optional[ResourceName] = None
    Terms: Optional[TermList] = None


class AppliedTerminologyList(BaseModel):
    __root__: List[AppliedTerminology]


class ParallelDataConfig(BaseModel):
    """
    Specifies the format and S3 location of the parallel data input file.
    """

    S3Uri: S3Uri
    Format: ParallelDataFormat


class EncryptionKey(BaseModel):
    """
    The encryption key used to encrypt this object.
    """

    Type: EncryptionKeyType
    Id: EncryptionKeyID


class TextTranslationJobProperties(BaseModel):
    """
    Provides information about a translation job.
    """

    JobId: Optional[JobId] = None
    JobName: Optional[JobName] = None
    JobStatus: Optional[JobStatus] = None
    JobDetails: Optional[JobDetails] = None
    SourceLanguageCode: Optional[LanguageCodeString] = None
    TargetLanguageCodes: Optional[TargetLanguageCodeStringList] = None
    TerminologyNames: Optional[ResourceNameList] = None
    ParallelDataNames: Optional[ResourceNameList] = None
    Message: Optional[UnboundedLengthString] = None
    SubmittedTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    InputDataConfig: Optional[InputDataConfig] = None
    OutputDataConfig: Optional[OutputDataConfig] = None
    DataAccessRoleArn: Optional[IamRoleArn] = None


class ParallelDataProperties(BaseModel):
    """
    The properties of a parallel data resource.
    """

    Name: Optional[ResourceName] = None
    Arn: Optional[ParallelDataArn] = None
    Description: Optional[Description] = None
    Status: Optional[ParallelDataStatus] = None
    SourceLanguageCode: Optional[LanguageCodeString] = None
    TargetLanguageCodes: Optional[LanguageCodeStringList] = None
    ParallelDataConfig: Optional[ParallelDataConfig] = None
    Message: Optional[UnboundedLengthString] = None
    ImportedDataSize: Optional[Long] = None
    ImportedRecordCount: Optional[Long] = None
    FailedRecordCount: Optional[Long] = None
    SkippedRecordCount: Optional[Long] = None
    EncryptionKey: Optional[EncryptionKey] = None
    CreatedAt: Optional[Timestamp] = None
    LastUpdatedAt: Optional[Timestamp] = None
    LatestUpdateAttemptStatus: Optional[ParallelDataStatus] = None
    LatestUpdateAttemptAt: Optional[Timestamp] = None


class ParallelDataDataLocation(BaseModel):
    """
    The location of the most recent parallel data input file that was successfully imported into Amazon Translate.
    """

    RepositoryType: String
    Location: String


class TerminologyProperties(BaseModel):
    """
    The properties of the custom terminology.
    """

    Name: Optional[ResourceName] = None
    Description: Optional[Description] = None
    Arn: Optional[TerminologyArn] = None
    SourceLanguageCode: Optional[LanguageCodeString] = None
    TargetLanguageCodes: Optional[LanguageCodeStringList] = None
    EncryptionKey: Optional[EncryptionKey] = None
    SizeBytes: Optional[Integer] = None
    TermCount: Optional[Integer] = None
    CreatedAt: Optional[Timestamp] = None
    LastUpdatedAt: Optional[Timestamp] = None


class TerminologyDataLocation(ParallelDataDataLocation):
    """
    The location of the custom terminology data.
    """

    pass


class TerminologyData(BaseModel):
    """
    The data associated with the custom terminology.
    """

    File: TerminologyFile
    Format: TerminologyDataFormat


class ParallelDataPropertiesList(BaseModel):
    __root__: List[ParallelDataProperties]


class TerminologyPropertiesList(BaseModel):
    __root__: List[TerminologyProperties]


class TextTranslationJobFilter(BaseModel):
    """
    Provides information for filtering a list of translation jobs. For more information, see <a>ListTextTranslationJobs</a>.
    """

    JobName: Optional[JobName] = None
    JobStatus: Optional[JobStatus] = None
    SubmittedBeforeTime: Optional[Timestamp] = None
    SubmittedAfterTime: Optional[Timestamp] = None


class TextTranslationJobPropertiesList(BaseModel):
    __root__: List[TextTranslationJobProperties]


class CreateParallelDataRequest(BaseModel):
    Name: ResourceName
    Description: Optional[Description] = None
    ParallelDataConfig: ParallelDataConfig
    EncryptionKey: Optional[EncryptionKey] = None
    ClientToken: ClientTokenString


class DescribeTextTranslationJobResponse(BaseModel):
    TextTranslationJobProperties: Optional[TextTranslationJobProperties] = None


class GetParallelDataResponse(BaseModel):
    ParallelDataProperties: Optional[ParallelDataProperties] = None
    DataLocation: Optional[ParallelDataDataLocation] = None
    AuxiliaryDataLocation: Optional[ParallelDataDataLocation] = None
    LatestUpdateAttemptAuxiliaryDataLocation: Optional[ParallelDataDataLocation] = None


class GetTerminologyResponse(BaseModel):
    TerminologyProperties: Optional[TerminologyProperties] = None
    TerminologyDataLocation: Optional[TerminologyDataLocation] = None


class ImportTerminologyResponse(BaseModel):
    TerminologyProperties: Optional[TerminologyProperties] = None


class ImportTerminologyRequest(BaseModel):
    Name: ResourceName
    MergeStrategy: MergeStrategy
    Description: Optional[Description] = None
    TerminologyData: TerminologyData
    EncryptionKey: Optional[EncryptionKey] = None


class ListParallelDataResponse(BaseModel):
    ParallelDataPropertiesList: Optional[ParallelDataPropertiesList] = None
    NextToken: Optional[NextToken] = None


class ListTerminologiesResponse(BaseModel):
    TerminologyPropertiesList: Optional[TerminologyPropertiesList] = None
    NextToken: Optional[NextToken] = None


class ListTextTranslationJobsResponse(BaseModel):
    TextTranslationJobPropertiesList: Optional[TextTranslationJobPropertiesList] = None
    NextToken: Optional[NextToken] = None


class ListTextTranslationJobsRequest(BaseModel):
    Filter: Optional[TextTranslationJobFilter] = None
    NextToken: Optional[NextToken] = None
    MaxResults: Optional[MaxResultsInteger] = None


class TranslateTextResponse(BaseModel):
    TranslatedText: String
    SourceLanguageCode: LanguageCodeString
    TargetLanguageCode: LanguageCodeString
    AppliedTerminologies: Optional[AppliedTerminologyList] = None


class UpdateParallelDataRequest(BaseModel):
    Name: ResourceName
    Description: Optional[Description] = None
    ParallelDataConfig: ParallelDataConfig
    ClientToken: ClientTokenString
