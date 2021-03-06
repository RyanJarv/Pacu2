# generated by datamodel-codegen:
#   filename:  openapi.yaml
#   timestamp: 2021-12-31T02:47:20+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Annotated, Any, List, Optional

from pydantic import BaseModel


class ClusterAlreadyExistsFault(BaseModel):
    __root__: Any


class InvalidClusterStateFault(ClusterAlreadyExistsFault):
    pass


class InsufficientClusterCapacityFault(ClusterAlreadyExistsFault):
    pass


class SubnetGroupNotFoundFault(ClusterAlreadyExistsFault):
    pass


class InvalidParameterGroupStateFault(ClusterAlreadyExistsFault):
    pass


class ParameterGroupNotFoundFault(ClusterAlreadyExistsFault):
    pass


class ClusterQuotaForCustomerExceededFault(ClusterAlreadyExistsFault):
    pass


class NodeQuotaForClusterExceededFault(ClusterAlreadyExistsFault):
    pass


class NodeQuotaForCustomerExceededFault(ClusterAlreadyExistsFault):
    pass


class InvalidVPCNetworkStateFault(ClusterAlreadyExistsFault):
    pass


class TagQuotaPerResourceExceeded(ClusterAlreadyExistsFault):
    pass


class ServiceLinkedRoleNotFoundFault(ClusterAlreadyExistsFault):
    pass


class InvalidParameterValueException(ClusterAlreadyExistsFault):
    pass


class InvalidParameterCombinationException(ClusterAlreadyExistsFault):
    pass


class ServiceQuotaExceededException(ClusterAlreadyExistsFault):
    pass


class ParameterGroupQuotaExceededFault(ClusterAlreadyExistsFault):
    pass


class ParameterGroupAlreadyExistsFault(ClusterAlreadyExistsFault):
    pass


class SubnetGroupAlreadyExistsFault(ClusterAlreadyExistsFault):
    pass


class SubnetGroupQuotaExceededFault(ClusterAlreadyExistsFault):
    pass


class SubnetQuotaExceededFault(ClusterAlreadyExistsFault):
    pass


class InvalidSubnet(ClusterAlreadyExistsFault):
    pass


class ClusterNotFoundFault(ClusterAlreadyExistsFault):
    pass


class NodeNotFoundFault(ClusterAlreadyExistsFault):
    pass


class SubnetGroupInUseFault(ClusterAlreadyExistsFault):
    pass


class InvalidARNFault(ClusterAlreadyExistsFault):
    pass


class TagNotFoundFault(ClusterAlreadyExistsFault):
    pass


class SubnetInUse(ClusterAlreadyExistsFault):
    pass


class String(BaseModel):
    __root__: str


class AvailabilityZoneList(BaseModel):
    __root__: List[String]


class ChangeType(Enum):
    IMMEDIATE = 'IMMEDIATE'
    REQUIRES_REBOOT = 'REQUIRES_REBOOT'


class IntegerOptional(BaseModel):
    __root__: int


class NodeIdentifierList(AvailabilityZoneList):
    pass


class NotificationConfiguration(BaseModel):
    """
    Describes a notification topic and its status. Notification topics are used for publishing DAX events to subscribers using Amazon Simple Notification Service (SNS).
    """

    TopicArn: Optional[String] = None
    TopicStatus: Optional[String] = None


class ParameterGroupStatus(BaseModel):
    """
    The status of a parameter group.
    """

    ParameterGroupName: Optional[String] = None
    ParameterApplyStatus: Optional[String] = None
    NodeIdsToReboot: Optional[NodeIdentifierList] = None


class ClusterEndpointEncryptionType(Enum):
    NONE = 'NONE'
    TLS = 'TLS'


class ClusterNameList(AvailabilityZoneList):
    pass


class Integer(IntegerOptional):
    pass


class SecurityGroupIdentifierList(AvailabilityZoneList):
    pass


class ParameterGroup(BaseModel):
    """
    A named set of parameters that are applied to all of the nodes in a DAX cluster.
    """

    ParameterGroupName: Optional[String] = None
    Description: Optional[String] = None


class SubnetIdentifierList(AvailabilityZoneList):
    pass


class SourceType(Enum):
    CLUSTER = 'CLUSTER'
    PARAMETER_GROUP = 'PARAMETER_GROUP'
    SUBNET_GROUP = 'SUBNET_GROUP'


class TStamp(BaseModel):
    __root__: datetime


class ParameterGroupNameList(AvailabilityZoneList):
    pass


class ParameterGroupList(BaseModel):
    __root__: List[ParameterGroup]


class SubnetGroupNameList(AvailabilityZoneList):
    pass


class Event(BaseModel):
    """
    Represents a single occurrence of something interesting within the system. Some examples of events are creating a DAX cluster, adding or removing a node, or rebooting a node.
    """

    SourceName: Optional[String] = None
    SourceType: Optional[SourceType] = None
    Message: Optional[String] = None
    Date: Optional[TStamp] = None


class IsModifiable(Enum):
    TRUE = 'TRUE'
    FALSE = 'FALSE'
    CONDITIONAL = 'CONDITIONAL'


class KeyList(AvailabilityZoneList):
    pass


class NodeTypeSpecificValue(BaseModel):
    """
    Represents a parameter value that is applicable to a particular node type.
    """

    NodeType: Optional[String] = None
    Value: Optional[String] = None


class NodeTypeSpecificValueList(BaseModel):
    __root__: List[NodeTypeSpecificValue]


class ParameterType(Enum):
    DEFAULT = 'DEFAULT'
    NODE_TYPE_SPECIFIC = 'NODE_TYPE_SPECIFIC'


class Parameter(BaseModel):
    """
    Describes an individual setting that controls some aspect of DAX behavior.
    """

    ParameterName: Optional[String] = None
    ParameterType: Optional[ParameterType] = None
    ParameterValue: Optional[String] = None
    NodeTypeSpecificValues: Optional[NodeTypeSpecificValueList] = None
    Description: Optional[String] = None
    Source: Optional[String] = None
    DataType: Optional[String] = None
    AllowedValues: Optional[String] = None
    IsModifiable: Optional[IsModifiable] = None
    ChangeType: Optional[ChangeType] = None


class ParameterNameValue(BaseModel):
    """
    An individual DAX parameter.
    """

    ParameterName: Optional[String] = None
    ParameterValue: Optional[String] = None


class ParameterNameValueList(BaseModel):
    __root__: List[ParameterNameValue]


class SSEStatus(Enum):
    ENABLING = 'ENABLING'
    ENABLED = 'ENABLED'
    DISABLING = 'DISABLING'
    DISABLED = 'DISABLED'


class SSEEnabled(BaseModel):
    __root__: bool


class SecurityGroupMembership(BaseModel):
    """
    An individual VPC security group and its status.
    """

    SecurityGroupIdentifier: Optional[String] = None
    Status: Optional[String] = None


class Subnet(BaseModel):
    """
    Represents the subnet associated with a DAX cluster. This parameter refers to subnets defined in Amazon Virtual Private Cloud (Amazon VPC) and used with DAX.
    """

    SubnetIdentifier: Optional[String] = None
    SubnetAvailabilityZone: Optional[String] = None


class SubnetList(BaseModel):
    __root__: List[Subnet]


class Tag(BaseModel):
    """
    <p>A description of a tag. Every tag is a key-value pair. You can add up to 50 tags to a single DAX cluster.</p> <p>AWS-assigned tag names and values are automatically assigned the <code>aws:</code> prefix, which the user cannot assign. AWS-assigned tag names do not count towards the tag limit of 50. User-assigned tag names have the prefix <code>user:</code>.</p> <p>You cannot backdate the application of a tag.</p>
    """

    Key: Optional[String] = None
    Value: Optional[String] = None


class CreateParameterGroupResponse(BaseModel):
    ParameterGroup: Optional[ParameterGroup] = None


class CreateParameterGroupRequest(BaseModel):
    ParameterGroupName: String
    Description: Optional[String] = None


class CreateSubnetGroupRequest(BaseModel):
    SubnetGroupName: String
    Description: Optional[String] = None
    SubnetIds: SubnetIdentifierList


class DecreaseReplicationFactorRequest(BaseModel):
    ClusterName: String
    NewReplicationFactor: Integer
    AvailabilityZones: Optional[AvailabilityZoneList] = None
    NodeIdsToRemove: Optional[NodeIdentifierList] = None


class DeleteClusterRequest(BaseModel):
    ClusterName: String


class DeleteParameterGroupResponse(BaseModel):
    DeletionMessage: Optional[String] = None


class DeleteParameterGroupRequest(BaseModel):
    ParameterGroupName: String


class DeleteSubnetGroupResponse(DeleteParameterGroupResponse):
    pass


class DeleteSubnetGroupRequest(BaseModel):
    SubnetGroupName: String


class DescribeClustersRequest(BaseModel):
    ClusterNames: Optional[ClusterNameList] = None
    MaxResults: Optional[IntegerOptional] = None
    NextToken: Optional[String] = None


class DescribeDefaultParametersRequest(BaseModel):
    MaxResults: Optional[IntegerOptional] = None
    NextToken: Optional[String] = None


class DescribeEventsRequest(BaseModel):
    SourceName: Optional[String] = None
    SourceType: Optional[SourceType] = None
    StartTime: Optional[TStamp] = None
    EndTime: Optional[TStamp] = None
    Duration: Optional[IntegerOptional] = None
    MaxResults: Optional[IntegerOptional] = None
    NextToken: Optional[String] = None


class DescribeParameterGroupsResponse(BaseModel):
    NextToken: Optional[String] = None
    ParameterGroups: Optional[ParameterGroupList] = None


class DescribeParameterGroupsRequest(BaseModel):
    ParameterGroupNames: Optional[ParameterGroupNameList] = None
    MaxResults: Optional[IntegerOptional] = None
    NextToken: Optional[String] = None


class DescribeParametersRequest(BaseModel):
    ParameterGroupName: String
    Source: Optional[String] = None
    MaxResults: Optional[IntegerOptional] = None
    NextToken: Optional[String] = None


class DescribeSubnetGroupsRequest(BaseModel):
    SubnetGroupNames: Optional[SubnetGroupNameList] = None
    MaxResults: Optional[IntegerOptional] = None
    NextToken: Optional[String] = None


class IncreaseReplicationFactorRequest(BaseModel):
    ClusterName: String
    NewReplicationFactor: Integer
    AvailabilityZones: Optional[AvailabilityZoneList] = None


class ListTagsRequest(BaseModel):
    ResourceName: String
    NextToken: Optional[String] = None


class RebootNodeRequest(BaseModel):
    ClusterName: String
    NodeId: String


class UntagResourceRequest(BaseModel):
    ResourceName: String
    TagKeys: KeyList


class UpdateClusterRequest(BaseModel):
    ClusterName: String
    Description: Optional[String] = None
    PreferredMaintenanceWindow: Optional[String] = None
    NotificationTopicArn: Optional[String] = None
    NotificationTopicStatus: Optional[String] = None
    ParameterGroupName: Optional[String] = None
    SecurityGroupIds: Optional[SecurityGroupIdentifierList] = None


class UpdateParameterGroupResponse(CreateParameterGroupResponse):
    pass


class UpdateParameterGroupRequest(BaseModel):
    ParameterGroupName: String
    ParameterNameValues: ParameterNameValueList


class UpdateSubnetGroupRequest(BaseModel):
    SubnetGroupName: String
    Description: Optional[String] = None
    SubnetIds: Optional[SubnetIdentifierList] = None


class Endpoint(BaseModel):
    """
    Represents the information required for client programs to connect to the endpoint for a DAX cluster.
    """

    Address: Optional[String] = None
    Port: Optional[Integer] = None
    URL: Optional[String] = None


class SecurityGroupMembershipList(BaseModel):
    __root__: List[SecurityGroupMembership]


class SSEDescription(BaseModel):
    """
    The description of the server-side encryption status on the specified DAX cluster.
    """

    Status: Optional[SSEStatus] = None


class TagList(BaseModel):
    __root__: List[Tag]


class SSESpecification(BaseModel):
    """
    Represents the settings used to enable server-side encryption.
    """

    Enabled: SSEEnabled


class SubnetGroup(BaseModel):
    """
    <p>Represents the output of one of the following actions:</p> <ul> <li> <p> <i>CreateSubnetGroup</i> </p> </li> <li> <p> <i>ModifySubnetGroup</i> </p> </li> </ul>
    """

    SubnetGroupName: Optional[String] = None
    Description: Optional[String] = None
    VpcId: Optional[String] = None
    Subnets: Optional[SubnetList] = None


class ParameterList(BaseModel):
    __root__: List[Parameter]


class EventList(BaseModel):
    __root__: List[Event]


class SubnetGroupList(BaseModel):
    __root__: List[SubnetGroup]


class Node(BaseModel):
    """
    Represents an individual node within a DAX cluster.
    """

    NodeId: Optional[String] = None
    Endpoint: Optional[Endpoint] = None
    NodeCreateTime: Optional[TStamp] = None
    AvailabilityZone: Optional[String] = None
    NodeStatus: Optional[String] = None
    ParameterGroupStatus: Optional[String] = None


class CreateClusterRequest(BaseModel):
    ClusterName: String
    NodeType: String
    Description: Optional[String] = None
    ReplicationFactor: Integer
    AvailabilityZones: Optional[AvailabilityZoneList] = None
    SubnetGroupName: Optional[String] = None
    SecurityGroupIds: Optional[SecurityGroupIdentifierList] = None
    PreferredMaintenanceWindow: Optional[String] = None
    NotificationTopicArn: Optional[String] = None
    IamRoleArn: String
    ParameterGroupName: Optional[String] = None
    Tags: Optional[TagList] = None
    SSESpecification: Optional[SSESpecification] = None
    ClusterEndpointEncryptionType: Optional[ClusterEndpointEncryptionType] = None


class CreateSubnetGroupResponse(BaseModel):
    SubnetGroup: Optional[SubnetGroup] = None


class DescribeDefaultParametersResponse(BaseModel):
    NextToken: Optional[String] = None
    Parameters: Optional[ParameterList] = None


class DescribeEventsResponse(BaseModel):
    NextToken: Optional[String] = None
    Events: Optional[EventList] = None


class DescribeParametersResponse(DescribeDefaultParametersResponse):
    pass


class DescribeSubnetGroupsResponse(BaseModel):
    NextToken: Optional[String] = None
    SubnetGroups: Optional[SubnetGroupList] = None


class ListTagsResponse(BaseModel):
    Tags: Optional[TagList] = None
    NextToken: Optional[String] = None


class TagResourceResponse(BaseModel):
    Tags: Optional[TagList] = None


class TagResourceRequest(BaseModel):
    ResourceName: String
    Tags: TagList


class UntagResourceResponse(TagResourceResponse):
    pass


class UpdateSubnetGroupResponse(CreateSubnetGroupResponse):
    pass


class NodeList(BaseModel):
    __root__: List[Node]


class Cluster(BaseModel):
    """
    Contains all of the attributes of a specific DAX cluster.
    """

    ClusterName: Optional[String] = None
    Description: Optional[String] = None
    ClusterArn: Optional[String] = None
    TotalNodes: Optional[IntegerOptional] = None
    ActiveNodes: Optional[IntegerOptional] = None
    NodeType: Optional[String] = None
    Status: Optional[String] = None
    ClusterDiscoveryEndpoint: Optional[Endpoint] = None
    NodeIdsToRemove: Optional[NodeIdentifierList] = None
    Nodes: Optional[NodeList] = None
    PreferredMaintenanceWindow: Optional[String] = None
    NotificationConfiguration: Optional[NotificationConfiguration] = None
    SubnetGroup: Optional[String] = None
    SecurityGroups: Optional[SecurityGroupMembershipList] = None
    IamRoleArn: Optional[String] = None
    ParameterGroup: Optional[ParameterGroupStatus] = None
    SSEDescription: Optional[SSEDescription] = None
    ClusterEndpointEncryptionType: Optional[ClusterEndpointEncryptionType] = None


class ClusterList(BaseModel):
    __root__: List[Cluster]


class CreateClusterResponse(BaseModel):
    Cluster: Optional[Cluster] = None


class DecreaseReplicationFactorResponse(CreateClusterResponse):
    pass


class DeleteClusterResponse(CreateClusterResponse):
    pass


class DescribeClustersResponse(BaseModel):
    NextToken: Optional[String] = None
    Clusters: Optional[ClusterList] = None


class IncreaseReplicationFactorResponse(CreateClusterResponse):
    pass


class RebootNodeResponse(CreateClusterResponse):
    pass


class UpdateClusterResponse(CreateClusterResponse):
    pass
