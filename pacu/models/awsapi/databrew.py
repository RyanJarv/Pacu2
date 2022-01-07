# generated by datamodel-codegen:
#   filename:  openapi.yaml
#   timestamp: 2021-12-31T02:47:13+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Annotated, Any, List, Optional

from pydantic import BaseModel, Extra, Field


class RecipeVersion(BaseModel):
    __root__: Annotated[str, Field(max_length=16, min_length=1)]


class ConflictException(BaseModel):
    __root__: Any


class ResourceNotFoundException(ConflictException):
    pass


class ValidationException(ConflictException):
    pass


class PathParametersMap(BaseModel):
    """
    A structure that map names of parameters used in the Amazon S3 path of a dataset to their definitions. A definition includes parameter type and conditions.
    """

    pass

    class Config:
        extra = Extra.allow


class TagValue(BaseModel):
    __root__: Annotated[str, Field(max_length=256)]


class AccessDeniedException(ConflictException):
    pass


class ServiceQuotaExceededException(ConflictException):
    pass


class Bucket(BaseModel):
    __root__: Annotated[str, Field(max_length=63, min_length=3)]


class Key(BaseModel):
    __root__: Annotated[str, Field(max_length=1280, min_length=1)]


class SampleMode(Enum):
    FULL_DATASET = 'FULL_DATASET'
    CUSTOM_ROWS = 'CUSTOM_ROWS'


class JobSize(BaseModel):
    __root__: int


class SampleSize(BaseModel):
    __root__: Annotated[int, Field(ge=1.0, le=5000.0)]


class SampleType(Enum):
    FIRST_N = 'FIRST_N'
    LAST_N = 'LAST_N'
    RANDOM = 'RANDOM'


class InternalServerException(ConflictException):
    pass


class RecipeName(BaseModel):
    __root__: Annotated[str, Field(max_length=255, min_length=1)]


class JobName(BaseModel):
    __root__: Annotated[str, Field(max_length=240, min_length=1)]


class DeleteJobResponse(BaseModel):
    Name: JobName


class DeleteRecipeVersionResponse(BaseModel):
    Name: RecipeName
    RecipeVersion: RecipeVersion


class PublishRecipeResponse(BaseModel):
    Name: RecipeName


class StartColumnIndex(BaseModel):
    __root__: Annotated[int, Field(ge=0.0)]


class ColumnRange(BaseModel):
    __root__: Annotated[int, Field(ge=0.0, le=20.0)]


class TagResourceResponse(BaseModel):
    pass


class UntagResourceResponse(TagResourceResponse):
    pass


class TagKey(BaseModel):
    __root__: Annotated[str, Field(max_length=128, min_length=1)]


class UpdateProfileJobResponse(DeleteJobResponse):
    pass


class UpdateRecipeResponse(PublishRecipeResponse):
    pass


class UpdateRecipeJobResponse(DeleteJobResponse):
    pass


class AccountId(BaseModel):
    __root__: Annotated[str, Field(max_length=255)]


class ActionId(JobSize):
    pass


class Arn(BaseModel):
    __root__: Annotated[str, Field(max_length=2048, min_length=20)]


class AssumeControl(BaseModel):
    __root__: bool


class Attempt(JobSize):
    pass


class RecipeVersionList(BaseModel):
    __root__: Annotated[List[RecipeVersion], Field(max_items=50, min_items=1)]


class BatchDeleteRecipeVersionRequest(BaseModel):
    RecipeVersions: RecipeVersionList


class CatalogId(RecipeName):
    pass


class ClientSessionId(BaseModel):
    __root__: Annotated[
        str, Field(max_length=255, min_length=1, regex='^[a-zA-Z0-9][a-zA-Z0-9-]*$')
    ]


class ColumnName(RecipeName):
    pass


class ColumnNameList(BaseModel):
    __root__: Annotated[List[ColumnName], Field(max_items=200)]


class ColumnSelector(BaseModel):
    """
    Selector of a column from a dataset for profile job configuration. One selector includes either a column name or a regular expression.
    """

    Regex: Optional[ColumnName] = None
    Name: Optional[ColumnName] = None


class CompressionFormat(Enum):
    GZIP = 'GZIP'
    LZ4 = 'LZ4'
    SNAPPY = 'SNAPPY'
    BZIP2 = 'BZIP2'
    DEFLATE = 'DEFLATE'
    LZO = 'LZO'
    BROTLI = 'BROTLI'
    ZSTD = 'ZSTD'
    ZLIB = 'ZLIB'


class Condition(BaseModel):
    __root__: Annotated[str, Field(max_length=128, min_length=1, regex='^[A-Z\\_]+$')]


class ConditionValue(BaseModel):
    __root__: Annotated[str, Field(max_length=1024)]


class TargetColumn(BaseModel):
    __root__: Annotated[str, Field(max_length=1024, min_length=1)]


class ConditionExpression(BaseModel):
    """
    <p>Represents an individual condition that evaluates to true or false.</p> <p>Conditions are used with recipe actions. The action is only performed for column values where the condition evaluates to true.</p> <p>If a recipe requires more than one condition, then the recipe must specify multiple <code>ConditionExpression</code> elements. Each condition is applied to the rows in a dataset first, before the recipe action is performed.</p>
    """

    Condition: Condition
    Value: Optional[ConditionValue] = None
    TargetColumn: TargetColumn


class CreateColumn(AssumeControl):
    pass


class DatasetName(RecipeName):
    pass


class InputFormat(Enum):
    CSV = 'CSV'
    JSON = 'JSON'
    PARQUET = 'PARQUET'
    EXCEL = 'EXCEL'


class TagMap(BaseModel):
    pass

    class Config:
        extra = Extra.allow


class EncryptionKeyArn(Arn):
    pass


class EncryptionMode(Enum):
    SSE_KMS = 'SSE-KMS'
    SSE_S3 = 'SSE-S3'


class LogSubscription(Enum):
    ENABLE = 'ENABLE'
    DISABLE = 'DISABLE'


class MaxCapacity(JobSize):
    pass


class MaxRetries(StartColumnIndex):
    pass


class Timeout(StartColumnIndex):
    pass


class JobSample(BaseModel):
    """
    A sample configuration for profile jobs only, which determines the number of rows on which the profile job is run. If a <code>JobSample</code> value isn't provided, the default is used. The default value is CUSTOM_ROWS for the mode parameter and 20,000 for the size parameter.
    """

    Mode: Optional[SampleMode] = None
    Size: Optional[JobSize] = None


class ProjectName(RecipeName):
    pass


class Sample(BaseModel):
    """
    Represents the sample size and sampling type for DataBrew to use for interactive data analysis.
    """

    Size: Optional[SampleSize] = None
    Type: SampleType


class CreateProjectRequest(BaseModel):
    DatasetName: DatasetName
    Name: ProjectName
    RecipeName: RecipeName
    Sample: Optional[Sample] = None
    RoleArn: Arn
    Tags: Optional[TagMap] = None


class RecipeReference(BaseModel):
    """
    Represents the name and version of a DataBrew recipe.
    """

    Name: RecipeName
    RecipeVersion: Optional[RecipeVersion] = None


class RecipeDescription(ConditionValue):
    pass


class JobNameList(BaseModel):
    __root__: Annotated[List[JobName], Field(max_items=50)]


class CronExpression(BaseModel):
    __root__: Annotated[str, Field(max_length=512, min_length=1)]


class ScheduleName(RecipeName):
    pass


class CreateScheduleRequest(BaseModel):
    JobNames: Optional[JobNameList] = None
    CronExpression: CronExpression
    Tags: Optional[TagMap] = None
    Name: ScheduleName


class CreatedBy(BaseModel):
    __root__: str


class Delimiter(BaseModel):
    __root__: Annotated[str, Field(max_length=1, min_length=1)]


class HeaderRow(AssumeControl):
    pass


class CsvOutputOptions(BaseModel):
    """
    Represents a set of options that define how DataBrew will write a comma-separated value (CSV) file.
    """

    Delimiter: Optional[Delimiter] = None


class DatabaseName(RecipeName):
    pass


class TableName(RecipeName):
    pass


class OverwriteOutput(AssumeControl):
    pass


class GlueConnectionName(RecipeName):
    pass


class DatabaseTableName(RecipeName):
    pass


class DatabaseOutputMode(Enum):
    NEW_TABLE = 'NEW_TABLE'


class Date(BaseModel):
    __root__: datetime


class LastModifiedBy(CreatedBy):
    pass


class Source(Enum):
    S3 = 'S3'
    DATA_CATALOG = 'DATA-CATALOG'
    DATABASE = 'DATABASE'


class PathParameterName(RecipeName):
    pass


class ParameterType(Enum):
    Datetime = 'Datetime'
    Number = 'Number'
    String = 'String'


class DatetimeFormat(BaseModel):
    __root__: Annotated[str, Field(max_length=100, min_length=2)]


class TimezoneOffset(BaseModel):
    __root__: Annotated[
        str,
        Field(
            max_length=6, min_length=1, regex='^(Z|[-+](\\d|\\d{2}|\\d{2}:?\\d{2}))$'
        ),
    ]


class LocaleCode(BaseModel):
    __root__: Annotated[
        str, Field(max_length=100, min_length=2, regex='^[A-Za-z0-9_\\.#@\\-]+$')
    ]


class DeleteDatasetRequest(BaseModel):
    pass


class DeleteJobRequest(BaseModel):
    pass


class DeleteProjectRequest(BaseModel):
    pass


class DeleteRecipeVersionRequest(BaseModel):
    pass


class DeleteScheduleRequest(BaseModel):
    pass


class DescribeDatasetRequest(BaseModel):
    pass


class DescribeJobRequest(BaseModel):
    pass


class JobType(Enum):
    PROFILE = 'PROFILE'
    RECIPE = 'RECIPE'


class JobRunId(RecipeName):
    pass


class DescribeJobRunRequest(BaseModel):
    pass


class JobRunErrorMessage(CreatedBy):
    pass


class ExecutionTime(JobSize):
    pass


class JobRunState(Enum):
    STARTING = 'STARTING'
    RUNNING = 'RUNNING'
    STOPPING = 'STOPPING'
    STOPPED = 'STOPPED'
    SUCCEEDED = 'SUCCEEDED'
    FAILED = 'FAILED'
    TIMEOUT = 'TIMEOUT'


class LogGroupName(CronExpression):
    pass


class StartedBy(CreatedBy):
    pass


class DescribeProjectRequest(BaseModel):
    pass


class SessionStatus(Enum):
    ASSIGNED = 'ASSIGNED'
    FAILED = 'FAILED'
    INITIALIZING = 'INITIALIZING'
    PROVISIONING = 'PROVISIONING'
    READY = 'READY'
    RECYCLING = 'RECYCLING'
    ROTATING = 'ROTATING'
    TERMINATED = 'TERMINATED'
    TERMINATING = 'TERMINATING'
    UPDATING = 'UPDATING'


class OpenedBy(CreatedBy):
    pass


class DescribeRecipeRequest(BaseModel):
    pass


class PublishedBy(CreatedBy):
    pass


class DescribeScheduleRequest(BaseModel):
    pass


class ErrorCode(BaseModel):
    __root__: Annotated[str, Field(regex='^[1-5][0-9][0-9]$')]


class Expression(BaseModel):
    __root__: Annotated[
        str, Field(max_length=1024, min_length=4, regex='^[<>0-9A-Za-z_:)(!= ]+$')
    ]


class MaxFiles(BaseModel):
    __root__: Annotated[int, Field(ge=1.0)]


class OrderedBy(Enum):
    LAST_MODIFIED_DATE = 'LAST_MODIFIED_DATE'


class Order(Enum):
    DESCENDING = 'DESCENDING'
    ASCENDING = 'ASCENDING'


class ValuesMap(BaseModel):
    pass

    class Config:
        extra = Extra.allow


class MultiLine(AssumeControl):
    pass


class MaxResults100(BaseModel):
    __root__: Annotated[int, Field(ge=1.0, le=100.0)]


class NextToken(BaseModel):
    __root__: Annotated[str, Field(max_length=2000, min_length=1)]


class ListDatasetsRequest(BaseModel):
    pass


class ListJobRunsRequest(BaseModel):
    pass


class ListJobsRequest(BaseModel):
    pass


class ListProjectsRequest(BaseModel):
    pass


class ListRecipeVersionsRequest(BaseModel):
    pass


class ListRecipesRequest(BaseModel):
    pass


class ListSchedulesRequest(BaseModel):
    pass


class ListTagsForResourceRequest(BaseModel):
    pass


class Operation(Condition):
    pass


class OutputFormat(Enum):
    CSV = 'CSV'
    JSON = 'JSON'
    PARQUET = 'PARQUET'
    GLUEPARQUET = 'GLUEPARQUET'
    AVRO = 'AVRO'
    ORC = 'ORC'
    XML = 'XML'
    TABLEAUHYPER = 'TABLEAUHYPER'


class OutputFormatOptions(BaseModel):
    """
    Represents a set of options that define the structure of comma-separated (CSV) job output.
    """

    Csv: Optional[CsvOutputOptions] = None


class ParameterValue(BaseModel):
    __root__: Annotated[str, Field(max_length=32768, min_length=1)]


class ParameterMap(BaseModel):
    pass

    class Config:
        extra = Extra.allow


class ParameterName(BaseModel):
    __root__: Annotated[
        str, Field(max_length=128, min_length=1, regex='^[A-Za-z0-9]+$')
    ]


class Preview(AssumeControl):
    pass


class Project(BaseModel):
    """
    Represents all of the attributes of a DataBrew project.
    """

    AccountId: Optional[AccountId] = None
    CreateDate: Optional[Date] = None
    CreatedBy: Optional[CreatedBy] = None
    DatasetName: Optional[DatasetName] = None
    LastModifiedDate: Optional[Date] = None
    LastModifiedBy: Optional[LastModifiedBy] = None
    Name: ProjectName
    RecipeName: RecipeName
    ResourceArn: Optional[Arn] = None
    Sample: Optional[Sample] = None
    Tags: Optional[TagMap] = None
    RoleArn: Optional[Arn] = None
    OpenedBy: Optional[OpenedBy] = None
    OpenDate: Optional[Date] = None


class PublishRecipeRequest(BaseModel):
    Description: Optional[RecipeDescription] = None


class RecipeErrorMessage(CreatedBy):
    pass


class Result(CreatedBy):
    pass


class Schedule(BaseModel):
    """
    Represents one or more dates and times when a job is to run.
    """

    AccountId: Optional[AccountId] = None
    CreatedBy: Optional[CreatedBy] = None
    CreateDate: Optional[Date] = None
    JobNames: Optional[JobNameList] = None
    LastModifiedBy: Optional[LastModifiedBy] = None
    LastModifiedDate: Optional[Date] = None
    ResourceArn: Optional[Arn] = None
    CronExpression: Optional[CronExpression] = None
    Tags: Optional[TagMap] = None
    Name: ScheduleName


class StepIndex(StartColumnIndex):
    pass


class SheetIndex(BaseModel):
    __root__: Annotated[int, Field(ge=0.0, le=200.0)]


class SheetName(BaseModel):
    __root__: Annotated[str, Field(max_length=31, min_length=1)]


class StartJobRunRequest(BaseModel):
    pass


class StartProjectSessionRequest(BaseModel):
    AssumeControl: Optional[AssumeControl] = None


class Statistic(Condition):
    pass


class StatisticList(BaseModel):
    __root__: Annotated[List[Statistic], Field(min_items=1)]


class StatisticOverride(BaseModel):
    """
    Override of a particular evaluation for a profile job.
    """

    Statistic: Statistic
    Parameters: ParameterMap


class StatisticOverrideList(BaseModel):
    __root__: Annotated[List[StatisticOverride], Field(min_items=1)]


class StopJobRunRequest(BaseModel):
    pass


class TagKeyList(BaseModel):
    __root__: Annotated[List[TagKey], Field(max_items=200, min_items=1)]


class TagResourceRequest(BaseModel):
    Tags: TagMap


class UntagResourceRequest(BaseModel):
    pass


class UpdateProjectRequest(BaseModel):
    Sample: Optional[Sample] = None
    RoleArn: Arn


class UpdateScheduleRequest(BaseModel):
    JobNames: Optional[JobNameList] = None
    CronExpression: CronExpression


class ValueReference(BaseModel):
    __root__: Annotated[
        str, Field(max_length=128, min_length=2, regex='^:[A-Za-z0-9_]+$')
    ]


class CreateDatasetResponse(BaseModel):
    Name: DatasetName


class JsonOptions(BaseModel):
    """
    Represents the JSON-specific options that define how input is to be interpreted by Glue DataBrew.
    """

    MultiLine: Optional[MultiLine] = None


class CsvOptions(BaseModel):
    """
    Represents a set of options that define how DataBrew will read a comma-separated value (CSV) file when creating a dataset from that file.
    """

    Delimiter: Optional[Delimiter] = None
    HeaderRow: Optional[HeaderRow] = None


class S3Location(BaseModel):
    """
    Represents an Amazon S3 location (bucket name and object key) where DataBrew can read input data, or write output from a job.
    """

    Bucket: Bucket
    Key: Optional[Key] = None


class DataCatalogInputDefinition(BaseModel):
    """
    Represents how metadata stored in the Glue Data Catalog is defined in a DataBrew dataset.
    """

    CatalogId: Optional[CatalogId] = None
    DatabaseName: DatabaseName
    TableName: TableName
    TempDirectory: Optional[S3Location] = None


class DatabaseInputDefinition(BaseModel):
    """
    Connection information for dataset input files stored in a database.
    """

    GlueConnectionName: GlueConnectionName
    DatabaseTableName: DatabaseTableName
    TempDirectory: Optional[S3Location] = None


class FilterExpression(BaseModel):
    """
    Represents a structure for defining parameter conditions. Supported conditions are described here: <a href="https://docs-aws.amazon.com/databrew/latest/dg/datasets.multiple-files.html#conditions.for.dynamic.datasets">Supported conditions for dynamic datasets</a> in the <i>Glue DataBrew Developer Guide</i>.
    """

    Expression: Expression
    ValuesMap: ValuesMap


class FilesLimit(BaseModel):
    """
    Represents a limit imposed on number of Amazon S3 files that should be selected for a dataset from a connected Amazon S3 path.
    """

    MaxFiles: MaxFiles
    OrderedBy: Optional[OrderedBy] = None
    Order: Optional[Order] = None


class CreateProfileJobResponse(DeleteJobResponse):
    pass


class StatisticsConfiguration(BaseModel):
    """
    Configuration of evaluations for a profile job. This configuration can be used to select evaluations and override the parameters of selected evaluations.
    """

    IncludedStatistics: Optional[StatisticList] = None
    Overrides: Optional[StatisticOverrideList] = None


class ColumnSelectorList(BaseModel):
    __root__: Annotated[List[ColumnSelector], Field(min_items=1)]


class CreateProjectResponse(BaseModel):
    Name: ProjectName


class CreateRecipeResponse(PublishRecipeResponse):
    pass


class CreateRecipeJobResponse(DeleteJobResponse):
    pass


class Output(BaseModel):
    """
    Represents options that specify how and where in Amazon S3 DataBrew writes the output generated by recipe jobs or profile jobs.
    """

    CompressionFormat: Optional[CompressionFormat] = None
    Format: Optional[OutputFormat] = None
    PartitionColumns: Optional[ColumnNameList] = None
    Location: S3Location
    Overwrite: Optional[OverwriteOutput] = None
    FormatOptions: Optional[OutputFormatOptions] = None


class CreateScheduleResponse(BaseModel):
    Name: ScheduleName


class DeleteDatasetResponse(CreateDatasetResponse):
    pass


class DeleteProjectResponse(CreateProjectResponse):
    pass


class DeleteScheduleResponse(CreateScheduleResponse):
    pass


class DescribeProjectResponse(BaseModel):
    CreateDate: Optional[Date] = None
    CreatedBy: Optional[CreatedBy] = None
    DatasetName: Optional[DatasetName] = None
    LastModifiedDate: Optional[Date] = None
    LastModifiedBy: Optional[LastModifiedBy] = None
    Name: ProjectName
    RecipeName: Optional[RecipeName] = None
    ResourceArn: Optional[Arn] = None
    Sample: Optional[Sample] = None
    RoleArn: Optional[Arn] = None
    Tags: Optional[TagMap] = None
    SessionStatus: Optional[SessionStatus] = None
    OpenedBy: Optional[OpenedBy] = None
    OpenDate: Optional[Date] = None


class DescribeScheduleResponse(BaseModel):
    CreateDate: Optional[Date] = None
    CreatedBy: Optional[CreatedBy] = None
    JobNames: Optional[JobNameList] = None
    LastModifiedBy: Optional[LastModifiedBy] = None
    LastModifiedDate: Optional[Date] = None
    ResourceArn: Optional[Arn] = None
    CronExpression: Optional[CronExpression] = None
    Tags: Optional[TagMap] = None
    Name: ScheduleName


class ListTagsForResourceResponse(BaseModel):
    Tags: Optional[TagMap] = None


class SendProjectSessionActionResponse(BaseModel):
    Result: Optional[Result] = None
    Name: ProjectName
    ActionId: Optional[ActionId] = None


class RecipeAction(BaseModel):
    """
    Represents a transformation and associated parameters that are used to apply a change to a DataBrew dataset. For more information, see <a href="https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions-reference.html">Recipe actions reference</a>.
    """

    Operation: Operation
    Parameters: Optional[ParameterMap] = None


class ConditionExpressionList(BaseModel):
    __root__: List[ConditionExpression]


class HiddenColumnList(BaseModel):
    __root__: List[ColumnName]


class StartJobRunResponse(BaseModel):
    RunId: JobRunId


class StartProjectSessionResponse(BaseModel):
    Name: ProjectName
    ClientSessionId: Optional[ClientSessionId] = None


class StopJobRunResponse(StartJobRunResponse):
    pass


class UpdateDatasetResponse(CreateDatasetResponse):
    pass


class UpdateProjectResponse(BaseModel):
    LastModifiedDate: Optional[Date] = None
    Name: ProjectName


class UpdateScheduleResponse(CreateScheduleResponse):
    pass


class ColumnStatisticsConfiguration(BaseModel):
    """
    Configuration for column evaluations for a profile job. ColumnStatisticsConfiguration can be used to select evaluations and override parameters of evaluations for particular columns.
    """

    Selectors: Optional[ColumnSelectorList] = None
    Statistics: StatisticsConfiguration


class Input(BaseModel):
    """
    Represents information on how DataBrew can find data, in either the Glue Data Catalog or Amazon S3.
    """

    S3InputDefinition: Optional[S3Location] = None
    DataCatalogInputDefinition: Optional[DataCatalogInputDefinition] = None
    DatabaseInputDefinition: Optional[DatabaseInputDefinition] = None


class PathOptions(BaseModel):
    """
    Represents a set of options that define how DataBrew selects files for a given Amazon S3 path in a dataset.
    """

    LastModifiedDateCondition: Optional[FilterExpression] = None
    FilesLimit: Optional[FilesLimit] = None
    Parameters: Optional[PathParametersMap] = None


class OutputList(BaseModel):
    __root__: Annotated[List[Output], Field(min_items=1)]


class S3TableOutputOptions(BaseModel):
    """
    Represents options that specify how and where DataBrew writes the Amazon S3 output generated by recipe jobs.
    """

    Location: S3Location


class DatabaseTableOutputOptions(BaseModel):
    """
    Represents options that specify how and where DataBrew writes the database output generated by recipe jobs.
    """

    TempDirectory: Optional[S3Location] = None
    TableName: DatabaseTableName


class DatetimeOptions(BaseModel):
    """
    Represents additional options for correct interpretation of datetime parameters used in the Amazon S3 path of a dataset.
    """

    Format: DatetimeFormat
    TimezoneOffset: Optional[TimezoneOffset] = None
    LocaleCode: Optional[LocaleCode] = None


class DatasetParameter(BaseModel):
    """
    Represents a dataset paramater that defines type and conditions for a parameter in the Amazon S3 path of the dataset.
    """

    Name: PathParameterName
    Type: ParameterType
    DatetimeOptions: Optional[DatetimeOptions] = None
    CreateColumn: Optional[CreateColumn] = None
    Filter: Optional[FilterExpression] = None


class SheetNameList(BaseModel):
    __root__: Annotated[List[SheetName], Field(max_items=1, min_items=1)]


class SheetIndexList(BaseModel):
    __root__: Annotated[List[SheetIndex], Field(max_items=1, min_items=1)]


class ProjectList(BaseModel):
    __root__: List[Project]


class ScheduleList(BaseModel):
    __root__: List[Schedule]


class RecipeVersionErrorDetail(BaseModel):
    """
    Represents any errors encountered when attempting to delete multiple recipe versions.
    """

    ErrorCode: Optional[ErrorCode] = None
    ErrorMessage: Optional[RecipeErrorMessage] = None
    RecipeVersion: Optional[RecipeVersion] = None


class ViewFrame(BaseModel):
    """
    Represents the data being transformed during an action.
    """

    StartColumnIndex: StartColumnIndex
    ColumnRange: Optional[ColumnRange] = None
    HiddenColumns: Optional[HiddenColumnList] = None


class ExcelOptions(BaseModel):
    """
    Represents a set of options that define how DataBrew will interpret a Microsoft Excel file when creating a dataset from that file.
    """

    SheetNames: Optional[SheetNameList] = None
    SheetIndexes: Optional[SheetIndexList] = None
    HeaderRow: Optional[HeaderRow] = None


class ColumnStatisticsConfigurationList(BaseModel):
    __root__: Annotated[List[ColumnStatisticsConfiguration], Field(min_items=1)]


class RecipeStep(BaseModel):
    """
    Represents a single step from a DataBrew recipe to be performed.
    """

    Action: RecipeAction
    ConditionExpressions: Optional[ConditionExpressionList] = None


class DataCatalogOutput(BaseModel):
    """
    Represents options that specify how and where in the Glue Data Catalog DataBrew writes the output generated by recipe jobs.
    """

    CatalogId: Optional[CatalogId] = None
    DatabaseName: DatabaseName
    TableName: TableName
    S3Options: Optional[S3TableOutputOptions] = None
    DatabaseOptions: Optional[DatabaseTableOutputOptions] = None
    Overwrite: Optional[OverwriteOutput] = None


class DatabaseOutput(BaseModel):
    """
    Represents a JDBC database output object which defines the output destination for a DataBrew recipe job to write into.
    """

    GlueConnectionName: GlueConnectionName
    DatabaseOptions: DatabaseTableOutputOptions
    DatabaseOutputMode: Optional[DatabaseOutputMode] = None


class ListProjectsResponse(BaseModel):
    Projects: ProjectList
    NextToken: Optional[NextToken] = None


class ListSchedulesResponse(BaseModel):
    Schedules: ScheduleList
    NextToken: Optional[NextToken] = None


class RecipeErrorList(BaseModel):
    __root__: List[RecipeVersionErrorDetail]


class FormatOptions(BaseModel):
    """
    Represents a set of options that define the structure of either comma-separated value (CSV), Excel, or JSON input.
    """

    Json: Optional[JsonOptions] = None
    Excel: Optional[ExcelOptions] = None
    Csv: Optional[CsvOptions] = None


class CreateDatasetRequest(BaseModel):
    Name: DatasetName
    Format: Optional[InputFormat] = None
    FormatOptions: Optional[FormatOptions] = None
    Input: Input
    PathOptions: Optional[PathOptions] = None
    Tags: Optional[TagMap] = None


class ProfileConfiguration(BaseModel):
    """
    Configuration for profile jobs. Configuration can be used to select columns, do evaluations, and override default parameters of evaluations. When configuration is undefined, the profile job will apply default settings to all supported columns.
    """

    DatasetStatisticsConfiguration: Optional[StatisticsConfiguration] = None
    ProfileColumns: Optional[ColumnSelectorList] = None
    ColumnStatisticsConfigurations: Optional[ColumnStatisticsConfigurationList] = None


class CreateProfileJobRequest(BaseModel):
    DatasetName: DatasetName
    EncryptionKeyArn: Optional[EncryptionKeyArn] = None
    EncryptionMode: Optional[EncryptionMode] = None
    Name: JobName
    LogSubscription: Optional[LogSubscription] = None
    MaxCapacity: Optional[MaxCapacity] = None
    MaxRetries: Optional[MaxRetries] = None
    OutputLocation: S3Location
    Configuration: Optional[ProfileConfiguration] = None
    RoleArn: Arn
    Tags: Optional[TagMap] = None
    Timeout: Optional[Timeout] = None
    JobSample: Optional[JobSample] = None


class DataCatalogOutputList(BaseModel):
    __root__: Annotated[List[DataCatalogOutput], Field(min_items=1)]


class DatabaseOutputList(BaseModel):
    __root__: Annotated[List[DatabaseOutput], Field(min_items=1)]


class CreateRecipeJobRequest(BaseModel):
    DatasetName: Optional[DatasetName] = None
    EncryptionKeyArn: Optional[EncryptionKeyArn] = None
    EncryptionMode: Optional[EncryptionMode] = None
    Name: JobName
    LogSubscription: Optional[LogSubscription] = None
    MaxCapacity: Optional[MaxCapacity] = None
    MaxRetries: Optional[MaxRetries] = None
    Outputs: Optional[OutputList] = None
    DataCatalogOutputs: Optional[DataCatalogOutputList] = None
    DatabaseOutputs: Optional[DatabaseOutputList] = None
    ProjectName: Optional[ProjectName] = None
    RecipeReference: Optional[RecipeReference] = None
    RoleArn: Arn
    Tags: Optional[TagMap] = None
    Timeout: Optional[Timeout] = None


class RecipeStepList(BaseModel):
    __root__: List[RecipeStep]


class CreateRecipeRequest(BaseModel):
    Description: Optional[RecipeDescription] = None
    Name: RecipeName
    Steps: RecipeStepList
    Tags: Optional[TagMap] = None


class Dataset(BaseModel):
    """
    Represents a dataset that can be processed by DataBrew.
    """

    AccountId: Optional[AccountId] = None
    CreatedBy: Optional[CreatedBy] = None
    CreateDate: Optional[Date] = None
    Name: DatasetName
    Format: Optional[InputFormat] = None
    FormatOptions: Optional[FormatOptions] = None
    Input: Input
    LastModifiedDate: Optional[Date] = None
    LastModifiedBy: Optional[LastModifiedBy] = None
    Source: Optional[Source] = None
    PathOptions: Optional[PathOptions] = None
    Tags: Optional[TagMap] = None
    ResourceArn: Optional[Arn] = None


class DatasetList(BaseModel):
    __root__: List[Dataset]


class Job(BaseModel):
    """
    Represents all of the attributes of a DataBrew job.
    """

    AccountId: Optional[AccountId] = None
    CreatedBy: Optional[CreatedBy] = None
    CreateDate: Optional[Date] = None
    DatasetName: Optional[DatasetName] = None
    EncryptionKeyArn: Optional[EncryptionKeyArn] = None
    EncryptionMode: Optional[EncryptionMode] = None
    Name: JobName
    Type: Optional[JobType] = None
    LastModifiedBy: Optional[LastModifiedBy] = None
    LastModifiedDate: Optional[Date] = None
    LogSubscription: Optional[LogSubscription] = None
    MaxCapacity: Optional[MaxCapacity] = None
    MaxRetries: Optional[MaxRetries] = None
    Outputs: Optional[OutputList] = None
    DataCatalogOutputs: Optional[DataCatalogOutputList] = None
    DatabaseOutputs: Optional[DatabaseOutputList] = None
    ProjectName: Optional[ProjectName] = None
    RecipeReference: Optional[RecipeReference] = None
    ResourceArn: Optional[Arn] = None
    RoleArn: Optional[Arn] = None
    Timeout: Optional[Timeout] = None
    Tags: Optional[TagMap] = None
    JobSample: Optional[JobSample] = None


class JobList(BaseModel):
    __root__: List[Job]


class JobRun(BaseModel):
    """
    Represents one run of a DataBrew job.
    """

    Attempt: Optional[Attempt] = None
    CompletedOn: Optional[Date] = None
    DatasetName: Optional[DatasetName] = None
    ErrorMessage: Optional[JobRunErrorMessage] = None
    ExecutionTime: Optional[ExecutionTime] = None
    JobName: Optional[JobName] = None
    RunId: Optional[JobRunId] = None
    State: Optional[JobRunState] = None
    LogSubscription: Optional[LogSubscription] = None
    LogGroupName: Optional[LogGroupName] = None
    Outputs: Optional[OutputList] = None
    DataCatalogOutputs: Optional[DataCatalogOutputList] = None
    DatabaseOutputs: Optional[DatabaseOutputList] = None
    RecipeReference: Optional[RecipeReference] = None
    StartedBy: Optional[StartedBy] = None
    StartedOn: Optional[Date] = None
    JobSample: Optional[JobSample] = None


class JobRunList(BaseModel):
    __root__: List[JobRun]


class Recipe(BaseModel):
    """
    Represents one or more actions to be performed on a DataBrew dataset.
    """

    CreatedBy: Optional[CreatedBy] = None
    CreateDate: Optional[Date] = None
    LastModifiedBy: Optional[LastModifiedBy] = None
    LastModifiedDate: Optional[Date] = None
    ProjectName: Optional[ProjectName] = None
    PublishedBy: Optional[PublishedBy] = None
    PublishedDate: Optional[Date] = None
    Description: Optional[RecipeDescription] = None
    Name: RecipeName
    ResourceArn: Optional[Arn] = None
    Steps: Optional[RecipeStepList] = None
    Tags: Optional[TagMap] = None
    RecipeVersion: Optional[RecipeVersion] = None


class SendProjectSessionActionRequest(BaseModel):
    Preview: Optional[Preview] = None
    RecipeStep: Optional[RecipeStep] = None
    StepIndex: Optional[StepIndex] = None
    ClientSessionId: Optional[ClientSessionId] = None
    ViewFrame: Optional[ViewFrame] = None


class UpdateDatasetRequest(BaseModel):
    Format: Optional[InputFormat] = None
    FormatOptions: Optional[FormatOptions] = None
    Input: Input
    PathOptions: Optional[PathOptions] = None


class UpdateProfileJobRequest(BaseModel):
    Configuration: Optional[ProfileConfiguration] = None
    EncryptionKeyArn: Optional[EncryptionKeyArn] = None
    EncryptionMode: Optional[EncryptionMode] = None
    LogSubscription: Optional[LogSubscription] = None
    MaxCapacity: Optional[MaxCapacity] = None
    MaxRetries: Optional[MaxRetries] = None
    OutputLocation: S3Location
    RoleArn: Arn
    Timeout: Optional[Timeout] = None
    JobSample: Optional[JobSample] = None


class UpdateRecipeJobRequest(BaseModel):
    EncryptionKeyArn: Optional[EncryptionKeyArn] = None
    EncryptionMode: Optional[EncryptionMode] = None
    LogSubscription: Optional[LogSubscription] = None
    MaxCapacity: Optional[MaxCapacity] = None
    MaxRetries: Optional[MaxRetries] = None
    Outputs: Optional[OutputList] = None
    DataCatalogOutputs: Optional[DataCatalogOutputList] = None
    DatabaseOutputs: Optional[DatabaseOutputList] = None
    RoleArn: Arn
    Timeout: Optional[Timeout] = None


class UpdateRecipeRequest(BaseModel):
    Description: Optional[RecipeDescription] = None
    Steps: Optional[RecipeStepList] = None


class BatchDeleteRecipeVersionResponse(BaseModel):
    Name: RecipeName
    Errors: Optional[RecipeErrorList] = None


class DescribeDatasetResponse(BaseModel):
    CreatedBy: Optional[CreatedBy] = None
    CreateDate: Optional[Date] = None
    Name: DatasetName
    Format: Optional[InputFormat] = None
    FormatOptions: Optional[FormatOptions] = None
    Input: Input
    LastModifiedDate: Optional[Date] = None
    LastModifiedBy: Optional[LastModifiedBy] = None
    Source: Optional[Source] = None
    PathOptions: Optional[PathOptions] = None
    Tags: Optional[TagMap] = None
    ResourceArn: Optional[Arn] = None


class DescribeJobResponse(BaseModel):
    CreateDate: Optional[Date] = None
    CreatedBy: Optional[CreatedBy] = None
    DatasetName: Optional[DatasetName] = None
    EncryptionKeyArn: Optional[EncryptionKeyArn] = None
    EncryptionMode: Optional[EncryptionMode] = None
    Name: JobName
    Type: Optional[JobType] = None
    LastModifiedBy: Optional[LastModifiedBy] = None
    LastModifiedDate: Optional[Date] = None
    LogSubscription: Optional[LogSubscription] = None
    MaxCapacity: Optional[MaxCapacity] = None
    MaxRetries: Optional[MaxRetries] = None
    Outputs: Optional[OutputList] = None
    DataCatalogOutputs: Optional[DataCatalogOutputList] = None
    DatabaseOutputs: Optional[DatabaseOutputList] = None
    ProjectName: Optional[ProjectName] = None
    ProfileConfiguration: Optional[ProfileConfiguration] = None
    RecipeReference: Optional[RecipeReference] = None
    ResourceArn: Optional[Arn] = None
    RoleArn: Optional[Arn] = None
    Tags: Optional[TagMap] = None
    Timeout: Optional[Timeout] = None
    JobSample: Optional[JobSample] = None


class DescribeJobRunResponse(BaseModel):
    Attempt: Optional[Attempt] = None
    CompletedOn: Optional[Date] = None
    DatasetName: Optional[DatasetName] = None
    ErrorMessage: Optional[JobRunErrorMessage] = None
    ExecutionTime: Optional[ExecutionTime] = None
    JobName: JobName
    ProfileConfiguration: Optional[ProfileConfiguration] = None
    RunId: Optional[JobRunId] = None
    State: Optional[JobRunState] = None
    LogSubscription: Optional[LogSubscription] = None
    LogGroupName: Optional[LogGroupName] = None
    Outputs: Optional[OutputList] = None
    DataCatalogOutputs: Optional[DataCatalogOutputList] = None
    DatabaseOutputs: Optional[DatabaseOutputList] = None
    RecipeReference: Optional[RecipeReference] = None
    StartedBy: Optional[StartedBy] = None
    StartedOn: Optional[Date] = None
    JobSample: Optional[JobSample] = None


class DescribeRecipeResponse(BaseModel):
    CreatedBy: Optional[CreatedBy] = None
    CreateDate: Optional[Date] = None
    LastModifiedBy: Optional[LastModifiedBy] = None
    LastModifiedDate: Optional[Date] = None
    ProjectName: Optional[ProjectName] = None
    PublishedBy: Optional[PublishedBy] = None
    PublishedDate: Optional[Date] = None
    Description: Optional[RecipeDescription] = None
    Name: RecipeName
    Steps: Optional[RecipeStepList] = None
    Tags: Optional[TagMap] = None
    ResourceArn: Optional[Arn] = None
    RecipeVersion: Optional[RecipeVersion] = None


class ListDatasetsResponse(BaseModel):
    Datasets: DatasetList
    NextToken: Optional[NextToken] = None


class ListJobRunsResponse(BaseModel):
    JobRuns: JobRunList
    NextToken: Optional[NextToken] = None


class ListJobsResponse(BaseModel):
    Jobs: JobList
    NextToken: Optional[NextToken] = None


class RecipeList(BaseModel):
    __root__: List[Recipe]


class ListRecipeVersionsResponse(BaseModel):
    NextToken: Optional[NextToken] = None
    Recipes: RecipeList


class ListRecipesResponse(BaseModel):
    Recipes: RecipeList
    NextToken: Optional[NextToken] = None