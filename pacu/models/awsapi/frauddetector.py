# generated by datamodel-codegen:
#   filename:  openapi.yaml
#   timestamp: 2021-12-31T02:49:42+00:00

from __future__ import annotations

from enum import Enum
from typing import Annotated, Any, List, Optional

from pydantic import BaseModel, Extra, Field, SecretStr


class ValidationException(BaseModel):
    __root__: Any


class InternalServerException(ValidationException):
    pass


class ThrottlingException(ValidationException):
    pass


class AccessDeniedException(ValidationException):
    pass


class CancelBatchPredictionJobResult(BaseModel):
    pass


class ResourceNotFoundException(ValidationException):
    pass


class CreateBatchPredictionJobResult(CancelBatchPredictionJobResult):
    pass


class CreateModelResult(CancelBatchPredictionJobResult):
    pass


class CreateVariableResult(CancelBatchPredictionJobResult):
    pass


class DeleteBatchPredictionJobResult(CancelBatchPredictionJobResult):
    pass


class DeleteDetectorResult(CancelBatchPredictionJobResult):
    pass


class ConflictException(ValidationException):
    pass


class DeleteDetectorVersionResult(CancelBatchPredictionJobResult):
    pass


class DeleteEntityTypeResult(CancelBatchPredictionJobResult):
    pass


class DeleteEventResult(CancelBatchPredictionJobResult):
    pass


class DeleteEventTypeResult(CancelBatchPredictionJobResult):
    pass


class DeleteExternalModelResult(CancelBatchPredictionJobResult):
    pass


class DeleteLabelResult(CancelBatchPredictionJobResult):
    pass


class DeleteModelResult(CancelBatchPredictionJobResult):
    pass


class DeleteModelVersionResult(CancelBatchPredictionJobResult):
    pass


class DeleteOutcomeResult(CancelBatchPredictionJobResult):
    pass


class DeleteRuleResult(CancelBatchPredictionJobResult):
    pass


class DeleteVariableResult(CancelBatchPredictionJobResult):
    pass


class ResourceUnavailableException(ValidationException):
    pass


class PutDetectorResult(CancelBatchPredictionJobResult):
    pass


class PutEntityTypeResult(CancelBatchPredictionJobResult):
    pass


class PutEventTypeResult(CancelBatchPredictionJobResult):
    pass


class PutExternalModelResult(CancelBatchPredictionJobResult):
    pass


class PutKMSEncryptionKeyResult(CancelBatchPredictionJobResult):
    pass


class PutLabelResult(CancelBatchPredictionJobResult):
    pass


class PutOutcomeResult(CancelBatchPredictionJobResult):
    pass


class TagResourceResult(CancelBatchPredictionJobResult):
    pass


class UntagResourceResult(CancelBatchPredictionJobResult):
    pass


class UpdateDetectorVersionResult(CancelBatchPredictionJobResult):
    pass


class UpdateDetectorVersionMetadataResult(CancelBatchPredictionJobResult):
    pass


class UpdateDetectorVersionStatusResult(CancelBatchPredictionJobResult):
    pass


class UpdateModelResult(CancelBatchPredictionJobResult):
    pass


class UpdateModelVersionStatusResult(CancelBatchPredictionJobResult):
    pass


class UpdateRuleMetadataResult(CancelBatchPredictionJobResult):
    pass


class UpdateVariableResult(CancelBatchPredictionJobResult):
    pass


class AsyncJobStatus(Enum):
    IN_PROGRESS_INITIALIZING = 'IN_PROGRESS_INITIALIZING'
    IN_PROGRESS = 'IN_PROGRESS'
    CANCEL_IN_PROGRESS = 'CANCEL_IN_PROGRESS'
    CANCELED = 'CANCELED'
    COMPLETE = 'COMPLETE'
    FAILED = 'FAILED'


class String(BaseModel):
    __root__: str


class Integer(BaseModel):
    __root__: int


class BatchCreateVariableError(BaseModel):
    """
    Provides the error of the batch create variable API.
    """

    name: Optional[String] = None
    code: Optional[Integer] = None
    message: Optional[String] = None


class BatchCreateVariableErrorList(BaseModel):
    __root__: List[BatchCreateVariableError]


class BatchGetVariableError(BatchCreateVariableError):
    """
    Provides the error of the batch get variable API.
    """

    pass


class BatchGetVariableErrorList(BaseModel):
    __root__: List[BatchGetVariableError]


class NameList(BaseModel):
    __root__: Annotated[List[String], Field(max_items=100, min_items=1)]


class Identifier(BaseModel):
    __root__: Annotated[str, Field(max_length=64, min_length=1, regex='^[0-9a-z_-]+$')]


class Time(BaseModel):
    __root__: Annotated[str, Field(max_length=30, min_length=11)]


class S3BucketLocation(BaseModel):
    __root__: Annotated[
        str, Field(max_length=512, min_length=1, regex='^s3:\\/\\/(.+)$')
    ]


class FloatVersionString(BaseModel):
    __root__: Annotated[
        str, Field(max_length=7, min_length=3, regex='^[1-9][0-9]{0,3}\\.[0-9]{1,2}$')
    ]


class IamRoleArn(BaseModel):
    __root__: Annotated[
        str,
        Field(
            max_length=256,
            min_length=1,
            regex='^arn\\:aws[a-z-]{0,15}\\:iam\\:\\:[0-9]{12}\\:role\\/[^\\s]{2,64}$',
        ),
    ]


class FraudDetectorArn(BaseModel):
    __root__: Annotated[
        str,
        Field(
            max_length=256,
            min_length=1,
            regex='^arn\\:aws[a-z-]{0,15}\\:frauddetector\\:[a-z0-9-]{3,20}\\:[0-9]{12}\\:[^\\s]{2,128}$',
        ),
    ]


class Integer1(Integer):
    pass


class BatchPrediction(BaseModel):
    """
    The batch prediction details.
    """

    jobId: Optional[Identifier] = None
    status: Optional[AsyncJobStatus] = None
    failureReason: Optional[String] = None
    startTime: Optional[Time] = None
    completionTime: Optional[Time] = None
    lastHeartbeatTime: Optional[Time] = None
    inputPath: Optional[S3BucketLocation] = None
    outputPath: Optional[S3BucketLocation] = None
    eventTypeName: Optional[Identifier] = None
    detectorName: Optional[Identifier] = None
    detectorVersion: Optional[FloatVersionString] = None
    iamRoleArn: Optional[IamRoleArn] = None
    arn: Optional[FraudDetectorArn] = None
    processedRecordsCount: Optional[Integer1] = None
    totalRecordsCount: Optional[Integer1] = None


class BatchPredictionList(BaseModel):
    __root__: List[BatchPrediction]


class WholeNumberVersionString(BaseModel):
    __root__: Annotated[str, Field(max_length=5, min_length=1, regex='^([1-9][0-9]*)$')]


class Description(BaseModel):
    __root__: Annotated[str, Field(max_length=128, min_length=1)]


class ListOfStrings(BaseModel):
    __root__: List[String]


class RuleExecutionMode(Enum):
    ALL_MATCHED = 'ALL_MATCHED'
    FIRST_MATCHED = 'FIRST_MATCHED'


class NonEmptyString(BaseModel):
    __root__: Annotated[str, Field(min_length=1)]


class DetectorVersionStatus(Enum):
    DRAFT = 'DRAFT'
    ACTIVE = 'ACTIVE'
    INACTIVE = 'INACTIVE'


class ModelIdentifier(BaseModel):
    __root__: Annotated[str, Field(max_length=64, min_length=1, regex='^[0-9a-z_]+$')]


class ModelTypeEnum(Enum):
    ONLINE_FRAUD_INSIGHTS = 'ONLINE_FRAUD_INSIGHTS'


class TrainingDataSourceEnum(Enum):
    EXTERNAL_EVENTS = 'EXTERNAL_EVENTS'


class ExternalEventsDetail(BaseModel):
    """
    Details for the external events data used for model version training.
    """

    dataLocation: S3BucketLocation
    dataAccessRoleArn: IamRoleArn


class RuleExpression(BaseModel):
    __root__: Annotated[SecretStr, Field(max_length=4096, min_length=1)]


class Language(Enum):
    DETECTORPL = 'DETECTORPL'


class NonEmptyListOfStrings(BaseModel):
    __root__: Annotated[List[String], Field(min_items=1)]


class Rule(BaseModel):
    """
    A rule.
    """

    detectorId: Identifier
    ruleId: Identifier
    ruleVersion: WholeNumberVersionString


class DataType(Enum):
    STRING = 'STRING'
    INTEGER = 'INTEGER'
    FLOAT = 'FLOAT'
    BOOLEAN = 'BOOLEAN'


class DataSource(Enum):
    EVENT = 'EVENT'
    MODEL_SCORE = 'MODEL_SCORE'
    EXTERNAL_MODEL_SCORE = 'EXTERNAL_MODEL_SCORE'


class CsvIndexToVariableMap(BaseModel):
    pass

    class Config:
        extra = Extra.allow


class SageMakerEndpointIdentifier(BaseModel):
    __root__: Annotated[
        str, Field(max_length=63, min_length=1, regex='^[0-9A-Za-z_-]+$')
    ]


class DetectorVersionMaxResults(BaseModel):
    __root__: Annotated[int, Field(ge=1000.0, le=2500.0)]


class ModelsMaxPageSize(BaseModel):
    __root__: Annotated[int, Field(ge=1.0, le=10.0)]


class Detector(BaseModel):
    """
    The detector.
    """

    detectorId: Optional[Identifier] = None
    description: Optional[Description] = None
    eventTypeName: Optional[Identifier] = None
    lastUpdatedTime: Optional[Time] = None
    createdTime: Optional[Time] = None
    arn: Optional[FraudDetectorArn] = None


class DetectorList(BaseModel):
    __root__: List[Detector]


class DetectorVersionSummary(BaseModel):
    """
    The summary of the detector version.
    """

    detectorVersionId: Optional[NonEmptyString] = None
    status: Optional[DetectorVersionStatus] = None
    description: Optional[Description] = None
    lastUpdatedTime: Optional[Time] = None


class DetectorsMaxResults(BaseModel):
    __root__: Annotated[int, Field(ge=5.0, le=10.0)]


class Entity(BaseModel):
    """
    The entity details.
    """

    entityType: String
    entityId: Identifier


class EntityType1(BaseModel):
    """
    The entity type details.
    """

    name: Optional[String] = None
    description: Optional[Description] = None
    lastUpdatedTime: Optional[Time] = None
    createdTime: Optional[Time] = None
    arn: Optional[FraudDetectorArn] = None


class EventType(BaseModel):
    """
    The event type details.
    """

    name: Optional[String] = None
    description: Optional[Description] = None
    eventVariables: Optional[ListOfStrings] = None
    labels: Optional[ListOfStrings] = None
    entityTypes: Optional[NonEmptyListOfStrings] = None
    lastUpdatedTime: Optional[Time] = None
    createdTime: Optional[Time] = None
    arn: Optional[FraudDetectorArn] = None


class VariableValue(BaseModel):
    __root__: Annotated[SecretStr, Field(max_length=1024, min_length=1)]


class EventVariableMap(BaseModel):
    pass

    class Config:
        extra = Extra.allow


class ModelSource(Enum):
    SAGEMAKER = 'SAGEMAKER'


class ModelEndpointStatus(Enum):
    ASSOCIATED = 'ASSOCIATED'
    DISSOCIATED = 'DISSOCIATED'


class ExternalModelEndpointDataBlobMap(BaseModel):
    pass

    class Config:
        extra = Extra.allow


class ExternalModelSummary(BaseModel):
    """
    The Amazon SageMaker model.
    """

    modelEndpoint: Optional[String] = None
    modelSource: Optional[ModelSource] = None


class ExternalModelPredictionMap(CsvIndexToVariableMap):
    pass


class ExternalModelOutputs1(BaseModel):
    """
    The fraud prediction scores from Amazon SageMaker model.
    """

    externalModel: Optional[ExternalModelSummary] = None
    outputs: Optional[ExternalModelPredictionMap] = None


class ExternalModelsMaxResults(DetectorsMaxResults):
    pass


class FieldValidationMessage(BaseModel):
    """
    The message details.
    """

    fieldName: Optional[String] = None
    identifier: Optional[String] = None
    title: Optional[String] = None
    content: Optional[String] = None
    type: Optional[String] = None


class FileValidationMessage(BaseModel):
    """
    The message details.
    """

    title: Optional[String] = None
    content: Optional[String] = None
    type: Optional[String] = None


class BatchPredictionsMaxPageSize(BaseModel):
    __root__: Annotated[int, Field(ge=1.0, le=50.0)]


class EntityTypesMaxResults(DetectorsMaxResults):
    pass


class EntityTypeList(BaseModel):
    __root__: List[EntityType1]


class ListOfEntities(BaseModel):
    __root__: List[Entity]


class UtcTimestampISO8601(BaseModel):
    __root__: Annotated[str, Field(max_length=30, min_length=10)]


class ListOfExternalModelOutputs(BaseModel):
    __root__: List[ExternalModelOutputs1]


class EventTypesMaxResults(DetectorsMaxResults):
    pass


class EventTypeList(BaseModel):
    __root__: List[EventType]


class LabelsMaxResults(BaseModel):
    __root__: Annotated[int, Field(ge=10.0, le=50.0)]


class OutcomesMaxResults(BaseModel):
    __root__: Annotated[int, Field(ge=50.0, le=100.0)]


class RulesMaxResults(OutcomesMaxResults):
    pass


class VariablesMaxResults(OutcomesMaxResults):
    pass


class JsonKeyToVariableMap(CsvIndexToVariableMap):
    pass


class KmsEncryptionKeyArn(BaseModel):
    __root__: Annotated[
        str,
        Field(
            max_length=90,
            min_length=7,
            regex='^DEFAULT|arn:[a-zA-Z0-9-]+:kms:[a-zA-Z0-9-]+:\\d{12}:key\\/\\w{8}-\\w{4}-\\w{4}-\\w{4}-\\w{12}$',
        ),
    ]


class Label(EntityType1):
    """
    The label details.
    """

    pass


class LabelMapper(BaseModel):
    pass

    class Config:
        extra = Extra.allow


class LabelSchema(BaseModel):
    """
    The label schema.
    """

    labelMapper: LabelMapper


class ModelVersion(BaseModel):
    """
    The model version.
    """

    modelId: ModelIdentifier
    modelType: ModelTypeEnum
    modelVersionNumber: NonEmptyString
    arn: Optional[FraudDetectorArn] = None


class RuleResult(BaseModel):
    """
    The rule results.
    """

    ruleId: Optional[String] = None
    outcomes: Optional[ListOfStrings] = None


class TagsMaxResults(BaseModel):
    __root__: Annotated[int, Field(ge=50.0, le=50.0)]


class Float(BaseModel):
    __root__: float


class MetricDataPoint(BaseModel):
    """
    Model performance metrics data points.
    """

    fpr: Optional[Float] = None
    precision: Optional[Float] = None
    tpr: Optional[Float] = None
    threshold: Optional[Float] = None


class Model(BaseModel):
    """
    The model.
    """

    modelId: Optional[ModelIdentifier] = None
    modelType: Optional[ModelTypeEnum] = None
    description: Optional[Description] = None
    eventTypeName: Optional[String] = None
    createdTime: Optional[Time] = None
    lastUpdatedTime: Optional[Time] = None
    arn: Optional[FraudDetectorArn] = None


class Blob(String):
    pass


class ContentType(BaseModel):
    __root__: Annotated[str, Field(max_length=1024, min_length=1)]


class ModelInputDataFormat(Enum):
    TEXT_CSV = 'TEXT_CSV'
    APPLICATION_JSON = 'APPLICATION_JSON'


class UseEventVariables(BaseModel):
    __root__: bool


class ModelOutputDataFormat(Enum):
    TEXT_CSV = 'TEXT_CSV'
    APPLICATION_JSONLINES = 'APPLICATION_JSONLINES'


class ModelPredictionMap(BaseModel):
    pass

    class Config:
        extra = Extra.allow


class ModelVersionStatus(Enum):
    ACTIVE = 'ACTIVE'
    INACTIVE = 'INACTIVE'
    TRAINING_CANCELLED = 'TRAINING_CANCELLED'


class Outcome(BaseModel):
    """
    The outcome.
    """

    name: Optional[Identifier] = None
    description: Optional[Description] = None
    lastUpdatedTime: Optional[Time] = None
    createdTime: Optional[Time] = None
    arn: Optional[FraudDetectorArn] = None


class RuleDetail(BaseModel):
    """
    The details of the rule.
    """

    ruleId: Optional[Identifier] = None
    description: Optional[Description] = None
    detectorId: Optional[Identifier] = None
    ruleVersion: Optional[WholeNumberVersionString] = None
    expression: Optional[RuleExpression] = None
    language: Optional[Language] = None
    outcomes: Optional[NonEmptyListOfStrings] = None
    lastUpdatedTime: Optional[Time] = None
    createdTime: Optional[Time] = None
    arn: Optional[FraudDetectorArn] = None


class TagKey(BaseModel):
    __root__: Annotated[
        str,
        Field(
            max_length=128, min_length=1, regex='^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-@]*)$'
        ),
    ]


class TagValue(BaseModel):
    __root__: Annotated[str, Field(max_length=256, min_length=0)]


class Tag(BaseModel):
    """
    A key and value pair.
    """

    key: TagKey
    value: TagValue


class MetricDataPointsList(BaseModel):
    __root__: List[MetricDataPoint]


class TrainingMetrics(BaseModel):
    """
    The training metric details.
    """

    auc: Optional[Float] = None
    metricDataPoints: Optional[MetricDataPointsList] = None


class TagKeyList(BaseModel):
    __root__: Annotated[List[TagKey], Field(max_items=50, min_items=0)]


class Variable(BaseModel):
    """
    The variable.
    """

    name: Optional[String] = None
    dataType: Optional[DataType] = None
    dataSource: Optional[DataSource] = None
    defaultValue: Optional[String] = None
    description: Optional[String] = None
    variableType: Optional[String] = None
    lastUpdatedTime: Optional[Time] = None
    createdTime: Optional[Time] = None
    arn: Optional[FraudDetectorArn] = None


class VariableEntry(BaseModel):
    """
    A variable in the list of variables for the batch create variable request.
    """

    name: Optional[String] = None
    dataType: Optional[String] = None
    dataSource: Optional[String] = None
    defaultValue: Optional[String] = None
    description: Optional[String] = None
    variableType: Optional[String] = None


class VariableName1(BaseModel):
    __root__: Annotated[str, Field(max_length=64, min_length=1)]


class BatchCreateVariableResult(BaseModel):
    errors: Optional[BatchCreateVariableErrorList] = None


class BatchGetVariableRequest(BaseModel):
    names: NameList


class CancelBatchPredictionJobRequest(BaseModel):
    jobId: Identifier


class CreateDetectorVersionResult(BaseModel):
    detectorId: Optional[Identifier] = None
    detectorVersionId: Optional[NonEmptyString] = None
    status: Optional[DetectorVersionStatus] = None


class CreateModelVersionResult(BaseModel):
    modelId: Optional[ModelIdentifier] = None
    modelType: Optional[ModelTypeEnum] = None
    modelVersionNumber: Optional[NonEmptyString] = None
    status: Optional[String] = None


class CreateRuleResult(BaseModel):
    rule: Optional[Rule] = None


class DeleteBatchPredictionJobRequest(BaseModel):
    jobId: Identifier


class DeleteDetectorRequest(BaseModel):
    detectorId: Identifier


class DeleteDetectorVersionRequest(BaseModel):
    detectorId: Identifier
    detectorVersionId: WholeNumberVersionString


class DeleteEntityTypeRequest(BaseModel):
    name: Identifier


class DeleteEventRequest(BaseModel):
    eventId: Identifier
    eventTypeName: Identifier


class DeleteEventTypeRequest(BaseModel):
    name: Identifier


class DeleteExternalModelRequest(BaseModel):
    modelEndpoint: SageMakerEndpointIdentifier


class DeleteLabelRequest(BaseModel):
    name: Identifier


class DeleteModelRequest(BaseModel):
    modelId: ModelIdentifier
    modelType: ModelTypeEnum


class DeleteModelVersionRequest(BaseModel):
    modelId: ModelIdentifier
    modelType: ModelTypeEnum
    modelVersionNumber: FloatVersionString


class DeleteOutcomeRequest(BaseModel):
    name: Identifier


class DeleteRuleRequest(BaseModel):
    rule: Rule


class DeleteVariableRequest(BaseModel):
    name: String


class DescribeDetectorRequest(BaseModel):
    detectorId: Identifier
    nextToken: Optional[String] = None
    maxResults: Optional[DetectorVersionMaxResults] = None


class DescribeModelVersionsRequest(BaseModel):
    modelId: Optional[ModelIdentifier] = None
    modelVersionNumber: Optional[FloatVersionString] = None
    modelType: Optional[ModelTypeEnum] = None
    nextToken: Optional[String] = None
    maxResults: Optional[ModelsMaxPageSize] = None


class GetBatchPredictionJobsResult(BaseModel):
    batchPredictions: Optional[BatchPredictionList] = None
    nextToken: Optional[String] = None


class GetBatchPredictionJobsRequest(BaseModel):
    jobId: Optional[Identifier] = None
    maxResults: Optional[BatchPredictionsMaxPageSize] = None
    nextToken: Optional[String] = None


class GetDetectorVersionRequest(BaseModel):
    detectorId: Identifier
    detectorVersionId: WholeNumberVersionString


class GetDetectorsResult(BaseModel):
    detectors: Optional[DetectorList] = None
    nextToken: Optional[String] = None


class GetDetectorsRequest(BaseModel):
    detectorId: Optional[Identifier] = None
    nextToken: Optional[String] = None
    maxResults: Optional[DetectorsMaxResults] = None


class GetEntityTypesResult(BaseModel):
    entityTypes: Optional[EntityTypeList] = None
    nextToken: Optional[String] = None


class GetEntityTypesRequest(BaseModel):
    name: Optional[Identifier] = None
    nextToken: Optional[String] = None
    maxResults: Optional[EntityTypesMaxResults] = None


class GetEventPredictionRequest(BaseModel):
    detectorId: String
    detectorVersionId: Optional[WholeNumberVersionString] = None
    eventId: String
    eventTypeName: String
    entities: ListOfEntities
    eventTimestamp: UtcTimestampISO8601
    eventVariables: EventVariableMap
    externalModelEndpointDataBlobs: Optional[ExternalModelEndpointDataBlobMap] = None


class GetEventTypesResult(BaseModel):
    eventTypes: Optional[EventTypeList] = None
    nextToken: Optional[String] = None


class GetEventTypesRequest(BaseModel):
    name: Optional[Identifier] = None
    nextToken: Optional[String] = None
    maxResults: Optional[EventTypesMaxResults] = None


class GetExternalModelsRequest(BaseModel):
    modelEndpoint: Optional[String] = None
    nextToken: Optional[String] = None
    maxResults: Optional[ExternalModelsMaxResults] = None


class GetLabelsRequest(BaseModel):
    name: Optional[Identifier] = None
    nextToken: Optional[String] = None
    maxResults: Optional[LabelsMaxResults] = None


class GetModelVersionRequest(BaseModel):
    modelId: ModelIdentifier
    modelType: ModelTypeEnum
    modelVersionNumber: FloatVersionString


class GetModelsRequest(BaseModel):
    modelId: Optional[ModelIdentifier] = None
    modelType: Optional[ModelTypeEnum] = None
    nextToken: Optional[String] = None
    maxResults: Optional[ModelsMaxPageSize] = None


class GetOutcomesRequest(BaseModel):
    name: Optional[Identifier] = None
    nextToken: Optional[String] = None
    maxResults: Optional[OutcomesMaxResults] = None


class GetRulesRequest(BaseModel):
    ruleId: Optional[Identifier] = None
    detectorId: Identifier
    ruleVersion: Optional[WholeNumberVersionString] = None
    nextToken: Optional[String] = None
    maxResults: Optional[RulesMaxResults] = None


class GetVariablesRequest(BaseModel):
    name: Optional[String] = None
    nextToken: Optional[String] = None
    maxResults: Optional[VariablesMaxResults] = None


class ListTagsForResourceRequest(BaseModel):
    resourceARN: FraudDetectorArn
    nextToken: Optional[String] = None
    maxResults: Optional[TagsMaxResults] = None


class PutKMSEncryptionKeyRequest(BaseModel):
    kmsEncryptionKeyArn: KmsEncryptionKeyArn


class UntagResourceRequest(BaseModel):
    resourceARN: FraudDetectorArn
    tagKeys: TagKeyList


class UpdateDetectorVersionMetadataRequest(BaseModel):
    detectorId: Identifier
    detectorVersionId: WholeNumberVersionString
    description: Description


class UpdateDetectorVersionStatusRequest(BaseModel):
    detectorId: Identifier
    detectorVersionId: WholeNumberVersionString
    status: DetectorVersionStatus


class UpdateModelRequest(BaseModel):
    modelId: ModelIdentifier
    modelType: ModelTypeEnum
    description: Optional[Description] = None


class UpdateModelVersionResult(BaseModel):
    modelId: Optional[ModelIdentifier] = None
    modelType: Optional[ModelTypeEnum] = None
    modelVersionNumber: Optional[FloatVersionString] = None
    status: Optional[String] = None


class UpdateModelVersionStatusRequest(BaseModel):
    modelId: ModelIdentifier
    modelType: ModelTypeEnum
    modelVersionNumber: FloatVersionString
    status: ModelVersionStatus


class UpdateRuleMetadataRequest(BaseModel):
    rule: Rule
    description: Description


class UpdateRuleVersionResult(CreateRuleResult):
    pass


class UpdateVariableRequest(BaseModel):
    name: String
    defaultValue: Optional[String] = None
    description: Optional[String] = None
    variableType: Optional[String] = None


class VariableEntryList(BaseModel):
    __root__: Annotated[List[VariableEntry], Field(max_items=25, min_items=1)]


class TagList(BaseModel):
    __root__: Annotated[List[Tag], Field(max_items=200, min_items=0)]


class VariableList(BaseModel):
    __root__: List[Variable]


class RuleList(BaseModel):
    __root__: List[Rule]


class ListOfModelVersions(BaseModel):
    __root__: List[ModelVersion]


class TrainingDataSchema(BaseModel):
    """
    The training data schema.
    """

    modelVariables: ListOfStrings
    labelSchema: LabelSchema


class FileValidationMessageList(BaseModel):
    __root__: List[FileValidationMessage]


class FieldValidationMessageList(BaseModel):
    __root__: List[FieldValidationMessage]


class DataValidationMetrics(BaseModel):
    """
    The model training validation messages.
    """

    fileLevelMessages: Optional[FileValidationMessageList] = None
    fieldLevelMessages: Optional[FieldValidationMessageList] = None


class DetectorVersionSummaryList(BaseModel):
    __root__: List[DetectorVersionSummary]


class ModelInputConfiguration(BaseModel):
    """
    The Amazon SageMaker model input configuration.
    """

    eventTypeName: Optional[Identifier] = None
    format: Optional[ModelInputDataFormat] = None
    useEventVariables: UseEventVariables
    jsonInputTemplate: Optional[String] = None
    csvInputTemplate: Optional[String] = None


class ModelOutputConfiguration(BaseModel):
    """
    Provides the Amazon Sagemaker model output configuration.
    """

    format: ModelOutputDataFormat
    jsonKeyToVariableMap: Optional[JsonKeyToVariableMap] = None
    csvIndexToVariableMap: Optional[CsvIndexToVariableMap] = None


class ExternalModel(BaseModel):
    """
    The Amazon SageMaker model.
    """

    modelEndpoint: Optional[String] = None
    modelSource: Optional[ModelSource] = None
    invokeModelEndpointRoleArn: Optional[String] = None
    inputConfiguration: Optional[ModelInputConfiguration] = None
    outputConfiguration: Optional[ModelOutputConfiguration] = None
    modelEndpointStatus: Optional[ModelEndpointStatus] = None
    lastUpdatedTime: Optional[Time] = None
    createdTime: Optional[Time] = None
    arn: Optional[FraudDetectorArn] = None


class ModelEndpointDataBlob(BaseModel):
    """
    A pre-formed Amazon SageMaker model input you can include if your detector version includes an imported Amazon SageMaker model endpoint with pass-through input configuration.
    """

    byteBuffer: Optional[Blob] = None
    contentType: Optional[ContentType] = None


class ExternalModelList(BaseModel):
    __root__: List[ExternalModel]


class ListOfRuleResults(BaseModel):
    __root__: List[RuleResult]


class KMSKey(BaseModel):
    """
    The KMS key details.
    """

    kmsEncryptionKeyArn: Optional[KmsEncryptionKeyArn] = None


class LabelList(BaseModel):
    __root__: List[Label]


class ModelList(BaseModel):
    __root__: List[Model]


class OutcomeList(BaseModel):
    __root__: List[Outcome]


class RuleDetailList(BaseModel):
    __root__: List[RuleDetail]


class LogOddsMetric(BaseModel):
    """
    The log odds metric details.
    """

    variableName: String
    variableType: String
    variableImportance: Float


class ListOfLogOddsMetrics(BaseModel):
    __root__: List[LogOddsMetric]


class ModelScores(BaseModel):
    """
    The fraud prediction scores.
    """

    modelVersion: Optional[ModelVersion] = None
    scores: Optional[ModelPredictionMap] = None


class VariableImportanceMetrics(BaseModel):
    """
    The variable importance metrics details.
    """

    logOddsMetrics: Optional[ListOfLogOddsMetrics] = None


class BatchCreateVariableRequest(BaseModel):
    variableEntries: VariableEntryList
    tags: Optional[TagList] = None


class BatchGetVariableResult(BaseModel):
    variables: Optional[VariableList] = None
    errors: Optional[BatchGetVariableErrorList] = None


class CreateBatchPredictionJobRequest(BaseModel):
    jobId: Identifier
    inputPath: S3BucketLocation
    outputPath: S3BucketLocation
    eventTypeName: Identifier
    detectorName: Identifier
    detectorVersion: Optional[WholeNumberVersionString] = None
    iamRoleArn: IamRoleArn
    tags: Optional[TagList] = None


class CreateDetectorVersionRequest(BaseModel):
    detectorId: Identifier
    description: Optional[Description] = None
    externalModelEndpoints: Optional[ListOfStrings] = None
    rules: RuleList
    modelVersions: Optional[ListOfModelVersions] = None
    ruleExecutionMode: Optional[RuleExecutionMode] = None
    tags: Optional[TagList] = None


class CreateModelRequest(BaseModel):
    modelId: ModelIdentifier
    modelType: ModelTypeEnum
    description: Optional[Description] = None
    eventTypeName: String
    tags: Optional[TagList] = None


class CreateModelVersionRequest(BaseModel):
    modelId: ModelIdentifier
    modelType: ModelTypeEnum
    trainingDataSource: TrainingDataSourceEnum
    trainingDataSchema: TrainingDataSchema
    externalEventsDetail: Optional[ExternalEventsDetail] = None
    tags: Optional[TagList] = None


class CreateRuleRequest(BaseModel):
    ruleId: Identifier
    detectorId: Identifier
    description: Optional[Description] = None
    expression: RuleExpression
    language: Language
    outcomes: NonEmptyListOfStrings
    tags: Optional[TagList] = None


class CreateVariableRequest(BaseModel):
    name: String
    dataType: DataType
    dataSource: DataSource
    defaultValue: String
    description: Optional[String] = None
    variableType: Optional[String] = None
    tags: Optional[TagList] = None


class DescribeDetectorResult(BaseModel):
    detectorId: Optional[Identifier] = None
    detectorVersionSummaries: Optional[DetectorVersionSummaryList] = None
    nextToken: Optional[String] = None
    arn: Optional[FraudDetectorArn] = None


class GetDetectorVersionResult(BaseModel):
    detectorId: Optional[Identifier] = None
    detectorVersionId: Optional[WholeNumberVersionString] = None
    description: Optional[Description] = None
    externalModelEndpoints: Optional[ListOfStrings] = None
    modelVersions: Optional[ListOfModelVersions] = None
    rules: Optional[RuleList] = None
    status: Optional[DetectorVersionStatus] = None
    lastUpdatedTime: Optional[Time] = None
    createdTime: Optional[Time] = None
    ruleExecutionMode: Optional[RuleExecutionMode] = None
    arn: Optional[FraudDetectorArn] = None


class GetExternalModelsResult(BaseModel):
    externalModels: Optional[ExternalModelList] = None
    nextToken: Optional[String] = None


class GetKMSEncryptionKeyResult(BaseModel):
    kmsKey: Optional[KMSKey] = None


class GetLabelsResult(BaseModel):
    labels: Optional[LabelList] = None
    nextToken: Optional[String] = None


class GetModelVersionResult(BaseModel):
    modelId: Optional[ModelIdentifier] = None
    modelType: Optional[ModelTypeEnum] = None
    modelVersionNumber: Optional[FloatVersionString] = None
    trainingDataSource: Optional[TrainingDataSourceEnum] = None
    trainingDataSchema: Optional[TrainingDataSchema] = None
    externalEventsDetail: Optional[ExternalEventsDetail] = None
    status: Optional[String] = None
    arn: Optional[FraudDetectorArn] = None


class GetModelsResult(BaseModel):
    nextToken: Optional[String] = None
    models: Optional[ModelList] = None


class GetOutcomesResult(BaseModel):
    outcomes: Optional[OutcomeList] = None
    nextToken: Optional[String] = None


class GetRulesResult(BaseModel):
    ruleDetails: Optional[RuleDetailList] = None
    nextToken: Optional[String] = None


class GetVariablesResult(BaseModel):
    variables: Optional[VariableList] = None
    nextToken: Optional[String] = None


class ListTagsForResourceResult(BaseModel):
    tags: Optional[TagList] = None
    nextToken: Optional[String] = None


class PutDetectorRequest(BaseModel):
    detectorId: Identifier
    description: Optional[Description] = None
    eventTypeName: Identifier
    tags: Optional[TagList] = None


class PutEntityTypeRequest(BaseModel):
    name: Identifier
    description: Optional[Description] = None
    tags: Optional[TagList] = None


class PutEventTypeRequest(BaseModel):
    name: Identifier
    description: Optional[Description] = None
    eventVariables: NonEmptyListOfStrings
    labels: Optional[ListOfStrings] = None
    entityTypes: NonEmptyListOfStrings
    tags: Optional[TagList] = None


class PutExternalModelRequest(BaseModel):
    modelEndpoint: SageMakerEndpointIdentifier
    modelSource: ModelSource
    invokeModelEndpointRoleArn: String
    inputConfiguration: ModelInputConfiguration
    outputConfiguration: ModelOutputConfiguration
    modelEndpointStatus: ModelEndpointStatus
    tags: Optional[TagList] = None


class PutLabelRequest(BaseModel):
    name: Identifier
    description: Optional[Description] = None
    tags: Optional[TagList] = None


class PutOutcomeRequest(BaseModel):
    name: Identifier
    description: Optional[Description] = None
    tags: Optional[TagList] = None


class TagResourceRequest(BaseModel):
    resourceARN: FraudDetectorArn
    tags: TagList


class UpdateDetectorVersionRequest(BaseModel):
    detectorId: Identifier
    detectorVersionId: WholeNumberVersionString
    externalModelEndpoints: ListOfStrings
    rules: RuleList
    description: Optional[Description] = None
    modelVersions: Optional[ListOfModelVersions] = None
    ruleExecutionMode: Optional[RuleExecutionMode] = None


class UpdateModelVersionRequest(BaseModel):
    modelId: ModelIdentifier
    modelType: ModelTypeEnum
    majorVersionNumber: WholeNumberVersionString
    externalEventsDetail: Optional[ExternalEventsDetail] = None
    tags: Optional[TagList] = None


class UpdateRuleVersionRequest(BaseModel):
    rule: Rule
    description: Optional[Description] = None
    expression: RuleExpression
    language: Language
    outcomes: NonEmptyListOfStrings
    tags: Optional[TagList] = None


class ListOfModelScores(BaseModel):
    __root__: List[ModelScores]


class TrainingResult(BaseModel):
    """
    The training result details.
    """

    dataValidationMetrics: Optional[DataValidationMetrics] = None
    trainingMetrics: Optional[TrainingMetrics] = None
    variableImportanceMetrics: Optional[VariableImportanceMetrics] = None


class ModelVersionDetail(BaseModel):
    """
    The details of the model version.
    """

    modelId: Optional[ModelIdentifier] = None
    modelType: Optional[ModelTypeEnum] = None
    modelVersionNumber: Optional[FloatVersionString] = None
    status: Optional[String] = None
    trainingDataSource: Optional[TrainingDataSourceEnum] = None
    trainingDataSchema: Optional[TrainingDataSchema] = None
    externalEventsDetail: Optional[ExternalEventsDetail] = None
    trainingResult: Optional[TrainingResult] = None
    lastUpdatedTime: Optional[Time] = None
    createdTime: Optional[Time] = None
    arn: Optional[FraudDetectorArn] = None


class GetEventPredictionResult(BaseModel):
    modelScores: Optional[ListOfModelScores] = None
    ruleResults: Optional[ListOfRuleResults] = None
    externalModelOutputs: Optional[ListOfExternalModelOutputs] = None


class ModelVersionDetailList(BaseModel):
    __root__: List[ModelVersionDetail]


class DescribeModelVersionsResult(BaseModel):
    modelVersionDetails: Optional[ModelVersionDetailList] = None
    nextToken: Optional[String] = None
