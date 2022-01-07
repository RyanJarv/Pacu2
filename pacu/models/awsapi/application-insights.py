# generated by datamodel-codegen:
#   filename:  openapi.yaml
#   timestamp: 2021-12-31T02:45:06+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Annotated, Any, List, Optional

from pydantic import BaseModel, Extra, Field


class ResourceInUseException(BaseModel):
    __root__: Any


class ResourceNotFoundException(ResourceInUseException):
    pass


class ValidationException(ResourceInUseException):
    pass


class InternalServerException(ResourceInUseException):
    pass


class TagsAlreadyExistException(ResourceInUseException):
    pass


class AccessDeniedException(ResourceInUseException):
    pass


class CreateComponentResponse(BaseModel):
    pass


class DeleteApplicationResponse(CreateComponentResponse):
    pass


class BadRequestException(ResourceInUseException):
    pass


class DeleteComponentResponse(CreateComponentResponse):
    pass


class DeleteLogPatternResponse(CreateComponentResponse):
    pass


class TagResourceResponse(CreateComponentResponse):
    pass


class TooManyTagsException(ResourceInUseException):
    pass


class UntagResourceResponse(CreateComponentResponse):
    pass


class UpdateComponentResponse(CreateComponentResponse):
    pass


class UpdateComponentConfigurationResponse(CreateComponentResponse):
    pass


class AffectedResource(BaseModel):
    __root__: str


class AmazonResourceName(BaseModel):
    __root__: Annotated[
        str,
        Field(
            max_length=1011,
            min_length=1,
            regex='^arn:aws(-\\w+)*:[\\w\\d-]+:([\\w\\d-]*)?:[\\w\\d_-]*([:/].+)*$',
        ),
    ]


class ComponentName(BaseModel):
    __root__: Annotated[
        str,
        Field(
            max_length=1011,
            min_length=1,
            regex='(?:^[\\d\\w\\-_\\.+]*$)|(?:^arn:aws(-\\w+)*:[\\w\\d-]+:([\\w\\d-]*)?:[\\w\\d_-]*([:/].+)*$)',
        ),
    ]


class Remarks(AffectedResource):
    pass


class ResourceType(BaseModel):
    __root__: Annotated[str, Field(max_length=50, min_length=1, regex='[0-9a-zA-Z:_]*')]


class OsType(Enum):
    WINDOWS = 'WINDOWS'
    LINUX = 'LINUX'


class Tier(Enum):
    CUSTOM = 'CUSTOM'
    DEFAULT = 'DEFAULT'
    DOT_NET_CORE = 'DOT_NET_CORE'
    DOT_NET_WORKER = 'DOT_NET_WORKER'
    DOT_NET_WEB_TIER = 'DOT_NET_WEB_TIER'
    DOT_NET_WEB = 'DOT_NET_WEB'
    SQL_SERVER = 'SQL_SERVER'
    SQL_SERVER_ALWAYSON_AVAILABILITY_GROUP = 'SQL_SERVER_ALWAYSON_AVAILABILITY_GROUP'
    MYSQL = 'MYSQL'
    POSTGRESQL = 'POSTGRESQL'
    JAVA_JMX = 'JAVA_JMX'
    ORACLE = 'ORACLE'


class Monitor(BaseModel):
    __root__: bool


class DetectedWorkload(BaseModel):
    pass

    class Config:
        extra = Extra.allow


class ApplicationComponent(BaseModel):
    """
    Describes a standalone resource or similarly grouped resources that the application is made up of.
    """

    ComponentName: Optional[ComponentName] = None
    ComponentRemarks: Optional[Remarks] = None
    ResourceType: Optional[ResourceType] = None
    OsType: Optional[OsType] = None
    Tier: Optional[Tier] = None
    Monitor: Optional[Monitor] = None
    DetectedWorkload: Optional[DetectedWorkload] = None


class ApplicationComponentList(BaseModel):
    __root__: List[ApplicationComponent]


class ResourceGroupName(BaseModel):
    __root__: Annotated[
        str, Field(max_length=256, min_length=1, regex='[a-zA-Z0-9\\.\\-_]*')
    ]


class LifeCycle(AffectedResource):
    pass


class OpsItemSNSTopicArn(BaseModel):
    __root__: Annotated[
        str,
        Field(
            max_length=300,
            min_length=20,
            regex='^arn:aws(-\\w+)*:[\\w\\d-]+:([\\w\\d-]*)?:[\\w\\d_-]*([:/].+)*$',
        ),
    ]


class OpsCenterEnabled(Monitor):
    pass


class CWEMonitorEnabled(Monitor):
    pass


class ApplicationInfo(BaseModel):
    """
    Describes the status of the application.
    """

    ResourceGroupName: Optional[ResourceGroupName] = None
    LifeCycle: Optional[LifeCycle] = None
    OpsItemSNSTopicArn: Optional[OpsItemSNSTopicArn] = None
    OpsCenterEnabled: Optional[OpsCenterEnabled] = None
    CWEMonitorEnabled: Optional[CWEMonitorEnabled] = None
    Remarks: Optional[Remarks] = None


class ApplicationInfoList(BaseModel):
    __root__: List[ApplicationInfo]


class CloudWatchEventDetailType(AffectedResource):
    pass


class CloudWatchEventId(AffectedResource):
    pass


class CloudWatchEventSource(Enum):
    EC2 = 'EC2'
    CODE_DEPLOY = 'CODE_DEPLOY'
    HEALTH = 'HEALTH'
    RDS = 'RDS'


class CodeDeployApplication(AffectedResource):
    pass


class CodeDeployDeploymentGroup(AffectedResource):
    pass


class CodeDeployDeploymentId(AffectedResource):
    pass


class CodeDeployInstanceGroupId(AffectedResource):
    pass


class CodeDeployState(AffectedResource):
    pass


class ComponentConfiguration(BaseModel):
    __root__: Annotated[str, Field(max_length=10000, min_length=1, regex='[\\S\\s]+')]


class ConfigurationEventMonitoredResourceARN(AffectedResource):
    pass


class ConfigurationEventStatus(Enum):
    INFO = 'INFO'
    WARN = 'WARN'
    ERROR = 'ERROR'


class ConfigurationEventResourceType(Enum):
    CLOUDWATCH_ALARM = 'CLOUDWATCH_ALARM'
    CLOUDWATCH_LOG = 'CLOUDWATCH_LOG'
    CLOUDFORMATION = 'CLOUDFORMATION'
    SSM_ASSOCIATION = 'SSM_ASSOCIATION'


class ConfigurationEventTime(BaseModel):
    __root__: datetime


class ConfigurationEventDetail(AffectedResource):
    pass


class ConfigurationEventResourceName(AffectedResource):
    pass


class ConfigurationEvent(BaseModel):
    """
    The event information.
    """

    MonitoredResourceARN: Optional[ConfigurationEventMonitoredResourceARN] = None
    EventStatus: Optional[ConfigurationEventStatus] = None
    EventResourceType: Optional[ConfigurationEventResourceType] = None
    EventTime: Optional[ConfigurationEventTime] = None
    EventDetail: Optional[ConfigurationEventDetail] = None
    EventResourceName: Optional[ConfigurationEventResourceName] = None


class ConfigurationEventList(BaseModel):
    __root__: List[ConfigurationEvent]


class CustomComponentName(BaseModel):
    __root__: Annotated[
        str, Field(max_length=128, min_length=1, regex='^[\\d\\w\\-_\\.+]*$')
    ]


class LogPatternSetName(BaseModel):
    __root__: Annotated[
        str, Field(max_length=30, min_length=1, regex='[a-zA-Z0-9\\.\\-_]*')
    ]


class LogPatternName(BaseModel):
    __root__: Annotated[
        str, Field(max_length=50, min_length=1, regex='[a-zA-Z0-9\\.\\-_]*')
    ]


class LogPatternRegex(BaseModel):
    __root__: Annotated[str, Field(max_length=50, min_length=1, regex='[\\S\\s]+')]


class LogPatternRank(BaseModel):
    __root__: int


class LogPattern(BaseModel):
    """
    An object that defines the log patterns that belongs to a <code>LogPatternSet</code>.
    """

    PatternSetName: Optional[LogPatternSetName] = None
    PatternName: Optional[LogPatternName] = None
    Pattern: Optional[LogPatternRegex] = None
    Rank: Optional[LogPatternRank] = None


class ObservationId(BaseModel):
    __root__: Annotated[
        str,
        Field(
            max_length=38,
            min_length=38,
            regex='o-[0-9a-fA-F]{8}\\-[0-9a-fA-F]{4}\\-[0-9a-fA-F]{4}\\-[0-9a-fA-F]{4}\\-[0-9a-fA-F]{12}',
        ),
    ]


class ProblemId(BaseModel):
    __root__: Annotated[
        str,
        Field(
            max_length=38,
            min_length=38,
            regex='p-[0-9a-fA-F]{8}\\-[0-9a-fA-F]{4}\\-[0-9a-fA-F]{4}\\-[0-9a-fA-F]{4}\\-[0-9a-fA-F]{12}',
        ),
    ]


class WorkloadMetaData(BaseModel):
    pass

    class Config:
        extra = Extra.allow


class EbsCause(AffectedResource):
    pass


class EbsEvent(AffectedResource):
    pass


class EbsRequestId(AffectedResource):
    pass


class EbsResult(AffectedResource):
    pass


class Ec2State(AffectedResource):
    pass


class EndTime(ConfigurationEventTime):
    pass


class FeedbackValue(Enum):
    NOT_SPECIFIED = 'NOT_SPECIFIED'
    USEFUL = 'USEFUL'
    NOT_USEFUL = 'NOT_USEFUL'


class Feedback(BaseModel):
    pass

    class Config:
        extra = Extra.allow


class FeedbackKey(Enum):
    INSIGHTS_FEEDBACK = 'INSIGHTS_FEEDBACK'


class HealthEventArn(AffectedResource):
    pass


class HealthEventDescription(AffectedResource):
    pass


class HealthEventTypeCategory(AffectedResource):
    pass


class HealthEventTypeCode(AffectedResource):
    pass


class HealthService(AffectedResource):
    pass


class Insights(AffectedResource):
    pass


class LineTime(ConfigurationEventTime):
    pass


class MaxEntities(BaseModel):
    __root__: Annotated[int, Field(ge=1.0, le=40.0)]


class PaginationToken(BaseModel):
    __root__: Annotated[str, Field(max_length=1024, min_length=1, regex='.+')]


class StartTime(ConfigurationEventTime):
    pass


class LogPatternSetList(BaseModel):
    __root__: List[LogPatternSetName]


class LogPatternList(BaseModel):
    __root__: List[LogPattern]


class LogFilter(Enum):
    ERROR = 'ERROR'
    WARN = 'WARN'
    INFO = 'INFO'


class LogGroup(AffectedResource):
    pass


class LogText(AffectedResource):
    pass


class MetaDataKey(AffectedResource):
    pass


class MetaDataValue(AffectedResource):
    pass


class MetricName(AffectedResource):
    pass


class MetricNamespace(AffectedResource):
    pass


class SourceType(AffectedResource):
    pass


class SourceARN(AffectedResource):
    pass


class Unit(AffectedResource):
    pass


class Value(BaseModel):
    __root__: float


class RdsEventCategories(AffectedResource):
    pass


class RdsEventMessage(AffectedResource):
    pass


class S3EventName(AffectedResource):
    pass


class StatesExecutionArn(AffectedResource):
    pass


class StatesArn(AffectedResource):
    pass


class StatesStatus(AffectedResource):
    pass


class StatesInput(AffectedResource):
    pass


class XRayFaultPercent(LogPatternRank):
    pass


class XRayThrottlePercent(LogPatternRank):
    pass


class XRayErrorPercent(LogPatternRank):
    pass


class XRayRequestCount(LogPatternRank):
    pass


class XRayRequestAverageLatency(LogPatternRank):
    pass


class XRayNodeName(AffectedResource):
    pass


class XRayNodeType(AffectedResource):
    pass


class Title(AffectedResource):
    pass


class Status(Enum):
    IGNORE = 'IGNORE'
    RESOLVED = 'RESOLVED'
    PENDING = 'PENDING'


class SeverityLevel(Enum):
    Low = 'Low'
    Medium = 'Medium'
    High = 'High'


class RemoveSNSTopic(Monitor):
    pass


class ResourceARN(AmazonResourceName):
    pass


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
    <p>An object that defines the tags associated with an application. A <i>tag</i> is a label that you optionally define and associate with an application. Tags can help you categorize and manage resources in different ways, such as by purpose, owner, environment, or other criteria.</p> <p>Each tag consists of a required <i>tag key</i> and an associated <i>tag value</i>, both of which you define. A tag key is a general label that acts as a category for a more specific tag value. A tag value acts as a descriptor within a tag key. A tag key can contain as many as 128 characters. A tag value can contain as many as 256 characters. The characters can be Unicode letters, digits, white space, or one of the following symbols: _ . : / = + -. The following additional restrictions apply to tags:</p> <ul> <li> <p>Tag keys and values are case sensitive.</p> </li> <li> <p>For each associated resource, each tag key must be unique and it can have only one value.</p> </li> <li> <p>The <code>aws:</code> prefix is reserved for use by AWS; you can’t use it in any tag keys or values that you define. In addition, you can't edit or remove tag keys or values that use this prefix. </p> </li> </ul>
    """

    Key: TagKey
    Value: TagValue


class TagKeyList(BaseModel):
    __root__: Annotated[List[TagKey], Field(max_items=200, min_items=0)]


class CreateApplicationResponse(BaseModel):
    ApplicationInfo: Optional[ApplicationInfo] = None


class CreateLogPatternResponse(BaseModel):
    LogPattern: Optional[LogPattern] = None
    ResourceGroupName: Optional[ResourceGroupName] = None


class CreateLogPatternRequest(BaseModel):
    ResourceGroupName: ResourceGroupName
    PatternSetName: LogPatternSetName
    PatternName: LogPatternName
    Pattern: LogPatternRegex
    Rank: LogPatternRank


class DeleteApplicationRequest(BaseModel):
    ResourceGroupName: ResourceGroupName


class DeleteComponentRequest(BaseModel):
    ResourceGroupName: ResourceGroupName
    ComponentName: CustomComponentName


class DeleteLogPatternRequest(BaseModel):
    ResourceGroupName: ResourceGroupName
    PatternSetName: LogPatternSetName
    PatternName: LogPatternName


class DescribeApplicationResponse(CreateApplicationResponse):
    pass


class DescribeApplicationRequest(BaseModel):
    ResourceGroupName: ResourceGroupName


class DescribeComponentRequest(BaseModel):
    ResourceGroupName: ResourceGroupName
    ComponentName: ComponentName


class DescribeComponentConfigurationResponse(BaseModel):
    Monitor: Optional[Monitor] = None
    Tier: Optional[Tier] = None
    ComponentConfiguration: Optional[ComponentConfiguration] = None


class DescribeComponentConfigurationRequest(BaseModel):
    ResourceGroupName: ResourceGroupName
    ComponentName: ComponentName


class DescribeComponentConfigurationRecommendationResponse(BaseModel):
    ComponentConfiguration: Optional[ComponentConfiguration] = None


class DescribeComponentConfigurationRecommendationRequest(BaseModel):
    ResourceGroupName: ResourceGroupName
    ComponentName: ComponentName
    Tier: Tier


class DescribeLogPatternResponse(BaseModel):
    ResourceGroupName: Optional[ResourceGroupName] = None
    LogPattern: Optional[LogPattern] = None


class DescribeLogPatternRequest(BaseModel):
    ResourceGroupName: ResourceGroupName
    PatternSetName: LogPatternSetName
    PatternName: LogPatternName


class DescribeObservationRequest(BaseModel):
    ObservationId: ObservationId


class DescribeProblemRequest(BaseModel):
    ProblemId: ProblemId


class DescribeProblemObservationsRequest(BaseModel):
    ProblemId: ProblemId


class ListApplicationsResponse(BaseModel):
    ApplicationInfoList: Optional[ApplicationInfoList] = None
    NextToken: Optional[PaginationToken] = None


class ListApplicationsRequest(BaseModel):
    MaxResults: Optional[MaxEntities] = None
    NextToken: Optional[PaginationToken] = None


class ListComponentsResponse(BaseModel):
    ApplicationComponentList: Optional[ApplicationComponentList] = None
    NextToken: Optional[PaginationToken] = None


class ListComponentsRequest(BaseModel):
    ResourceGroupName: ResourceGroupName
    MaxResults: Optional[MaxEntities] = None
    NextToken: Optional[PaginationToken] = None


class ListConfigurationHistoryResponse(BaseModel):
    EventList: Optional[ConfigurationEventList] = None
    NextToken: Optional[PaginationToken] = None


class ListConfigurationHistoryRequest(BaseModel):
    ResourceGroupName: Optional[ResourceGroupName] = None
    StartTime: Optional[StartTime] = None
    EndTime: Optional[EndTime] = None
    EventStatus: Optional[ConfigurationEventStatus] = None
    MaxResults: Optional[MaxEntities] = None
    NextToken: Optional[PaginationToken] = None


class ListLogPatternSetsResponse(BaseModel):
    ResourceGroupName: Optional[ResourceGroupName] = None
    LogPatternSets: Optional[LogPatternSetList] = None
    NextToken: Optional[PaginationToken] = None


class ListLogPatternSetsRequest(BaseModel):
    ResourceGroupName: ResourceGroupName
    MaxResults: Optional[MaxEntities] = None
    NextToken: Optional[PaginationToken] = None


class ListLogPatternsResponse(BaseModel):
    ResourceGroupName: Optional[ResourceGroupName] = None
    LogPatterns: Optional[LogPatternList] = None
    NextToken: Optional[PaginationToken] = None


class ListLogPatternsRequest(BaseModel):
    ResourceGroupName: ResourceGroupName
    PatternSetName: Optional[LogPatternSetName] = None
    MaxResults: Optional[MaxEntities] = None
    NextToken: Optional[PaginationToken] = None


class ListProblemsRequest(BaseModel):
    ResourceGroupName: Optional[ResourceGroupName] = None
    StartTime: Optional[StartTime] = None
    EndTime: Optional[EndTime] = None
    MaxResults: Optional[MaxEntities] = None
    NextToken: Optional[PaginationToken] = None


class ListTagsForResourceRequest(BaseModel):
    ResourceARN: AmazonResourceName


class UntagResourceRequest(BaseModel):
    ResourceARN: AmazonResourceName
    TagKeys: TagKeyList


class UpdateApplicationResponse(CreateApplicationResponse):
    pass


class UpdateApplicationRequest(BaseModel):
    ResourceGroupName: ResourceGroupName
    OpsCenterEnabled: Optional[OpsCenterEnabled] = None
    CWEMonitorEnabled: Optional[CWEMonitorEnabled] = None
    OpsItemSNSTopicArn: Optional[OpsItemSNSTopicArn] = None
    RemoveSNSTopic: Optional[RemoveSNSTopic] = None


class UpdateComponentConfigurationRequest(BaseModel):
    ResourceGroupName: ResourceGroupName
    ComponentName: ComponentName
    Monitor: Optional[Monitor] = None
    Tier: Optional[Tier] = None
    ComponentConfiguration: Optional[ComponentConfiguration] = None


class UpdateLogPatternResponse(DescribeLogPatternResponse):
    pass


class UpdateLogPatternRequest(BaseModel):
    ResourceGroupName: ResourceGroupName
    PatternSetName: LogPatternSetName
    PatternName: LogPatternName
    Pattern: Optional[LogPatternRegex] = None
    Rank: Optional[LogPatternRank] = None


class TagList(BaseModel):
    __root__: Annotated[List[Tag], Field(max_items=200, min_items=0)]


class ResourceList(BaseModel):
    __root__: List[ResourceARN]


class Observation(BaseModel):
    """
    Describes an anomaly or error with the application.
    """

    Id: Optional[ObservationId] = None
    StartTime: Optional[StartTime] = None
    EndTime: Optional[EndTime] = None
    SourceType: Optional[SourceType] = None
    SourceARN: Optional[SourceARN] = None
    LogGroup: Optional[LogGroup] = None
    LineTime: Optional[LineTime] = None
    LogText: Optional[LogText] = None
    LogFilter: Optional[LogFilter] = None
    MetricNamespace: Optional[MetricNamespace] = None
    MetricName: Optional[MetricName] = None
    Unit: Optional[Unit] = None
    Value: Optional[Value] = None
    CloudWatchEventId: Optional[CloudWatchEventId] = None
    CloudWatchEventSource: Optional[CloudWatchEventSource] = None
    CloudWatchEventDetailType: Optional[CloudWatchEventDetailType] = None
    HealthEventArn: Optional[HealthEventArn] = None
    HealthService: Optional[HealthService] = None
    HealthEventTypeCode: Optional[HealthEventTypeCode] = None
    HealthEventTypeCategory: Optional[HealthEventTypeCategory] = None
    HealthEventDescription: Optional[HealthEventDescription] = None
    CodeDeployDeploymentId: Optional[CodeDeployDeploymentId] = None
    CodeDeployDeploymentGroup: Optional[CodeDeployDeploymentGroup] = None
    CodeDeployState: Optional[CodeDeployState] = None
    CodeDeployApplication: Optional[CodeDeployApplication] = None
    CodeDeployInstanceGroupId: Optional[CodeDeployInstanceGroupId] = None
    Ec2State: Optional[Ec2State] = None
    RdsEventCategories: Optional[RdsEventCategories] = None
    RdsEventMessage: Optional[RdsEventMessage] = None
    S3EventName: Optional[S3EventName] = None
    StatesExecutionArn: Optional[StatesExecutionArn] = None
    StatesArn: Optional[StatesArn] = None
    StatesStatus: Optional[StatesStatus] = None
    StatesInput: Optional[StatesInput] = None
    EbsEvent: Optional[EbsEvent] = None
    EbsResult: Optional[EbsResult] = None
    EbsCause: Optional[EbsCause] = None
    EbsRequestId: Optional[EbsRequestId] = None
    XRayFaultPercent: Optional[XRayFaultPercent] = None
    XRayThrottlePercent: Optional[XRayThrottlePercent] = None
    XRayErrorPercent: Optional[XRayErrorPercent] = None
    XRayRequestCount: Optional[XRayRequestCount] = None
    XRayRequestAverageLatency: Optional[XRayRequestAverageLatency] = None
    XRayNodeName: Optional[XRayNodeName] = None
    XRayNodeType: Optional[XRayNodeType] = None


class Problem(BaseModel):
    """
    Describes a problem that is detected by correlating observations.
    """

    Id: Optional[ProblemId] = None
    Title: Optional[Title] = None
    Insights: Optional[Insights] = None
    Status: Optional[Status] = None
    AffectedResource: Optional[AffectedResource] = None
    StartTime: Optional[StartTime] = None
    EndTime: Optional[EndTime] = None
    SeverityLevel: Optional[SeverityLevel] = None
    ResourceGroupName: Optional[ResourceGroupName] = None
    Feedback: Optional[Feedback] = None


class ProblemList(BaseModel):
    __root__: List[Problem]


class ObservationList(BaseModel):
    __root__: List[Observation]


class CreateApplicationRequest(BaseModel):
    ResourceGroupName: ResourceGroupName
    OpsCenterEnabled: Optional[OpsCenterEnabled] = None
    CWEMonitorEnabled: Optional[CWEMonitorEnabled] = None
    OpsItemSNSTopicArn: Optional[OpsItemSNSTopicArn] = None
    Tags: Optional[TagList] = None


class CreateComponentRequest(BaseModel):
    ResourceGroupName: ResourceGroupName
    ComponentName: CustomComponentName
    ResourceList: ResourceList


class DescribeComponentResponse(BaseModel):
    ApplicationComponent: Optional[ApplicationComponent] = None
    ResourceList: Optional[ResourceList] = None


class DescribeObservationResponse(BaseModel):
    Observation: Optional[Observation] = None


class DescribeProblemResponse(BaseModel):
    Problem: Optional[Problem] = None


class ListProblemsResponse(BaseModel):
    ProblemList: Optional[ProblemList] = None
    NextToken: Optional[PaginationToken] = None


class ListTagsForResourceResponse(BaseModel):
    Tags: Optional[TagList] = None


class TagResourceRequest(BaseModel):
    ResourceARN: AmazonResourceName
    Tags: TagList


class UpdateComponentRequest(BaseModel):
    ResourceGroupName: ResourceGroupName
    ComponentName: CustomComponentName
    NewComponentName: Optional[CustomComponentName] = None
    ResourceList: Optional[ResourceList] = None


class RelatedObservations(BaseModel):
    """
    Describes observations related to the problem.
    """

    ObservationList: Optional[ObservationList] = None


class DescribeProblemObservationsResponse(BaseModel):
    RelatedObservations: Optional[RelatedObservations] = None
