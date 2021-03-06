# generated by datamodel-codegen:
#   filename:  openapi.yaml
#   timestamp: 2021-12-31T02:58:18+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Annotated, Any, List, Optional

from pydantic import BaseModel, Extra, Field


class InvalidInput(BaseModel):
    __root__: Any


class NamespaceAlreadyExists(InvalidInput):
    pass


class ResourceLimitExceeded(InvalidInput):
    pass


class DuplicateRequest(InvalidInput):
    pass


class TooManyTagsException(InvalidInput):
    pass


class NamespaceNotFound(InvalidInput):
    pass


class ServiceAlreadyExists(InvalidInput):
    pass


class ResourceInUse(InvalidInput):
    pass


class DeleteServiceResponse(BaseModel):
    pass


class ServiceNotFound(InvalidInput):
    pass


class InstanceNotFound(InvalidInput):
    pass


class RequestLimitExceeded(InvalidInput):
    pass


class OperationNotFound(InvalidInput):
    pass


class ResourceNotFoundException(InvalidInput):
    pass


class TagResourceResponse(DeleteServiceResponse):
    pass


class UntagResourceResponse(DeleteServiceResponse):
    pass


class CustomHealthNotFound(InvalidInput):
    pass


class AmazonResourceName(BaseModel):
    __root__: Annotated[str, Field(max_length=1011, min_length=1)]


class Arn(BaseModel):
    __root__: Annotated[str, Field(max_length=255)]


class AttrKey(BaseModel):
    __root__: Annotated[str, Field(max_length=255, regex='^[a-zA-Z0-9!-~]+$')]


class AttrValue(BaseModel):
    __root__: Annotated[
        str,
        Field(
            max_length=1024,
            regex='^([a-zA-Z0-9!-~][ \\ta-zA-Z0-9!-~]*){0,1}[a-zA-Z0-9!-~]{0,1}$',
        ),
    ]


class Attributes(BaseModel):
    pass

    class Config:
        extra = Extra.allow


class Code(BaseModel):
    __root__: str


class NamespaceNameHttp(BaseModel):
    __root__: Annotated[str, Field(max_length=1024, regex='^[!-~]{1,1024}$')]


class ResourceId(BaseModel):
    __root__: Annotated[str, Field(max_length=64)]


class ResourceDescription(BaseModel):
    __root__: Annotated[str, Field(max_length=1024)]


class OperationId(Arn):
    pass


class NamespaceNamePrivate(NamespaceNameHttp):
    pass


class NamespaceNamePublic(BaseModel):
    __root__: Annotated[
        str,
        Field(
            max_length=1024,
            regex='^([a-zA-Z0-9]([a-zA-Z0-9\\-]{0,61}[a-zA-Z0-9])?\\.)+[a-zA-Z0-9]([a-zA-Z0-9\\-]{0,61}[a-zA-Z0-9])?$',
        ),
    ]


class ServiceName(BaseModel):
    __root__: Annotated[
        str,
        Field(
            regex='((?=^.{1,127}$)^([a-zA-Z0-9_][a-zA-Z0-9-_]{0,61}[a-zA-Z0-9_]|[a-zA-Z0-9])(\\.([a-zA-Z0-9_][a-zA-Z0-9-_]{0,61}[a-zA-Z0-9_]|[a-zA-Z0-9]))*$)|(^\\.$)'
        ),
    ]


class ServiceTypeOption(Enum):
    HTTP = 'HTTP'


class CustomHealthStatus(Enum):
    HEALTHY = 'HEALTHY'
    UNHEALTHY = 'UNHEALTHY'


class NamespaceName(ResourceDescription):
    pass


class DiscoverMaxResults(BaseModel):
    __root__: Annotated[int, Field(ge=1.0, le=1000.0)]


class HealthStatusFilter(Enum):
    HEALTHY = 'HEALTHY'
    UNHEALTHY = 'UNHEALTHY'
    ALL = 'ALL'
    HEALTHY_OR_ELSE_ALL = 'HEALTHY_OR_ELSE_ALL'


class RoutingPolicy(Enum):
    MULTIVALUE = 'MULTIVALUE'
    WEIGHTED = 'WEIGHTED'


class RecordType(Enum):
    SRV = 'SRV'
    A = 'A'
    AAAA = 'AAAA'
    CNAME = 'CNAME'


class RecordTTL(BaseModel):
    __root__: Annotated[int, Field(ge=0.0, le=2147483647.0)]


class DnsRecord(BaseModel):
    """
    A complex type that contains information about the Route 53 DNS records that you want Cloud Map to create when you register an instance.
    """

    Type: RecordType
    TTL: RecordTTL


class FailureThreshold(BaseModel):
    __root__: Annotated[int, Field(ge=1.0, le=10.0)]


class FilterCondition(Enum):
    EQ = 'EQ'
    IN = 'IN'
    BETWEEN = 'BETWEEN'


class FilterValue(BaseModel):
    __root__: Annotated[str, Field(max_length=255, min_length=1)]


class FilterValues(BaseModel):
    __root__: List[FilterValue]


class Instance(BaseModel):
    """
    A complex type that contains information about an instance that Cloud Map creates when you submit a <code>RegisterInstance</code> request.
    """

    Id: ResourceId
    CreatorRequestId: Optional[ResourceId] = None
    Attributes: Optional[Attributes] = None


class InstanceIdList(BaseModel):
    __root__: Annotated[List[ResourceId], Field(min_items=1)]


class MaxResults(BaseModel):
    __root__: Annotated[int, Field(ge=1.0, le=100.0)]


class NextToken(BaseModel):
    __root__: Annotated[str, Field(max_length=4096)]


class InstanceHealthStatusMap(BaseModel):
    pass

    class Config:
        extra = Extra.allow


class HealthCheckType(Enum):
    HTTP = 'HTTP'
    HTTPS = 'HTTPS'
    TCP = 'TCP'


class ResourcePath(Arn):
    pass


class HealthStatus(Enum):
    HEALTHY = 'HEALTHY'
    UNHEALTHY = 'UNHEALTHY'
    UNKNOWN = 'UNKNOWN'


class HttpInstanceSummary(BaseModel):
    """
    In a response to a <a href="https://docs.aws.amazon.com/cloud-map/latest/api/API_DiscoverInstances.html">DiscoverInstances</a> request, <code>HttpInstanceSummary</code> contains information about one instance that matches the values that you specified in the request.
    """

    InstanceId: Optional[ResourceId] = None
    NamespaceName: Optional[NamespaceNameHttp] = None
    ServiceName: Optional[ServiceName] = None
    HealthStatus: Optional[HealthStatus] = None
    Attributes: Optional[Attributes] = None


class HttpNamespaceChange(BaseModel):
    """
    Updated properties for the HTTP namespace.
    """

    Description: ResourceDescription


class HttpProperties(BaseModel):
    """
    A complex type that contains the name of an HTTP namespace.
    """

    HttpName: Optional[NamespaceName] = None


class InstanceId(BaseModel):
    __root__: Annotated[str, Field(max_length=64, regex='^[0-9a-zA-Z_/:.@-]+$')]


class InstanceSummary(BaseModel):
    """
    A complex type that contains information about the instances that you registered by using a specified service.
    """

    Id: Optional[ResourceId] = None
    Attributes: Optional[Attributes] = None


class InstanceSummaryList(BaseModel):
    __root__: List[InstanceSummary]


class Message(Code):
    pass


class NamespaceType(Enum):
    DNS_PUBLIC = 'DNS_PUBLIC'
    DNS_PRIVATE = 'DNS_PRIVATE'
    HTTP = 'HTTP'


class ResourceCount(BaseModel):
    __root__: int


class Timestamp(BaseModel):
    __root__: datetime


class NamespaceFilterName(Enum):
    TYPE = 'TYPE'


class NamespaceFilter(BaseModel):
    """
    A complex type that identifies the namespaces that you want to list. You can choose to list public or private namespaces.
    """

    Name: NamespaceFilterName
    Values: FilterValues
    Condition: Optional[FilterCondition] = None


class OperationType(Enum):
    CREATE_NAMESPACE = 'CREATE_NAMESPACE'
    DELETE_NAMESPACE = 'DELETE_NAMESPACE'
    UPDATE_NAMESPACE = 'UPDATE_NAMESPACE'
    UPDATE_SERVICE = 'UPDATE_SERVICE'
    REGISTER_INSTANCE = 'REGISTER_INSTANCE'
    DEREGISTER_INSTANCE = 'DEREGISTER_INSTANCE'


class OperationStatus(Enum):
    SUBMITTED = 'SUBMITTED'
    PENDING = 'PENDING'
    SUCCESS = 'SUCCESS'
    FAIL = 'FAIL'


class OperationTargetsMap(BaseModel):
    pass

    class Config:
        extra = Extra.allow


class OperationFilterName(Enum):
    NAMESPACE_ID = 'NAMESPACE_ID'
    SERVICE_ID = 'SERVICE_ID'
    STATUS = 'STATUS'
    TYPE = 'TYPE'
    UPDATE_DATE = 'UPDATE_DATE'


class OperationFilter(BaseModel):
    """
    A complex type that lets you select the operations that you want to list.
    """

    Name: OperationFilterName
    Values: FilterValues
    Condition: Optional[FilterCondition] = None


class OperationSummary(BaseModel):
    """
    A complex type that contains information about an operation that matches the criteria that you specified in a <a href="https://docs.aws.amazon.com/cloud-map/latest/api/API_ListOperations.html">ListOperations</a> request.
    """

    Id: Optional[OperationId] = None
    Status: Optional[OperationStatus] = None


class OperationTargetType(Enum):
    NAMESPACE = 'NAMESPACE'
    SERVICE = 'SERVICE'
    INSTANCE = 'INSTANCE'


class SOAChange(BaseModel):
    """
    Updated Start of Authority (SOA) properties for a public or private DNS namespace.
    """

    TTL: RecordTTL


class PublicDnsPropertiesMutableChange(BaseModel):
    """
    Updated DNS properties for the public DNS namespace.
    """

    SOA: SOAChange


class ServiceType(Enum):
    HTTP = 'HTTP'
    DNS_HTTP = 'DNS_HTTP'
    DNS = 'DNS'


class ServiceFilterName(Enum):
    NAMESPACE_ID = 'NAMESPACE_ID'


class ServiceFilter(BaseModel):
    """
    A complex type that lets you specify the namespaces that you want to list services for.
    """

    Name: ServiceFilterName
    Values: FilterValues
    Condition: Optional[FilterCondition] = None


class TagKey(BaseModel):
    __root__: Annotated[str, Field(max_length=128, min_length=1)]


class TagValue(BaseModel):
    __root__: Annotated[str, Field(max_length=256, min_length=0)]


class Tag(BaseModel):
    """
    A custom key-value pair that's associated with a resource.
    """

    Key: TagKey
    Value: TagValue


class TagKeyList(BaseModel):
    __root__: Annotated[List[TagKey], Field(max_items=200, min_items=0)]


class CreateHttpNamespaceResponse(BaseModel):
    OperationId: Optional[OperationId] = None


class CreatePrivateDnsNamespaceResponse(CreateHttpNamespaceResponse):
    pass


class CreatePublicDnsNamespaceResponse(CreateHttpNamespaceResponse):
    pass


class DeleteNamespaceResponse(CreateHttpNamespaceResponse):
    pass


class DeleteNamespaceRequest(BaseModel):
    Id: ResourceId


class DeleteServiceRequest(BaseModel):
    Id: ResourceId


class DeregisterInstanceResponse(CreateHttpNamespaceResponse):
    pass


class DeregisterInstanceRequest(BaseModel):
    ServiceId: ResourceId
    InstanceId: ResourceId


class DiscoverInstancesRequest(BaseModel):
    NamespaceName: NamespaceName
    ServiceName: ServiceName
    MaxResults: Optional[DiscoverMaxResults] = None
    QueryParameters: Optional[Attributes] = None
    OptionalParameters: Optional[Attributes] = None
    HealthStatus: Optional[HealthStatusFilter] = None


class GetInstanceResponse(BaseModel):
    Instance: Optional[Instance] = None


class GetInstanceRequest(BaseModel):
    ServiceId: ResourceId
    InstanceId: ResourceId


class GetInstancesHealthStatusResponse(BaseModel):
    Status: Optional[InstanceHealthStatusMap] = None
    NextToken: Optional[NextToken] = None


class GetInstancesHealthStatusRequest(BaseModel):
    ServiceId: ResourceId
    Instances: Optional[InstanceIdList] = None
    MaxResults: Optional[MaxResults] = None
    NextToken: Optional[NextToken] = None


class GetNamespaceRequest(BaseModel):
    Id: ResourceId


class GetOperationRequest(BaseModel):
    OperationId: ResourceId


class GetServiceRequest(BaseModel):
    Id: ResourceId


class ListInstancesResponse(BaseModel):
    Instances: Optional[InstanceSummaryList] = None
    NextToken: Optional[NextToken] = None


class ListInstancesRequest(BaseModel):
    ServiceId: ResourceId
    NextToken: Optional[NextToken] = None
    MaxResults: Optional[MaxResults] = None


class ListTagsForResourceRequest(BaseModel):
    ResourceARN: AmazonResourceName


class RegisterInstanceResponse(CreateHttpNamespaceResponse):
    pass


class RegisterInstanceRequest(BaseModel):
    ServiceId: ResourceId
    InstanceId: InstanceId
    CreatorRequestId: Optional[ResourceId] = None
    Attributes: Attributes


class UntagResourceRequest(BaseModel):
    ResourceARN: AmazonResourceName
    TagKeys: TagKeyList


class UpdateHttpNamespaceResponse(CreateHttpNamespaceResponse):
    pass


class UpdateHttpNamespaceRequest(BaseModel):
    Id: ResourceId
    UpdaterRequestId: Optional[ResourceId] = None
    Namespace: HttpNamespaceChange


class UpdateInstanceCustomHealthStatusRequest(BaseModel):
    ServiceId: ResourceId
    InstanceId: ResourceId
    Status: CustomHealthStatus


class UpdatePrivateDnsNamespaceResponse(CreateHttpNamespaceResponse):
    pass


class UpdatePublicDnsNamespaceResponse(CreateHttpNamespaceResponse):
    pass


class UpdateServiceResponse(CreateHttpNamespaceResponse):
    pass


class TagList(BaseModel):
    __root__: Annotated[List[Tag], Field(max_items=200, min_items=0)]


class HealthCheckConfig(BaseModel):
    """
    <p> <i>Public DNS and HTTP namespaces only.</i> A complex type that contains settings for an optional health check. If you specify settings for a health check, Cloud Map associates the health check with the records that you specify in <code>DnsConfig</code>.</p> <important> <p>If you specify a health check configuration, you can specify either <code>HealthCheckCustomConfig</code> or <code>HealthCheckConfig</code> but not both.</p> </important> <p>Health checks are basic Route 53 health checks that monitor an Amazon Web Services endpoint. For information about pricing for health checks, see <a href="http://aws.amazon.com/route53/pricing/">Amazon Route 53 Pricing</a>.</p> <p>Note the following about configuring health checks.</p> <dl> <dt>A and AAAA records</dt> <dd> <p>If <code>DnsConfig</code> includes configurations for both <code>A</code> and <code>AAAA</code> records, Cloud Map creates a health check that uses the IPv4 address to check the health of the resource. If the endpoint tthat's specified by the IPv4 address is unhealthy, Route 53 considers both the <code>A</code> and <code>AAAA</code> records to be unhealthy. </p> </dd> <dt>CNAME records</dt> <dd> <p>You can't specify settings for <code>HealthCheckConfig</code> when the <code>DNSConfig</code> includes <code>CNAME</code> for the value of <code>Type</code>. If you do, the <code>CreateService</code> request will fail with an <code>InvalidInput</code> error.</p> </dd> <dt>Request interval</dt> <dd> <p>A Route 53 health checker in each health-checking Amazon Web Services Region sends a health check request to an endpoint every 30 seconds. On average, your endpoint receives a health check request about every two seconds. However, health checkers don't coordinate with one another. Therefore, you might sometimes see several requests in one second that's followed by a few seconds with no health checks at all.</p> </dd> <dt>Health checking regions</dt> <dd> <p>Health checkers perform checks from all Route 53 health-checking Regions. For a list of the current Regions, see <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_HealthCheckConfig.html#Route53-Type-HealthCheckConfig-Regions">Regions</a>.</p> </dd> <dt>Alias records</dt> <dd> <p>When you register an instance, if you include the <code>AWS_ALIAS_DNS_NAME</code> attribute, Cloud Map creates a Route 53 alias record. Note the following:</p> <ul> <li> <p>Route 53 automatically sets <code>EvaluateTargetHealth</code> to true for alias records. When <code>EvaluateTargetHealth</code> is true, the alias record inherits the health of the referenced Amazon Web Services resource. such as an ELB load balancer. For more information, see <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_AliasTarget.html#Route53-Type-AliasTarget-EvaluateTargetHealth">EvaluateTargetHealth</a>.</p> </li> <li> <p>If you include <code>HealthCheckConfig</code> and then use the service to register an instance that creates an alias record, Route 53 doesn't create the health check.</p> </li> </ul> </dd> <dt>Charges for health checks</dt> <dd> <p>Health checks are basic Route 53 health checks that monitor an Amazon Web Services endpoint. For information about pricing for health checks, see <a href="http://aws.amazon.com/route53/pricing/">Amazon Route 53 Pricing</a>.</p> </dd> </dl>
    """

    Type: HealthCheckType
    ResourcePath: Optional[ResourcePath] = None
    FailureThreshold: Optional[FailureThreshold] = None


class HealthCheckCustomConfig(BaseModel):
    """
    <p>A complex type that contains information about an optional custom health check. A custom health check, which requires that you use a third-party health checker to evaluate the health of your resources, is useful in the following circumstances:</p> <ul> <li> <p>You can't use a health check that's defined by <code>HealthCheckConfig</code> because the resource isn't available over the internet. For example, you can use a custom health check when the instance is in an Amazon VPC. (To check the health of resources in a VPC, the health checker must also be in the VPC.)</p> </li> <li> <p>You want to use a third-party health checker regardless of where your resources are located.</p> </li> </ul> <important> <p>If you specify a health check configuration, you can specify either <code>HealthCheckCustomConfig</code> or <code>HealthCheckConfig</code> but not both.</p> </important> <p>To change the status of a custom health check, submit an <code>UpdateInstanceCustomHealthStatus</code> request. Cloud Map doesn't monitor the status of the resource, it just keeps a record of the status specified in the most recent <code>UpdateInstanceCustomHealthStatus</code> request.</p> <p>Here's how custom health checks work:</p> <ol> <li> <p>You create a service.</p> </li> <li> <p>You register an instance.</p> </li> <li> <p>You configure a third-party health checker to monitor the resource that's associated with the new instance. </p> <note> <p>Cloud Map doesn't check the health of the resource directly. </p> </note> </li> <li> <p>The third-party health-checker determines that the resource is unhealthy and notifies your application.</p> </li> <li> <p>Your application submits an <code>UpdateInstanceCustomHealthStatus</code> request.</p> </li> <li> <p>Cloud Map waits for 30 seconds.</p> </li> <li> <p>If another <code>UpdateInstanceCustomHealthStatus</code> request doesn't arrive during that time to change the status back to healthy, Cloud Map stops routing traffic to the resource.</p> </li> </ol>
    """

    FailureThreshold: Optional[FailureThreshold] = None


class HttpInstanceSummaryList(BaseModel):
    __root__: List[HttpInstanceSummary]


class DnsRecordList(BaseModel):
    __root__: List[DnsRecord]


class DnsConfigChange(BaseModel):
    """
    A complex type that contains information about changes to the Route 53 DNS records that Cloud Map creates when you register an instance.
    """

    DnsRecords: DnsRecordList


class SOA(SOAChange):
    """
    Start of Authority (SOA) properties for a public or private DNS namespace.
    """

    pass


class DnsProperties2(BaseModel):
    """
    A complex type that contains the ID for the Route 53 hosted zone that Cloud Map creates when you create a namespace.
    """

    HostedZoneId: Optional[ResourceId] = None
    SOA: Optional[SOA] = None


class Operation(BaseModel):
    """
    A complex type that contains information about a specified operation.
    """

    Id: Optional[OperationId] = None
    Type: Optional[OperationType] = None
    Status: Optional[OperationStatus] = None
    ErrorMessage: Optional[Message] = None
    ErrorCode: Optional[Code] = None
    CreateDate: Optional[Timestamp] = None
    UpdateDate: Optional[Timestamp] = None
    Targets: Optional[OperationTargetsMap] = None


class NamespaceFilters(BaseModel):
    __root__: List[NamespaceFilter]


class OperationFilters(BaseModel):
    __root__: List[OperationFilter]


class OperationSummaryList(BaseModel):
    __root__: List[OperationSummary]


class ServiceFilters(BaseModel):
    __root__: List[ServiceFilter]


class NamespaceProperties(BaseModel):
    """
    A complex type that contains information that's specific to the namespace type.
    """

    DnsProperties: Optional[DnsProperties2] = None
    HttpProperties: Optional[HttpProperties] = None


class NamespaceSummary(BaseModel):
    """
    A complex type that contains information about a namespace.
    """

    Id: Optional[ResourceId] = None
    Arn: Optional[Arn] = None
    Name: Optional[NamespaceName] = None
    Type: Optional[NamespaceType] = None
    Description: Optional[ResourceDescription] = None
    ServiceCount: Optional[ResourceCount] = None
    Properties: Optional[NamespaceProperties] = None
    CreateDate: Optional[Timestamp] = None


class PrivateDnsPropertiesMutable(BaseModel):
    """
    DNS properties for the private DNS namespace.
    """

    SOA: SOA


class PrivateDnsPropertiesMutableChange(PublicDnsPropertiesMutableChange):
    """
    Updated DNS properties for the private DNS namespace.
    """

    pass


class PublicDnsNamespacePropertiesChange(BaseModel):
    """
    Updated properties for the public DNS namespace.
    """

    DnsProperties: PublicDnsPropertiesMutableChange


class PublicDnsNamespaceChange(BaseModel):
    """
    Updated properties for the public DNS namespace.
    """

    Description: Optional[ResourceDescription] = None
    Properties: Optional[PublicDnsNamespacePropertiesChange] = None


class PublicDnsPropertiesMutable(PrivateDnsPropertiesMutable):
    """
    DNS properties for the public DNS namespace.
    """

    pass


class ServiceChange(BaseModel):
    """
    A complex type that contains changes to an existing service.
    """

    Description: Optional[ResourceDescription] = None
    DnsConfig: Optional[DnsConfigChange] = None
    HealthCheckConfig: Optional[HealthCheckConfig] = None


class CreateHttpNamespaceRequest(BaseModel):
    Name: NamespaceNameHttp
    CreatorRequestId: Optional[ResourceId] = None
    Description: Optional[ResourceDescription] = None
    Tags: Optional[TagList] = None


class DiscoverInstancesResponse(BaseModel):
    Instances: Optional[HttpInstanceSummaryList] = None


class GetOperationResponse(BaseModel):
    Operation: Optional[Operation] = None


class ListNamespacesRequest(BaseModel):
    NextToken: Optional[NextToken] = None
    MaxResults: Optional[MaxResults] = None
    Filters: Optional[NamespaceFilters] = None


class ListOperationsResponse(BaseModel):
    Operations: Optional[OperationSummaryList] = None
    NextToken: Optional[NextToken] = None


class ListOperationsRequest(BaseModel):
    NextToken: Optional[NextToken] = None
    MaxResults: Optional[MaxResults] = None
    Filters: Optional[OperationFilters] = None


class ListServicesRequest(BaseModel):
    NextToken: Optional[NextToken] = None
    MaxResults: Optional[MaxResults] = None
    Filters: Optional[ServiceFilters] = None


class ListTagsForResourceResponse(BaseModel):
    Tags: Optional[TagList] = None


class TagResourceRequest(BaseModel):
    ResourceARN: AmazonResourceName
    Tags: TagList


class UpdatePublicDnsNamespaceRequest(BaseModel):
    Id: ResourceId
    UpdaterRequestId: Optional[ResourceId] = None
    Namespace: PublicDnsNamespaceChange


class UpdateServiceRequest(BaseModel):
    Id: ResourceId
    Service: ServiceChange


class PrivateDnsNamespaceProperties(BaseModel):
    """
    DNS properties for the private DNS namespace.
    """

    DnsProperties: PrivateDnsPropertiesMutable


class PublicDnsNamespaceProperties(BaseModel):
    """
    DNS properties for the public DNS namespace.
    """

    DnsProperties: PublicDnsPropertiesMutable


class DnsConfig(BaseModel):
    """
    A complex type that contains information about the Amazon Route 53 DNS records that you want Cloud Map to create when you register an instance.
    """

    NamespaceId: Optional[ResourceId] = None
    RoutingPolicy: Optional[RoutingPolicy] = None
    DnsRecords: DnsRecordList


class Service(BaseModel):
    """
    A complex type that contains information about the specified service.
    """

    Id: Optional[ResourceId] = None
    Arn: Optional[Arn] = None
    Name: Optional[ServiceName] = None
    NamespaceId: Optional[ResourceId] = None
    Description: Optional[ResourceDescription] = None
    InstanceCount: Optional[ResourceCount] = None
    DnsConfig: Optional[DnsConfig] = None
    Type: Optional[ServiceType] = None
    HealthCheckConfig: Optional[HealthCheckConfig] = None
    HealthCheckCustomConfig: Optional[HealthCheckCustomConfig] = None
    CreateDate: Optional[Timestamp] = None
    CreatorRequestId: Optional[ResourceId] = None


class Namespace(BaseModel):
    """
    A complex type that contains information about a specified namespace.
    """

    Id: Optional[ResourceId] = None
    Arn: Optional[Arn] = None
    Name: Optional[NamespaceName] = None
    Type: Optional[NamespaceType] = None
    Description: Optional[ResourceDescription] = None
    ServiceCount: Optional[ResourceCount] = None
    Properties: Optional[NamespaceProperties] = None
    CreateDate: Optional[Timestamp] = None
    CreatorRequestId: Optional[ResourceId] = None


class NamespaceSummariesList(BaseModel):
    __root__: List[NamespaceSummary]


class PrivateDnsNamespacePropertiesChange(BaseModel):
    """
    Updated properties for the private DNS namespace.
    """

    DnsProperties: PrivateDnsPropertiesMutableChange


class PrivateDnsNamespaceChange(BaseModel):
    """
    Updated properties for the private DNS namespace.
    """

    Description: Optional[ResourceDescription] = None
    Properties: Optional[PrivateDnsNamespacePropertiesChange] = None


class ServiceSummary(BaseModel):
    """
    A complex type that contains information about a specified service.
    """

    Id: Optional[ResourceId] = None
    Arn: Optional[Arn] = None
    Name: Optional[ServiceName] = None
    Type: Optional[ServiceType] = None
    Description: Optional[ResourceDescription] = None
    InstanceCount: Optional[ResourceCount] = None
    DnsConfig: Optional[DnsConfig] = None
    HealthCheckConfig: Optional[HealthCheckConfig] = None
    HealthCheckCustomConfig: Optional[HealthCheckCustomConfig] = None
    CreateDate: Optional[Timestamp] = None


class CreatePrivateDnsNamespaceRequest(BaseModel):
    Name: NamespaceNamePrivate
    CreatorRequestId: Optional[ResourceId] = None
    Description: Optional[ResourceDescription] = None
    Vpc: ResourceId
    Tags: Optional[TagList] = None
    Properties: Optional[PrivateDnsNamespaceProperties] = None


class CreatePublicDnsNamespaceRequest(BaseModel):
    Name: NamespaceNamePublic
    CreatorRequestId: Optional[ResourceId] = None
    Description: Optional[ResourceDescription] = None
    Tags: Optional[TagList] = None
    Properties: Optional[PublicDnsNamespaceProperties] = None


class CreateServiceResponse(BaseModel):
    Service: Optional[Service] = None


class CreateServiceRequest(BaseModel):
    Name: ServiceName
    NamespaceId: Optional[ResourceId] = None
    CreatorRequestId: Optional[ResourceId] = None
    Description: Optional[ResourceDescription] = None
    DnsConfig: Optional[DnsConfig] = None
    HealthCheckConfig: Optional[HealthCheckConfig] = None
    HealthCheckCustomConfig: Optional[HealthCheckCustomConfig] = None
    Tags: Optional[TagList] = None
    Type: Optional[ServiceTypeOption] = None


class GetNamespaceResponse(BaseModel):
    Namespace: Optional[Namespace] = None


class GetServiceResponse(CreateServiceResponse):
    pass


class ListNamespacesResponse(BaseModel):
    Namespaces: Optional[NamespaceSummariesList] = None
    NextToken: Optional[NextToken] = None


class UpdatePrivateDnsNamespaceRequest(BaseModel):
    Id: ResourceId
    UpdaterRequestId: Optional[ResourceId] = None
    Namespace: PrivateDnsNamespaceChange


class ServiceSummariesList(BaseModel):
    __root__: List[ServiceSummary]


class ListServicesResponse(BaseModel):
    Services: Optional[ServiceSummariesList] = None
    NextToken: Optional[NextToken] = None
