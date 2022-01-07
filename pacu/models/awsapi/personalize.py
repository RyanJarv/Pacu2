# generated by datamodel-codegen:
#   filename:  openapi.yaml
#   timestamp: 2021-12-31T02:53:46+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Annotated, Any, List, Optional

from pydantic import BaseModel, Extra, Field, SecretStr


class InvalidInputException(BaseModel):
    __root__: Any


class ResourceAlreadyExistsException(InvalidInputException):
    pass


class LimitExceededException(InvalidInputException):
    pass


class ResourceNotFoundException(InvalidInputException):
    pass


class ResourceInUseException(InvalidInputException):
    pass


class InvalidNextTokenException(InvalidInputException):
    pass


class AccountId(BaseModel):
    __root__: Annotated[str, Field(max_length=256)]


class Name(BaseModel):
    __root__: Annotated[
        str, Field(max_length=63, min_length=1, regex='^[a-zA-Z0-9][a-zA-Z0-9\\-_]*')
    ]


class Arn(BaseModel):
    __root__: Annotated[
        str, Field(max_length=256, regex='arn:([a-z\\d-]+):personalize:.*:.*:.+')
    ]


class HyperParameters(BaseModel):
    pass

    class Config:
        extra = Extra.allow


class ResourceConfig(HyperParameters):
    pass


class TrainingInputMode(AccountId):
    pass


class Date(BaseModel):
    __root__: datetime


class DockerURI(AccountId):
    pass


class ArnList(BaseModel):
    __root__: Annotated[List[Arn], Field(max_items=100)]


class MetricName(AccountId):
    pass


class AutoMLConfig(BaseModel):
    """
    When the solution performs AutoML (<code>performAutoML</code> is true in <a>CreateSolution</a>), Amazon Personalize determines which recipe, from the specified list, optimizes the given metric. Amazon Personalize then uses that recipe for the solution.
    """

    metricName: Optional[MetricName] = None
    recipeList: Optional[ArnList] = None


class AutoMLResult(BaseModel):
    """
    When the solution performs AutoML (<code>performAutoML</code> is true in <a>CreateSolution</a>), specifies the recipe that best optimized the specified metric.
    """

    bestRecipeArn: Optional[Arn] = None


class AvroSchema(BaseModel):
    __root__: Annotated[str, Field(max_length=10000)]


class FailureReason(BaseModel):
    __root__: str


class NumBatchResults(BaseModel):
    __root__: int


class BatchInferenceJobConfig(BaseModel):
    """
    The configuration details of a batch inference job.
    """

    itemExplorationConfig: Optional[HyperParameters] = None


class RoleArn(BaseModel):
    __root__: Annotated[
        str,
        Field(
            max_length=256,
            regex='arn:([a-z\\d-]+):iam::\\d{12}:role/?[a-zA-Z_0-9+=,.@\\-_/]+',
        ),
    ]


class Status(AccountId):
    pass


class BatchInferenceJobSummary(BaseModel):
    """
    A truncated version of the <a>BatchInferenceJob</a> datatype. The <a>ListBatchInferenceJobs</a> operation returns a list of batch inference job summaries.
    """

    batchInferenceJobArn: Optional[Arn] = None
    jobName: Optional[Name] = None
    status: Optional[Status] = None
    creationDateTime: Optional[Date] = None
    lastUpdatedDateTime: Optional[Date] = None
    failureReason: Optional[FailureReason] = None
    solutionVersionArn: Optional[Arn] = None


class BatchInferenceJobs(BaseModel):
    __root__: Annotated[List[BatchInferenceJobSummary], Field(max_items=100)]


class Boolean(BaseModel):
    __root__: bool


class TransactionsPerSecond(BaseModel):
    __root__: Annotated[int, Field(ge=1.0)]


class CampaignConfig(BatchInferenceJobConfig):
    """
    The configuration details of a campaign.
    """

    pass


class CampaignUpdateSummary(BaseModel):
    """
    Provides a summary of the properties of a campaign update. For a complete listing, call the <a>DescribeCampaign</a> API.
    """

    solutionVersionArn: Optional[Arn] = None
    minProvisionedTPS: Optional[TransactionsPerSecond] = None
    campaignConfig: Optional[CampaignConfig] = None
    status: Optional[Status] = None
    failureReason: Optional[FailureReason] = None
    creationDateTime: Optional[Date] = None
    lastUpdatedDateTime: Optional[Date] = None


class Campaign(BaseModel):
    """
    Describes a deployed solution version, otherwise known as a campaign. For more information on campaigns, see <a>CreateCampaign</a>.
    """

    name: Optional[Name] = None
    campaignArn: Optional[Arn] = None
    solutionVersionArn: Optional[Arn] = None
    minProvisionedTPS: Optional[TransactionsPerSecond] = None
    campaignConfig: Optional[CampaignConfig] = None
    status: Optional[Status] = None
    failureReason: Optional[FailureReason] = None
    creationDateTime: Optional[Date] = None
    lastUpdatedDateTime: Optional[Date] = None
    latestCampaignUpdate: Optional[CampaignUpdateSummary] = None


class CampaignSummary(BaseModel):
    """
    Provides a summary of the properties of a campaign. For a complete listing, call the <a>DescribeCampaign</a> API.
    """

    name: Optional[Name] = None
    campaignArn: Optional[Arn] = None
    status: Optional[Status] = None
    creationDateTime: Optional[Date] = None
    lastUpdatedDateTime: Optional[Date] = None
    failureReason: Optional[FailureReason] = None


class Campaigns(BaseModel):
    __root__: Annotated[List[CampaignSummary], Field(max_items=100)]


class ParameterName(AccountId):
    pass


class CategoricalValue(BaseModel):
    __root__: Annotated[str, Field(max_length=1000)]


class ContinuousMinValue(BaseModel):
    __root__: Annotated[float, Field(ge=-1000000.0)]


class ContinuousMaxValue(ContinuousMinValue):
    pass


class ContinuousHyperParameterRange(BaseModel):
    """
    Provides the name and range of a continuous hyperparameter.
    """

    name: Optional[ParameterName] = None
    minValue: Optional[ContinuousMinValue] = None
    maxValue: Optional[ContinuousMaxValue] = None


class ContinuousHyperParameterRanges1(BaseModel):
    __root__: Annotated[List[ContinuousHyperParameterRange], Field(max_items=100)]


class IngestionMode(Enum):
    BULK = 'BULK'
    PUT = 'PUT'
    ALL = 'ALL'


class KmsKeyArn(BaseModel):
    __root__: Annotated[str, Field(regex='arn:aws.*:kms:.*:[0-9]{12}:key/.*')]


class DatasetType(AccountId):
    pass


class TrackingId(AccountId):
    pass


class FilterExpression(BaseModel):
    __root__: Annotated[SecretStr, Field(max_length=2500, min_length=1)]


class PerformAutoML(Boolean):
    pass


class EventType(AccountId):
    pass


class TrainingMode(Enum):
    FULL = 'FULL'
    UPDATE = 'UPDATE'


class S3Location(BaseModel):
    __root__: Annotated[str, Field(max_length=256, regex='(s3|http|https)://.+')]


class Dataset(BaseModel):
    """
    Provides metadata for a dataset.
    """

    name: Optional[Name] = None
    datasetArn: Optional[Arn] = None
    datasetGroupArn: Optional[Arn] = None
    datasetType: Optional[DatasetType] = None
    schemaArn: Optional[Arn] = None
    status: Optional[Status] = None
    creationDateTime: Optional[Date] = None
    lastUpdatedDateTime: Optional[Date] = None


class DatasetExportJobSummary(BaseModel):
    """
    Provides a summary of the properties of a dataset export job. For a complete listing, call the <a>DescribeDatasetExportJob</a> API.
    """

    datasetExportJobArn: Optional[Arn] = None
    jobName: Optional[Name] = None
    status: Optional[Status] = None
    creationDateTime: Optional[Date] = None
    lastUpdatedDateTime: Optional[Date] = None
    failureReason: Optional[FailureReason] = None


class DatasetExportJobs(BaseModel):
    __root__: Annotated[List[DatasetExportJobSummary], Field(max_items=100)]


class DatasetGroup(BaseModel):
    """
    <p>A dataset group is a collection of related datasets (Interactions, User, and Item). You create a dataset group by calling <a>CreateDatasetGroup</a>. You then create a dataset and add it to a dataset group by calling <a>CreateDataset</a>. The dataset group is used to create and train a solution by calling <a>CreateSolution</a>. A dataset group can contain only one of each type of dataset.</p> <p>You can specify an Key Management Service (KMS) key to encrypt the datasets in the group.</p>
    """

    name: Optional[Name] = None
    datasetGroupArn: Optional[Arn] = None
    status: Optional[Status] = None
    roleArn: Optional[RoleArn] = None
    kmsKeyArn: Optional[KmsKeyArn] = None
    creationDateTime: Optional[Date] = None
    lastUpdatedDateTime: Optional[Date] = None
    failureReason: Optional[FailureReason] = None


class DatasetGroupSummary(BaseModel):
    """
    Provides a summary of the properties of a dataset group. For a complete listing, call the <a>DescribeDatasetGroup</a> API.
    """

    name: Optional[Name] = None
    datasetGroupArn: Optional[Arn] = None
    status: Optional[Status] = None
    creationDateTime: Optional[Date] = None
    lastUpdatedDateTime: Optional[Date] = None
    failureReason: Optional[FailureReason] = None


class DatasetGroups(BaseModel):
    __root__: Annotated[List[DatasetGroupSummary], Field(max_items=100)]


class DatasetImportJobSummary(BaseModel):
    """
    Provides a summary of the properties of a dataset import job. For a complete listing, call the <a>DescribeDatasetImportJob</a> API.
    """

    datasetImportJobArn: Optional[Arn] = None
    jobName: Optional[Name] = None
    status: Optional[Status] = None
    creationDateTime: Optional[Date] = None
    lastUpdatedDateTime: Optional[Date] = None
    failureReason: Optional[FailureReason] = None


class DatasetImportJobs(BaseModel):
    __root__: Annotated[List[DatasetImportJobSummary], Field(max_items=100)]


class DatasetSchema(BaseModel):
    """
    Describes the schema for a dataset. For more information on schemas, see <a>CreateSchema</a>.
    """

    name: Optional[Name] = None
    schemaArn: Optional[Arn] = None
    schema_: Annotated[Optional[AvroSchema], Field(alias='schema')] = None
    creationDateTime: Optional[Date] = None
    lastUpdatedDateTime: Optional[Date] = None


class DatasetSchemaSummary(BaseModel):
    """
    Provides a summary of the properties of a dataset schema. For a complete listing, call the <a>DescribeSchema</a> API.
    """

    name: Optional[Name] = None
    schemaArn: Optional[Arn] = None
    creationDateTime: Optional[Date] = None
    lastUpdatedDateTime: Optional[Date] = None


class DatasetSummary(BaseModel):
    """
    Provides a summary of the properties of a dataset. For a complete listing, call the <a>DescribeDataset</a> API.
    """

    name: Optional[Name] = None
    datasetArn: Optional[Arn] = None
    datasetType: Optional[DatasetType] = None
    status: Optional[Status] = None
    creationDateTime: Optional[Date] = None
    lastUpdatedDateTime: Optional[Date] = None


class Datasets(BaseModel):
    __root__: Annotated[List[DatasetSummary], Field(max_items=100)]


class Tunable(Boolean):
    pass


class DefaultContinuousHyperParameterRange(BaseModel):
    """
    Provides the name and default range of a continuous hyperparameter and whether the hyperparameter is tunable. A tunable hyperparameter can have its value determined during hyperparameter optimization (HPO).
    """

    name: Optional[ParameterName] = None
    minValue: Optional[ContinuousMinValue] = None
    maxValue: Optional[ContinuousMaxValue] = None
    isTunable: Optional[Tunable] = None


class DefaultContinuousHyperParameterRanges(BaseModel):
    __root__: Annotated[
        List[DefaultContinuousHyperParameterRange], Field(max_items=100)
    ]


class IntegerMinValue(BaseModel):
    __root__: Annotated[int, Field(ge=-1000000.0)]


class IntegerMaxValue(BaseModel):
    __root__: Annotated[int, Field(le=1000000.0)]


class DefaultIntegerHyperParameterRange(BaseModel):
    """
    Provides the name and default range of a integer-valued hyperparameter and whether the hyperparameter is tunable. A tunable hyperparameter can have its value determined during hyperparameter optimization (HPO).
    """

    name: Optional[ParameterName] = None
    minValue: Optional[IntegerMinValue] = None
    maxValue: Optional[IntegerMaxValue] = None
    isTunable: Optional[Tunable] = None


class EventTracker(BaseModel):
    """
    Provides information about an event tracker.
    """

    name: Optional[Name] = None
    eventTrackerArn: Optional[Arn] = None
    accountId: Optional[AccountId] = None
    trackingId: Optional[TrackingId] = None
    datasetGroupArn: Optional[Arn] = None
    status: Optional[Status] = None
    creationDateTime: Optional[Date] = None
    lastUpdatedDateTime: Optional[Date] = None


class Filter(BaseModel):
    """
    Contains information on a recommendation filter, including its ARN, status, and filter expression.
    """

    name: Optional[Name] = None
    filterArn: Optional[Arn] = None
    creationDateTime: Optional[Date] = None
    lastUpdatedDateTime: Optional[Date] = None
    datasetGroupArn: Optional[Arn] = None
    failureReason: Optional[FailureReason] = None
    filterExpression: Optional[FilterExpression] = None
    status: Optional[Status] = None


class Description(FailureReason):
    pass


class EventTrackerSummary(BaseModel):
    """
    Provides a summary of the properties of an event tracker. For a complete listing, call the <a>DescribeEventTracker</a> API.
    """

    name: Optional[Name] = None
    eventTrackerArn: Optional[Arn] = None
    status: Optional[Status] = None
    creationDateTime: Optional[Date] = None
    lastUpdatedDateTime: Optional[Date] = None


class EventTrackers(BaseModel):
    __root__: Annotated[List[EventTrackerSummary], Field(max_items=100)]


class EventValueThreshold(AccountId):
    pass


class FeaturizationParameters(HyperParameters):
    pass


class ParameterValue(CategoricalValue):
    pass


class FeatureTransformationParameters(HyperParameters):
    pass


class FilterSummary(BaseModel):
    """
    A short summary of a filter's attributes.
    """

    name: Optional[Name] = None
    filterArn: Optional[Arn] = None
    creationDateTime: Optional[Date] = None
    lastUpdatedDateTime: Optional[Date] = None
    datasetGroupArn: Optional[Arn] = None
    failureReason: Optional[FailureReason] = None
    status: Optional[Status] = None


class Filters(BaseModel):
    __root__: Annotated[List[FilterSummary], Field(max_items=100)]


class Metrics(BaseModel):
    pass

    class Config:
        extra = Extra.allow


class HPOObjectiveType(AccountId):
    pass


class MetricRegex(AccountId):
    pass


class HPOResource(AccountId):
    pass


class IntegerHyperParameterRange(BaseModel):
    """
    Provides the name and range of an integer-valued hyperparameter.
    """

    name: Optional[ParameterName] = None
    minValue: Optional[IntegerMinValue] = None
    maxValue: Optional[IntegerMaxValue] = None


class ItemAttribute(BaseModel):
    __root__: Annotated[str, Field(max_length=150, min_length=1)]


class NextToken(BaseModel):
    __root__: Annotated[str, Field(max_length=1300)]


class MaxResults(BaseModel):
    __root__: Annotated[int, Field(ge=1.0, le=100.0)]


class RecipeProvider(Enum):
    SERVICE = 'SERVICE'


class Schemas(BaseModel):
    __root__: Annotated[List[DatasetSchemaSummary], Field(max_items=100)]


class MetricValue(BaseModel):
    __root__: float


class ObjectiveSensitivity(Enum):
    LOW = 'LOW'
    MEDIUM = 'MEDIUM'
    HIGH = 'HIGH'
    OFF = 'OFF'


class OptimizationObjective(BaseModel):
    """
    Describes the additional objective for the solution, such as maximizing streaming minutes or increasing revenue. For more information see <a href="https://docs.aws.amazon.com/personalize/latest/dg/optimizing-solution-for-objective.html">Optimizing a solution</a>.
    """

    itemAttribute: Optional[ItemAttribute] = None
    objectiveSensitivity: Optional[ObjectiveSensitivity] = None


class PerformHPO(Boolean):
    pass


class RecipeType(AccountId):
    pass


class RecipeSummary(BaseModel):
    """
    Provides a summary of the properties of a recipe. For a complete listing, call the <a>DescribeRecipe</a> API.
    """

    name: Optional[Name] = None
    recipeArn: Optional[Arn] = None
    status: Optional[Status] = None
    creationDateTime: Optional[Date] = None
    lastUpdatedDateTime: Optional[Date] = None


class SolutionVersionSummary(BaseModel):
    """
    Provides a summary of the properties of a solution version. For a complete listing, call the <a>DescribeSolutionVersion</a> API.
    """

    solutionVersionArn: Optional[Arn] = None
    status: Optional[Status] = None
    creationDateTime: Optional[Date] = None
    lastUpdatedDateTime: Optional[Date] = None
    failureReason: Optional[FailureReason] = None


class SolutionSummary(BaseModel):
    """
    Provides a summary of the properties of a solution. For a complete listing, call the <a>DescribeSolution</a> API.
    """

    name: Optional[Name] = None
    solutionArn: Optional[Arn] = None
    status: Optional[Status] = None
    creationDateTime: Optional[Date] = None
    lastUpdatedDateTime: Optional[Date] = None


class TrainingHours(BaseModel):
    __root__: Annotated[float, Field(ge=0.0)]


class TunedHPOParams(BaseModel):
    """
    If hyperparameter optimization (HPO) was performed, contains the hyperparameter values of the best performing model.
    """

    algorithmHyperParameters: Optional[HyperParameters] = None


class CreateBatchInferenceJobResponse(BaseModel):
    batchInferenceJobArn: Optional[Arn] = None


class CreateCampaignResponse(BaseModel):
    campaignArn: Optional[Arn] = None


class CreateCampaignRequest(BaseModel):
    name: Name
    solutionVersionArn: Arn
    minProvisionedTPS: Optional[TransactionsPerSecond] = None
    campaignConfig: Optional[CampaignConfig] = None


class CreateDatasetResponse(BaseModel):
    datasetArn: Optional[Arn] = None


class CreateDatasetRequest(BaseModel):
    name: Name
    schemaArn: Arn
    datasetGroupArn: Arn
    datasetType: DatasetType


class CreateDatasetExportJobResponse(BaseModel):
    datasetExportJobArn: Optional[Arn] = None


class CreateDatasetGroupResponse(BaseModel):
    datasetGroupArn: Optional[Arn] = None


class CreateDatasetGroupRequest(BaseModel):
    name: Name
    roleArn: Optional[RoleArn] = None
    kmsKeyArn: Optional[KmsKeyArn] = None


class CreateDatasetImportJobResponse(BaseModel):
    datasetImportJobArn: Optional[Arn] = None


class CreateEventTrackerResponse(BaseModel):
    eventTrackerArn: Optional[Arn] = None
    trackingId: Optional[TrackingId] = None


class CreateEventTrackerRequest(BaseModel):
    name: Name
    datasetGroupArn: Arn


class CreateFilterResponse(BaseModel):
    filterArn: Optional[Arn] = None


class CreateFilterRequest(BaseModel):
    name: Name
    datasetGroupArn: Arn
    filterExpression: FilterExpression


class CreateSchemaResponse(BaseModel):
    schemaArn: Optional[Arn] = None


class CreateSchemaRequest(BaseModel):
    name: Name
    schema_: Annotated[AvroSchema, Field(alias='schema')]


class CreateSolutionResponse(BaseModel):
    solutionArn: Optional[Arn] = None


class CreateSolutionVersionResponse(BaseModel):
    solutionVersionArn: Optional[Arn] = None


class CreateSolutionVersionRequest(BaseModel):
    solutionArn: Arn
    trainingMode: Optional[TrainingMode] = None


class DeleteCampaignRequest(BaseModel):
    campaignArn: Arn


class DeleteDatasetRequest(BaseModel):
    datasetArn: Arn


class DeleteDatasetGroupRequest(BaseModel):
    datasetGroupArn: Arn


class DeleteEventTrackerRequest(BaseModel):
    eventTrackerArn: Arn


class DeleteFilterRequest(BaseModel):
    filterArn: Arn


class DeleteSchemaRequest(BaseModel):
    schemaArn: Arn


class DeleteSolutionRequest(BaseModel):
    solutionArn: Arn


class DescribeAlgorithmRequest(BaseModel):
    algorithmArn: Arn


class DescribeBatchInferenceJobRequest(BaseModel):
    batchInferenceJobArn: Arn


class DescribeCampaignResponse(BaseModel):
    campaign: Optional[Campaign] = None


class DescribeCampaignRequest(BaseModel):
    campaignArn: Arn


class DescribeDatasetResponse(BaseModel):
    dataset: Optional[Dataset] = None


class DescribeDatasetRequest(BaseModel):
    datasetArn: Arn


class DescribeDatasetExportJobRequest(BaseModel):
    datasetExportJobArn: Arn


class DescribeDatasetGroupResponse(BaseModel):
    datasetGroup: Optional[DatasetGroup] = None


class DescribeDatasetGroupRequest(BaseModel):
    datasetGroupArn: Arn


class DescribeDatasetImportJobRequest(BaseModel):
    datasetImportJobArn: Arn


class DescribeEventTrackerResponse(BaseModel):
    eventTracker: Optional[EventTracker] = None


class DescribeEventTrackerRequest(BaseModel):
    eventTrackerArn: Arn


class DescribeFeatureTransformationRequest(BaseModel):
    featureTransformationArn: Arn


class DescribeFilterResponse(BaseModel):
    filter: Optional[Filter] = None


class DescribeFilterRequest(BaseModel):
    filterArn: Arn


class DescribeRecipeRequest(BaseModel):
    recipeArn: Arn


class DescribeSchemaResponse(BaseModel):
    schema_: Annotated[Optional[DatasetSchema], Field(alias='schema')] = None


class DescribeSchemaRequest(BaseModel):
    schemaArn: Arn


class DescribeSolutionRequest(BaseModel):
    solutionArn: Arn


class DescribeSolutionVersionRequest(BaseModel):
    solutionVersionArn: Arn


class GetSolutionMetricsResponse(BaseModel):
    solutionVersionArn: Optional[Arn] = None
    metrics: Optional[Metrics] = None


class GetSolutionMetricsRequest(BaseModel):
    solutionVersionArn: Arn


class ListBatchInferenceJobsResponse(BaseModel):
    batchInferenceJobs: Optional[BatchInferenceJobs] = None
    nextToken: Optional[NextToken] = None


class ListBatchInferenceJobsRequest(BaseModel):
    solutionVersionArn: Optional[Arn] = None
    nextToken: Optional[NextToken] = None
    maxResults: Optional[MaxResults] = None


class ListCampaignsResponse(BaseModel):
    campaigns: Optional[Campaigns] = None
    nextToken: Optional[NextToken] = None


class ListCampaignsRequest(BaseModel):
    solutionArn: Optional[Arn] = None
    nextToken: Optional[NextToken] = None
    maxResults: Optional[MaxResults] = None


class ListDatasetExportJobsResponse(BaseModel):
    datasetExportJobs: Optional[DatasetExportJobs] = None
    nextToken: Optional[NextToken] = None


class ListDatasetExportJobsRequest(BaseModel):
    datasetArn: Optional[Arn] = None
    nextToken: Optional[NextToken] = None
    maxResults: Optional[MaxResults] = None


class ListDatasetGroupsResponse(BaseModel):
    datasetGroups: Optional[DatasetGroups] = None
    nextToken: Optional[NextToken] = None


class ListDatasetGroupsRequest(BaseModel):
    nextToken: Optional[NextToken] = None
    maxResults: Optional[MaxResults] = None


class ListDatasetImportJobsResponse(BaseModel):
    datasetImportJobs: Optional[DatasetImportJobs] = None
    nextToken: Optional[NextToken] = None


class ListDatasetImportJobsRequest(BaseModel):
    datasetArn: Optional[Arn] = None
    nextToken: Optional[NextToken] = None
    maxResults: Optional[MaxResults] = None


class ListDatasetsResponse(BaseModel):
    datasets: Optional[Datasets] = None
    nextToken: Optional[NextToken] = None


class ListDatasetsRequest(BaseModel):
    datasetGroupArn: Optional[Arn] = None
    nextToken: Optional[NextToken] = None
    maxResults: Optional[MaxResults] = None


class ListEventTrackersResponse(BaseModel):
    eventTrackers: Optional[EventTrackers] = None
    nextToken: Optional[NextToken] = None


class ListEventTrackersRequest(BaseModel):
    datasetGroupArn: Optional[Arn] = None
    nextToken: Optional[NextToken] = None
    maxResults: Optional[MaxResults] = None


class ListFiltersResponse(BaseModel):
    Filters: Optional[Filters] = None
    nextToken: Optional[NextToken] = None


class ListFiltersRequest(BaseModel):
    datasetGroupArn: Optional[Arn] = None
    nextToken: Optional[NextToken] = None
    maxResults: Optional[MaxResults] = None


class ListRecipesRequest(BaseModel):
    recipeProvider: Optional[RecipeProvider] = None
    nextToken: Optional[NextToken] = None
    maxResults: Optional[MaxResults] = None


class ListSchemasResponse(BaseModel):
    schemas: Optional[Schemas] = None
    nextToken: Optional[NextToken] = None


class ListSchemasRequest(BaseModel):
    nextToken: Optional[NextToken] = None
    maxResults: Optional[MaxResults] = None


class ListSolutionVersionsRequest(BaseModel):
    solutionArn: Optional[Arn] = None
    nextToken: Optional[NextToken] = None
    maxResults: Optional[MaxResults] = None


class ListSolutionsRequest(BaseModel):
    datasetGroupArn: Optional[Arn] = None
    nextToken: Optional[NextToken] = None
    maxResults: Optional[MaxResults] = None


class StopSolutionVersionCreationRequest(BaseModel):
    solutionVersionArn: Arn


class UpdateCampaignResponse(CreateCampaignResponse):
    pass


class UpdateCampaignRequest(BaseModel):
    campaignArn: Arn
    solutionVersionArn: Optional[Arn] = None
    minProvisionedTPS: Optional[TransactionsPerSecond] = None
    campaignConfig: Optional[CampaignConfig] = None


class AlgorithmImage(BaseModel):
    """
    Describes an algorithm image.
    """

    name: Optional[Name] = None
    dockerURI: DockerURI


class S3DataConfig(BaseModel):
    """
    The configuration details of an Amazon S3 input or output bucket.
    """

    path: S3Location
    kmsKeyArn: Optional[KmsKeyArn] = None


class CategoricalValues(BaseModel):
    __root__: Annotated[List[CategoricalValue], Field(max_items=100)]


class CategoricalHyperParameterRange(BaseModel):
    """
    Provides the name and range of a categorical hyperparameter.
    """

    name: Optional[ParameterName] = None
    values: Optional[CategoricalValues] = None


class CategoricalHyperParameterRanges1(BaseModel):
    __root__: Annotated[List[CategoricalHyperParameterRange], Field(max_items=100)]


class DatasetExportJobOutput(BaseModel):
    """
    The output configuration parameters of a dataset export job.
    """

    s3DataDestination: S3DataConfig


class DataSource(BaseModel):
    """
    Describes the data source that contains the data to upload to a dataset.
    """

    dataLocation: Optional[S3Location] = None


class DatasetExportJob(BaseModel):
    """
    <p>Describes a job that exports a dataset to an Amazon S3 bucket. For more information, see <a>CreateDatasetExportJob</a>.</p> <p>A dataset export job can be in one of the following states:</p> <ul> <li> <p>CREATE PENDING &gt; CREATE IN_PROGRESS &gt; ACTIVE -or- CREATE FAILED</p> </li> </ul>
    """

    jobName: Optional[Name] = None
    datasetExportJobArn: Optional[Arn] = None
    datasetArn: Optional[Arn] = None
    ingestionMode: Optional[IngestionMode] = None
    roleArn: Optional[Arn] = None
    status: Optional[Status] = None
    jobOutput: Optional[DatasetExportJobOutput] = None
    creationDateTime: Optional[Date] = None
    lastUpdatedDateTime: Optional[Date] = None
    failureReason: Optional[FailureReason] = None


class DatasetImportJob(BaseModel):
    """
    <p>Describes a job that imports training data from a data source (Amazon S3 bucket) to an Amazon Personalize dataset. For more information, see <a>CreateDatasetImportJob</a>.</p> <p>A dataset import job can be in one of the following states:</p> <ul> <li> <p>CREATE PENDING &gt; CREATE IN_PROGRESS &gt; ACTIVE -or- CREATE FAILED</p> </li> </ul>
    """

    jobName: Optional[Name] = None
    datasetImportJobArn: Optional[Arn] = None
    datasetArn: Optional[Arn] = None
    dataSource: Optional[DataSource] = None
    roleArn: Optional[Arn] = None
    status: Optional[Status] = None
    creationDateTime: Optional[Date] = None
    lastUpdatedDateTime: Optional[Date] = None
    failureReason: Optional[FailureReason] = None


class DefaultCategoricalHyperParameterRange(BaseModel):
    """
    Provides the name and default range of a categorical hyperparameter and whether the hyperparameter is tunable. A tunable hyperparameter can have its value determined during hyperparameter optimization (HPO).
    """

    name: Optional[ParameterName] = None
    values: Optional[CategoricalValues] = None
    isTunable: Optional[Tunable] = None


class DefaultCategoricalHyperParameterRanges(BaseModel):
    __root__: Annotated[
        List[DefaultCategoricalHyperParameterRange], Field(max_items=100)
    ]


class DefaultIntegerHyperParameterRanges(BaseModel):
    __root__: Annotated[List[DefaultIntegerHyperParameterRange], Field(max_items=100)]


class FeatureTransformation(BaseModel):
    """
    Provides feature transformation information. Feature transformation is the process of modifying raw input data into a form more suitable for model training.
    """

    name: Optional[Name] = None
    featureTransformationArn: Optional[Arn] = None
    defaultParameters: Optional[FeaturizationParameters] = None
    creationDateTime: Optional[Date] = None
    lastUpdatedDateTime: Optional[Date] = None
    status: Optional[Status] = None


class Recipe(BaseModel):
    """
    Provides information about a recipe. Each recipe provides an algorithm that Amazon Personalize uses in model training when you use the <a>CreateSolution</a> operation.
    """

    name: Optional[Name] = None
    recipeArn: Optional[Arn] = None
    algorithmArn: Optional[Arn] = None
    featureTransformationArn: Optional[Arn] = None
    status: Optional[Status] = None
    description: Optional[Description] = None
    creationDateTime: Optional[Date] = None
    recipeType: Optional[RecipeType] = None
    lastUpdatedDateTime: Optional[Date] = None


class HPOObjective(BaseModel):
    """
    <p>The metric to optimize during hyperparameter optimization (HPO).</p> <note> <p>Amazon Personalize doesn't support configuring the <code>hpoObjective</code> at this time.</p> </note>
    """

    type: Optional[HPOObjectiveType] = None
    metricName: Optional[MetricName] = None
    metricRegex: Optional[MetricRegex] = None


class HPOResourceConfig(BaseModel):
    """
    Describes the resource configuration for hyperparameter optimization (HPO).
    """

    maxNumberOfTrainingJobs: Optional[HPOResource] = None
    maxParallelTrainingJobs: Optional[HPOResource] = None


class IntegerHyperParameterRanges(BaseModel):
    __root__: Annotated[List[IntegerHyperParameterRange], Field(max_items=100)]


class Recipes(BaseModel):
    __root__: Annotated[List[RecipeSummary], Field(max_items=100)]


class SolutionVersions(BaseModel):
    __root__: Annotated[List[SolutionVersionSummary], Field(max_items=100)]


class Solutions(BaseModel):
    __root__: Annotated[List[SolutionSummary], Field(max_items=100)]


class CreateDatasetExportJobRequest(BaseModel):
    jobName: Name
    datasetArn: Arn
    ingestionMode: Optional[IngestionMode] = None
    roleArn: RoleArn
    jobOutput: DatasetExportJobOutput


class CreateDatasetImportJobRequest(BaseModel):
    jobName: Name
    datasetArn: Arn
    dataSource: DataSource
    roleArn: RoleArn


class DescribeDatasetExportJobResponse(BaseModel):
    datasetExportJob: Optional[DatasetExportJob] = None


class DescribeDatasetImportJobResponse(BaseModel):
    datasetImportJob: Optional[DatasetImportJob] = None


class DescribeFeatureTransformationResponse(BaseModel):
    featureTransformation: Optional[FeatureTransformation] = None


class DescribeRecipeResponse(BaseModel):
    recipe: Optional[Recipe] = None


class ListRecipesResponse(BaseModel):
    recipes: Optional[Recipes] = None
    nextToken: Optional[NextToken] = None


class ListSolutionVersionsResponse(BaseModel):
    solutionVersions: Optional[SolutionVersions] = None
    nextToken: Optional[NextToken] = None


class ListSolutionsResponse(BaseModel):
    solutions: Optional[Solutions] = None
    nextToken: Optional[NextToken] = None


class DefaultHyperParameterRanges(BaseModel):
    """
    Specifies the hyperparameters and their default ranges. Hyperparameters can be categorical, continuous, or integer-valued.
    """

    integerHyperParameterRanges: Optional[DefaultIntegerHyperParameterRanges] = None
    continuousHyperParameterRanges: Optional[
        DefaultContinuousHyperParameterRanges
    ] = None
    categoricalHyperParameterRanges: Optional[
        DefaultCategoricalHyperParameterRanges
    ] = None


class Algorithm(BaseModel):
    """
    Describes a custom algorithm.
    """

    name: Optional[Name] = None
    algorithmArn: Optional[Arn] = None
    algorithmImage: Optional[AlgorithmImage] = None
    defaultHyperParameters: Optional[HyperParameters] = None
    defaultHyperParameterRanges: Optional[DefaultHyperParameterRanges] = None
    defaultResourceConfig: Optional[ResourceConfig] = None
    trainingInputMode: Optional[TrainingInputMode] = None
    roleArn: Optional[Arn] = None
    creationDateTime: Optional[Date] = None
    lastUpdatedDateTime: Optional[Date] = None


class BatchInferenceJobInput(BaseModel):
    """
    The input configuration of a batch inference job.
    """

    s3DataSource: S3DataConfig


class BatchInferenceJobOutput(DatasetExportJobOutput):
    """
    The output configuration parameters of a batch inference job.
    """

    pass


class BatchInferenceJob(BaseModel):
    """
    Contains information on a batch inference job.
    """

    jobName: Optional[Name] = None
    batchInferenceJobArn: Optional[Arn] = None
    filterArn: Optional[Arn] = None
    failureReason: Optional[FailureReason] = None
    solutionVersionArn: Optional[Arn] = None
    numResults: Optional[NumBatchResults] = None
    jobInput: Optional[BatchInferenceJobInput] = None
    jobOutput: Optional[BatchInferenceJobOutput] = None
    batchInferenceJobConfig: Optional[BatchInferenceJobConfig] = None
    roleArn: Optional[RoleArn] = None
    status: Optional[Status] = None
    creationDateTime: Optional[Date] = None
    lastUpdatedDateTime: Optional[Date] = None


class HyperParameterRanges(BaseModel):
    """
    Specifies the hyperparameters and their ranges. Hyperparameters can be categorical, continuous, or integer-valued.
    """

    integerHyperParameterRanges: Optional[IntegerHyperParameterRanges] = None
    continuousHyperParameterRanges: Optional[ContinuousHyperParameterRanges1] = None
    categoricalHyperParameterRanges: Optional[CategoricalHyperParameterRanges1] = None


class HPOConfig(BaseModel):
    """
    Describes the properties for hyperparameter optimization (HPO).
    """

    hpoObjective: Optional[HPOObjective] = None
    hpoResourceConfig: Optional[HPOResourceConfig] = None
    algorithmHyperParameterRanges: Optional[HyperParameterRanges] = None


class CreateBatchInferenceJobRequest(BaseModel):
    jobName: Name
    solutionVersionArn: Arn
    filterArn: Optional[Arn] = None
    numResults: Optional[NumBatchResults] = None
    jobInput: BatchInferenceJobInput
    jobOutput: BatchInferenceJobOutput
    roleArn: RoleArn
    batchInferenceJobConfig: Optional[BatchInferenceJobConfig] = None


class DescribeAlgorithmResponse(BaseModel):
    algorithm: Optional[Algorithm] = None


class DescribeBatchInferenceJobResponse(BaseModel):
    batchInferenceJob: Optional[BatchInferenceJob] = None


class SolutionConfig(BaseModel):
    """
    Describes the configuration properties for the solution.
    """

    eventValueThreshold: Optional[EventValueThreshold] = None
    hpoConfig: Optional[HPOConfig] = None
    algorithmHyperParameters: Optional[HyperParameters] = None
    featureTransformationParameters: Optional[FeatureTransformationParameters] = None
    autoMLConfig: Optional[AutoMLConfig] = None
    optimizationObjective: Optional[OptimizationObjective] = None


class Solution(BaseModel):
    """
    An object that provides information about a solution. A solution is a trained model that can be deployed as a campaign.
    """

    name: Optional[Name] = None
    solutionArn: Optional[Arn] = None
    performHPO: Optional[PerformHPO] = None
    performAutoML: Optional[PerformAutoML] = None
    recipeArn: Optional[Arn] = None
    datasetGroupArn: Optional[Arn] = None
    eventType: Optional[EventType] = None
    solutionConfig: Optional[SolutionConfig] = None
    autoMLResult: Optional[AutoMLResult] = None
    status: Optional[Status] = None
    creationDateTime: Optional[Date] = None
    lastUpdatedDateTime: Optional[Date] = None
    latestSolutionVersion: Optional[SolutionVersionSummary] = None


class SolutionVersion(BaseModel):
    """
    An object that provides information about a specific version of a <a>Solution</a>.
    """

    solutionVersionArn: Optional[Arn] = None
    solutionArn: Optional[Arn] = None
    performHPO: Optional[PerformHPO] = None
    performAutoML: Optional[PerformAutoML] = None
    recipeArn: Optional[Arn] = None
    eventType: Optional[EventType] = None
    datasetGroupArn: Optional[Arn] = None
    solutionConfig: Optional[SolutionConfig] = None
    trainingHours: Optional[TrainingHours] = None
    trainingMode: Optional[TrainingMode] = None
    tunedHPOParams: Optional[TunedHPOParams] = None
    status: Optional[Status] = None
    failureReason: Optional[FailureReason] = None
    creationDateTime: Optional[Date] = None
    lastUpdatedDateTime: Optional[Date] = None


class CreateSolutionRequest(BaseModel):
    name: Name
    performHPO: Optional[Boolean] = None
    performAutoML: Optional[PerformAutoML] = None
    recipeArn: Optional[Arn] = None
    datasetGroupArn: Arn
    eventType: Optional[EventType] = None
    solutionConfig: Optional[SolutionConfig] = None


class DescribeSolutionResponse(BaseModel):
    solution: Optional[Solution] = None


class DescribeSolutionVersionResponse(BaseModel):
    solutionVersion: Optional[SolutionVersion] = None
