# generated by datamodel-codegen:
#   filename:  openapi.yaml
#   timestamp: 2021-12-31T02:59:08+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Annotated, Any, List, Optional

from pydantic import BaseModel, Extra, Field


class String(BaseModel):
    __root__: Annotated[str, Field(max_length=1024, min_length=1)]


class Blob(BaseModel):
    __root__: Annotated[str, Field(max_length=10000000, min_length=1)]


class MaxOneYearInSeconds(BaseModel):
    __root__: Annotated[int, Field(ge=0.0, le=31622400.0)]


class MaxFifteenMinutesInSeconds(BaseModel):
    __root__: Annotated[int, Field(ge=3.0, le=840.0)]


class MaxSize3008(BaseModel):
    __root__: Annotated[int, Field(ge=960.0, le=3008.0)]


class NullableBoolean(BaseModel):
    __root__: bool


class EnvironmentVariablesMap(BaseModel):
    pass

    class Config:
        extra = Extra.allow


class TagValue(BaseModel):
    __root__: Annotated[str, Field(max_length=256)]


class InternalServerException(BaseModel):
    __root__: Any


class ValidationException(InternalServerException):
    pass


class DeleteCanaryResponse(BaseModel):
    pass


class ResourceNotFoundException(InternalServerException):
    pass


class ConflictException(InternalServerException):
    pass


class StartCanaryResponse(DeleteCanaryResponse):
    pass


class StopCanaryResponse(DeleteCanaryResponse):
    pass


class TagResourceResponse(DeleteCanaryResponse):
    pass


class UntagResourceResponse(DeleteCanaryResponse):
    pass


class TagKey(BaseModel):
    __root__: Annotated[
        str, Field(max_length=128, min_length=1, regex='^(?!aws:)[a-zA-Z+-=._:/]+$')
    ]


class UpdateCanaryResponse(DeleteCanaryResponse):
    pass


class BaseScreenshotConfigIgnoreCoordinate(BaseModel):
    __root__: Annotated[
        str, Field(regex='^(-?\\d{1,5}\\.?\\d{0,2},){3}(-?\\d{1,5}\\.?\\d{0,2}){1}$')
    ]


class UUID(BaseModel):
    __root__: Annotated[
        str,
        Field(regex='^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$'),
    ]


class CanaryName(BaseModel):
    __root__: Annotated[
        str, Field(max_length=21, min_length=1, regex='^[0-9a-z_\\-]+$')
    ]


class CanaryCodeOutput(BaseModel):
    """
    This structure contains information about the canary's Lambda handler and where its code is stored by CloudWatch Synthetics.
    """

    SourceLocationArn: Optional[String] = None
    Handler: Optional[String] = None


class RoleArn(BaseModel):
    __root__: Annotated[
        str,
        Field(
            max_length=2048,
            min_length=1,
            regex='arn:(aws[a-zA-Z-]*)?:iam::\\d{12}:role/?[a-zA-Z_0-9+=,.@\\-_/]+',
        ),
    ]


class CanaryScheduleOutput(BaseModel):
    """
    How long, in seconds, for the canary to continue making regular runs according to the schedule in the <code>Expression</code> value.
    """

    Expression: Optional[String] = None
    DurationInSeconds: Optional[MaxOneYearInSeconds] = None


class CanaryRunConfigOutput(BaseModel):
    """
    A structure that contains information about a canary run.
    """

    TimeoutInSeconds: Optional[MaxFifteenMinutesInSeconds] = None
    MemoryInMB: Optional[MaxSize3008] = None
    ActiveTracing: Optional[NullableBoolean] = None


class MaxSize1024(BaseModel):
    __root__: Annotated[int, Field(ge=1.0, le=1024.0)]


class FunctionArn(BaseModel):
    __root__: Annotated[
        str,
        Field(
            max_length=2048,
            min_length=1,
            regex='arn:(aws[a-zA-Z-]*)?:lambda:[a-z]{2}((-gov)|(-iso(b?)))?-[a-z]+-\\d{1}:\\d{12}:function:[a-zA-Z0-9-_]+(:(\\$LATEST|[a-zA-Z0-9-_]+))?',
        ),
    ]


class TagMap(BaseModel):
    pass

    class Config:
        extra = Extra.allow


class CanaryArn(BaseModel):
    __root__: Annotated[
        str,
        Field(
            max_length=2048,
            min_length=1,
            regex='arn:(aws[a-zA-Z-]*)?:synthetics:[a-z]{2}((-gov)|(-iso(b?)))?-[a-z]+-\\d{1}:\\d{12}:canary:[0-9a-z_\\-]{1,21}',
        ),
    ]


class CanaryCodeInput(BaseModel):
    """
    Use this structure to input your script code for the canary. This structure contains the Lambda handler with the location where the canary should start running the script. If the script is stored in an S3 bucket, the bucket name, key, and version are also included. If the script was passed into the canary directly, the script code is contained in the value of <code>Zipfile</code>.
    """

    S3Bucket: Optional[String] = None
    S3Key: Optional[String] = None
    S3Version: Optional[String] = None
    ZipFile: Optional[Blob] = None
    Handler: String


class CanaryRunConfigInput(BaseModel):
    """
    A structure that contains input information for a canary run.
    """

    TimeoutInSeconds: Optional[MaxFifteenMinutesInSeconds] = None
    MemoryInMB: Optional[MaxSize3008] = None
    ActiveTracing: Optional[NullableBoolean] = None
    EnvironmentVariables: Optional[EnvironmentVariablesMap] = None


class CanaryRunState(Enum):
    RUNNING = 'RUNNING'
    PASSED = 'PASSED'
    FAILED = 'FAILED'


class CanaryRunStateReasonCode(Enum):
    CANARY_FAILURE = 'CANARY_FAILURE'
    EXECUTION_FAILURE = 'EXECUTION_FAILURE'


class Timestamp(BaseModel):
    __root__: datetime


class CanaryScheduleInput(BaseModel):
    """
    This structure specifies how often a canary is to make runs and the date and time when it should stop making runs.
    """

    Expression: String
    DurationInSeconds: Optional[MaxOneYearInSeconds] = None


class CanaryState(Enum):
    CREATING = 'CREATING'
    READY = 'READY'
    STARTING = 'STARTING'
    RUNNING = 'RUNNING'
    UPDATING = 'UPDATING'
    STOPPING = 'STOPPING'
    STOPPED = 'STOPPED'
    ERROR = 'ERROR'
    DELETING = 'DELETING'


class CanaryStateReasonCode(Enum):
    INVALID_PERMISSIONS = 'INVALID_PERMISSIONS'


class DeleteCanaryRequest(BaseModel):
    pass


class Token(BaseModel):
    __root__: Annotated[str, Field(max_length=252, min_length=4)]


class MaxSize100(BaseModel):
    __root__: Annotated[int, Field(ge=1.0, le=100.0)]


class DescribeCanariesLastRunRequest(BaseModel):
    NextToken: Optional[Token] = None
    MaxResults: Optional[MaxSize100] = None


class MaxCanaryResults(BaseModel):
    __root__: Annotated[int, Field(ge=1.0, le=20.0)]


class DescribeCanariesRequest(BaseModel):
    NextToken: Optional[Token] = None
    MaxResults: Optional[MaxCanaryResults] = None


class DescribeRuntimeVersionsRequest(BaseModel):
    NextToken: Optional[Token] = None
    MaxResults: Optional[MaxSize100] = None


class EnvironmentVariableName(BaseModel):
    __root__: Annotated[str, Field(regex='[a-zA-Z]([a-zA-Z0-9_])+')]


class EnvironmentVariableValue(BaseModel):
    __root__: str


class GetCanaryRequest(BaseModel):
    pass


class GetCanaryRunsRequest(BaseModel):
    NextToken: Optional[Token] = None
    MaxResults: Optional[MaxSize100] = None


class ListTagsForResourceRequest(BaseModel):
    pass


class RuntimeVersion(BaseModel):
    """
    This structure contains information about one canary runtime version. For more information about runtime versions, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Library.html"> Canary Runtime Versions</a>.
    """

    VersionName: Optional[String] = None
    Description: Optional[String] = None
    ReleaseDate: Optional[Timestamp] = None
    DeprecationDate: Optional[Timestamp] = None


class SecurityGroupId(EnvironmentVariableValue):
    pass


class StartCanaryRequest(BaseModel):
    pass


class StopCanaryRequest(BaseModel):
    pass


class SubnetId(EnvironmentVariableValue):
    pass


class TagKeyList(BaseModel):
    __root__: Annotated[List[TagKey], Field(max_items=50, min_items=1)]


class TagResourceRequest(BaseModel):
    Tags: TagMap


class UntagResourceRequest(BaseModel):
    pass


class VpcId(EnvironmentVariableValue):
    pass


class SubnetIds(BaseModel):
    __root__: Annotated[List[SubnetId], Field(max_items=16, min_items=0)]


class SecurityGroupIds(BaseModel):
    __root__: Annotated[List[SecurityGroupId], Field(max_items=5, min_items=0)]


class ListTagsForResourceResponse(BaseModel):
    Tags: Optional[TagMap] = None


class BaseScreenshotIgnoreCoordinates(BaseModel):
    __root__: Annotated[
        List[BaseScreenshotConfigIgnoreCoordinate], Field(max_items=20, min_items=0)
    ]


class BaseScreenshot(BaseModel):
    """
    A structure representing a screenshot that is used as a baseline during visual monitoring comparisons made by the canary.
    """

    ScreenshotName: String
    IgnoreCoordinates: Optional[BaseScreenshotIgnoreCoordinates] = None


class CanaryStatus(BaseModel):
    """
    A structure that contains the current state of the canary.
    """

    State: Optional[CanaryState] = None
    StateReason: Optional[String] = None
    StateReasonCode: Optional[CanaryStateReasonCode] = None


class CanaryTimeline(BaseModel):
    """
    This structure contains information about when the canary was created and modified.
    """

    Created: Optional[Timestamp] = None
    LastModified: Optional[Timestamp] = None
    LastStarted: Optional[Timestamp] = None
    LastStopped: Optional[Timestamp] = None


class VpcConfigOutput(BaseModel):
    """
    If this canary is to test an endpoint in a VPC, this structure contains information about the subnets and security groups of the VPC endpoint. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_VPC.html"> Running a Canary in a VPC</a>.
    """

    VpcId: Optional[VpcId] = None
    SubnetIds: Optional[SubnetIds] = None
    SecurityGroupIds: Optional[SecurityGroupIds] = None


class CanaryRunStatus(BaseModel):
    """
    This structure contains the status information about a canary run.
    """

    State: Optional[CanaryRunState] = None
    StateReason: Optional[String] = None
    StateReasonCode: Optional[CanaryRunStateReasonCode] = None


class CanaryRunTimeline(BaseModel):
    """
    This structure contains the start and end times of a single canary run.
    """

    Started: Optional[Timestamp] = None
    Completed: Optional[Timestamp] = None


class VpcConfigInput(BaseModel):
    """
    If this canary is to test an endpoint in a VPC, this structure contains information about the subnets and security groups of the VPC endpoint. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_VPC.html"> Running a Canary in a VPC</a>.
    """

    SubnetIds: Optional[SubnetIds] = None
    SecurityGroupIds: Optional[SecurityGroupIds] = None


class CreateCanaryRequest(BaseModel):
    Name: CanaryName
    Code: CanaryCodeInput
    ArtifactS3Location: String
    ExecutionRoleArn: RoleArn
    Schedule: CanaryScheduleInput
    RunConfig: Optional[CanaryRunConfigInput] = None
    SuccessRetentionPeriodInDays: Optional[MaxSize1024] = None
    FailureRetentionPeriodInDays: Optional[MaxSize1024] = None
    RuntimeVersion: String
    VpcConfig: Optional[VpcConfigInput] = None
    Tags: Optional[TagMap] = None


class RuntimeVersionList(BaseModel):
    __root__: List[RuntimeVersion]


class DescribeRuntimeVersionsResponse(BaseModel):
    RuntimeVersions: Optional[RuntimeVersionList] = None
    NextToken: Optional[Token] = None


class BaseScreenshots(BaseModel):
    __root__: List[BaseScreenshot]


class VisualReferenceOutput(BaseModel):
    """
    <p>If this canary performs visual monitoring by comparing screenshots, this structure contains the ID of the canary run that is used as the baseline for screenshots, and the coordinates of any parts of those screenshots that are ignored during visual monitoring comparison.</p> <p>Visual monitoring is supported only on canaries running the <b>syn-puppeteer-node-3.2</b> runtime or later.</p>
    """

    BaseScreenshots: Optional[BaseScreenshots] = None
    BaseCanaryRunId: Optional[String] = None


class CanaryRun(BaseModel):
    """
    This structure contains the details about one run of one canary.
    """

    Id: Optional[UUID] = None
    Name: Optional[CanaryName] = None
    Status: Optional[CanaryRunStatus] = None
    Timeline: Optional[CanaryRunTimeline] = None
    ArtifactS3Location: Optional[String] = None


class CanaryRuns(BaseModel):
    __root__: List[CanaryRun]


class VisualReferenceInput(BaseModel):
    """
    <p>An object that specifies what screenshots to use as a baseline for visual monitoring by this canary, and optionally the parts of the screenshots to ignore during the visual monitoring comparison.</p> <p>Visual monitoring is supported only on canaries running the <b>syn-puppeteer-node-3.2</b> runtime or later. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Library_SyntheticsLogger_VisualTesting.html"> Visual monitoring</a> and <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Blueprints_VisualTesting.html"> Visual monitoring blueprint</a> </p>
    """

    BaseScreenshots: Optional[BaseScreenshots] = None
    BaseCanaryRunId: String


class UpdateCanaryRequest(BaseModel):
    Code: Optional[CanaryCodeInput] = None
    ExecutionRoleArn: Optional[RoleArn] = None
    RuntimeVersion: Optional[String] = None
    Schedule: Optional[CanaryScheduleInput] = None
    RunConfig: Optional[CanaryRunConfigInput] = None
    SuccessRetentionPeriodInDays: Optional[MaxSize1024] = None
    FailureRetentionPeriodInDays: Optional[MaxSize1024] = None
    VpcConfig: Optional[VpcConfigInput] = None
    VisualReference: Optional[VisualReferenceInput] = None


class GetCanaryRunsResponse(BaseModel):
    CanaryRuns: Optional[CanaryRuns] = None
    NextToken: Optional[Token] = None


class Canary(BaseModel):
    """
    This structure contains all information about one canary in your account.
    """

    Id: Optional[UUID] = None
    Name: Optional[CanaryName] = None
    Code: Optional[CanaryCodeOutput] = None
    ExecutionRoleArn: Optional[RoleArn] = None
    Schedule: Optional[CanaryScheduleOutput] = None
    RunConfig: Optional[CanaryRunConfigOutput] = None
    SuccessRetentionPeriodInDays: Optional[MaxSize1024] = None
    FailureRetentionPeriodInDays: Optional[MaxSize1024] = None
    Status: Optional[CanaryStatus] = None
    Timeline: Optional[CanaryTimeline] = None
    ArtifactS3Location: Optional[String] = None
    EngineArn: Optional[FunctionArn] = None
    RuntimeVersion: Optional[String] = None
    VpcConfig: Optional[VpcConfigOutput] = None
    VisualReference: Optional[VisualReferenceOutput] = None
    Tags: Optional[TagMap] = None


class Canaries(BaseModel):
    __root__: List[Canary]


class CanaryLastRun(BaseModel):
    """
    This structure contains information about the most recent run of a single canary.
    """

    CanaryName: Optional[CanaryName] = None
    LastRun: Optional[CanaryRun] = None


class CanariesLastRun(BaseModel):
    __root__: List[CanaryLastRun]


class CreateCanaryResponse(BaseModel):
    Canary: Optional[Canary] = None


class DescribeCanariesResponse(BaseModel):
    Canaries: Optional[Canaries] = None
    NextToken: Optional[Token] = None


class DescribeCanariesLastRunResponse(BaseModel):
    CanariesLastRun: Optional[CanariesLastRun] = None
    NextToken: Optional[Token] = None


class GetCanaryResponse(CreateCanaryResponse):
    pass
