# generated by datamodel-codegen:
#   filename:  openapi.yaml
#   timestamp: 2021-12-31T02:49:36+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Annotated, Any, List, Optional

from pydantic import BaseModel, Extra, Field


class InvalidOperationException(BaseModel):
    __root__: Any


class InvalidInputException(InvalidOperationException):
    pass


class ResourceNotFoundException(InvalidOperationException):
    pass


class InternalErrorException(InvalidOperationException):
    pass


class LimitExceededException(InvalidOperationException):
    pass


class DeleteNotificationChannelRequest(BaseModel):
    pass


class DisassociateAdminAccountRequest(BaseModel):
    pass


class GetAdminAccountRequest(BaseModel):
    pass


class GetNotificationChannelRequest(BaseModel):
    pass


class InvalidTypeException(InvalidOperationException):
    pass


class TagResourceResponse(BaseModel):
    pass


class UntagResourceResponse(TagResourceResponse):
    pass


class AWSAccountId(BaseModel):
    __root__: Annotated[str, Field(max_length=1024, min_length=1, regex='^[0-9]+$')]


class AccountRoleStatus(Enum):
    READY = 'READY'
    CREATING = 'CREATING'
    PENDING_DELETION = 'PENDING_DELETION'
    DELETING = 'DELETING'
    DELETED = 'DELETED'


class ResourceId(BaseModel):
    __root__: Annotated[
        str,
        Field(
            max_length=1024, min_length=1, regex='^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-@]*)$'
        ),
    ]


class LengthBoundedString(BaseModel):
    __root__: Annotated[str, Field(max_length=1024, min_length=0)]


class ActionTarget(BaseModel):
    """
    Describes a remediation action target.
    """

    ResourceId: Optional[ResourceId] = None
    Description: Optional[LengthBoundedString] = None


class ResourceName(BaseModel):
    __root__: Annotated[
        str,
        Field(
            max_length=128, min_length=1, regex='^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-@]*)$'
        ),
    ]


class Protocol(BaseModel):
    __root__: Annotated[
        str,
        Field(max_length=20, min_length=1, regex='^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-@]*)$'),
    ]


class IPPortNumber(BaseModel):
    __root__: Annotated[int, Field(ge=0.0, le=65535.0)]


class App(BaseModel):
    """
    An individual Firewall Manager application.
    """

    AppName: ResourceName
    Protocol: Protocol
    Port: IPPortNumber


class AppsList3(BaseModel):
    __root__: List[App]


class ListId(BaseModel):
    __root__: Annotated[
        str, Field(max_length=36, min_length=36, regex='^[a-z0-9A-Z-]{36}$')
    ]


class UpdateToken(ResourceId):
    pass


class TimeStamp(BaseModel):
    __root__: datetime


class PreviousAppsList(BaseModel):
    pass

    class Config:
        extra = Extra.allow


class AppsListData(BaseModel):
    """
    An Firewall Manager applications list.
    """

    ListId: Optional[ListId] = None
    ListName: ResourceName
    ListUpdateToken: Optional[UpdateToken] = None
    CreateTime: Optional[TimeStamp] = None
    LastUpdateTime: Optional[TimeStamp] = None
    AppsList: AppsList3
    PreviousAppsList: Optional[PreviousAppsList] = None


class ResourceArn(ResourceId):
    pass


class AppsListDataSummary(BaseModel):
    """
    Details of the Firewall Manager applications list.
    """

    ListArn: Optional[ResourceArn] = None
    ListId: Optional[ListId] = None
    ListName: Optional[ResourceName] = None
    AppsList: Optional[AppsList3] = None


class AppsListsData(BaseModel):
    __root__: List[AppsListDataSummary]


class ViolationTarget(BaseModel):
    __root__: Annotated[str, Field(max_length=1024, min_length=0, regex='.*')]


class ResourceIdList(BaseModel):
    __root__: List[ResourceId]


class AwsEc2NetworkInterfaceViolation(BaseModel):
    """
    Violation detail for network interfaces associated with an EC2 instance.
    """

    ViolationTarget: Optional[ViolationTarget] = None
    ViolatingSecurityGroups: Optional[ResourceIdList] = None


class BasicInteger(BaseModel):
    __root__: Annotated[int, Field(ge=-2147483648.0, le=2147483647.0)]


class Boolean(BaseModel):
    __root__: bool


class CIDR(BaseModel):
    __root__: Annotated[str, Field(max_length=256, min_length=0, regex='[a-f0-9:./]+')]


class ViolationReason(Enum):
    WEB_ACL_MISSING_RULE_GROUP = 'WEB_ACL_MISSING_RULE_GROUP'
    RESOURCE_MISSING_WEB_ACL = 'RESOURCE_MISSING_WEB_ACL'
    RESOURCE_INCORRECT_WEB_ACL = 'RESOURCE_INCORRECT_WEB_ACL'
    RESOURCE_MISSING_SHIELD_PROTECTION = 'RESOURCE_MISSING_SHIELD_PROTECTION'
    RESOURCE_MISSING_WEB_ACL_OR_SHIELD_PROTECTION = (
        'RESOURCE_MISSING_WEB_ACL_OR_SHIELD_PROTECTION'
    )
    RESOURCE_MISSING_SECURITY_GROUP = 'RESOURCE_MISSING_SECURITY_GROUP'
    RESOURCE_VIOLATES_AUDIT_SECURITY_GROUP = 'RESOURCE_VIOLATES_AUDIT_SECURITY_GROUP'
    SECURITY_GROUP_UNUSED = 'SECURITY_GROUP_UNUSED'
    SECURITY_GROUP_REDUNDANT = 'SECURITY_GROUP_REDUNDANT'
    FMS_CREATED_SECURITY_GROUP_EDITED = 'FMS_CREATED_SECURITY_GROUP_EDITED'
    MISSING_FIREWALL = 'MISSING_FIREWALL'
    MISSING_FIREWALL_SUBNET_IN_AZ = 'MISSING_FIREWALL_SUBNET_IN_AZ'
    MISSING_EXPECTED_ROUTE_TABLE = 'MISSING_EXPECTED_ROUTE_TABLE'
    NETWORK_FIREWALL_POLICY_MODIFIED = 'NETWORK_FIREWALL_POLICY_MODIFIED'
    INTERNET_GATEWAY_MISSING_EXPECTED_ROUTE = 'INTERNET_GATEWAY_MISSING_EXPECTED_ROUTE'
    FIREWALL_SUBNET_MISSING_EXPECTED_ROUTE = 'FIREWALL_SUBNET_MISSING_EXPECTED_ROUTE'
    UNEXPECTED_FIREWALL_ROUTES = 'UNEXPECTED_FIREWALL_ROUTES'
    UNEXPECTED_TARGET_GATEWAY_ROUTES = 'UNEXPECTED_TARGET_GATEWAY_ROUTES'
    TRAFFIC_INSPECTION_CROSSES_AZ_BOUNDARY = 'TRAFFIC_INSPECTION_CROSSES_AZ_BOUNDARY'
    INVALID_ROUTE_CONFIGURATION = 'INVALID_ROUTE_CONFIGURATION'
    MISSING_TARGET_GATEWAY = 'MISSING_TARGET_GATEWAY'
    INTERNET_TRAFFIC_NOT_INSPECTED = 'INTERNET_TRAFFIC_NOT_INSPECTED'
    BLACK_HOLE_ROUTE_DETECTED = 'BLACK_HOLE_ROUTE_DETECTED'
    BLACK_HOLE_ROUTE_DETECTED_IN_FIREWALL_SUBNET = (
        'BLACK_HOLE_ROUTE_DETECTED_IN_FIREWALL_SUBNET'
    )
    RESOURCE_MISSING_DNS_FIREWALL = 'RESOURCE_MISSING_DNS_FIREWALL'


class ResourceType(ResourceName):
    pass


class ComplianceViolator(BaseModel):
    """
    Details of the resource that is not protected by the policy.
    """

    ResourceId: Optional[ResourceId] = None
    ViolationReason: Optional[ViolationReason] = None
    ResourceType: Optional[ResourceType] = None


class ComplianceViolators(BaseModel):
    __root__: List[ComplianceViolator]


class CustomerPolicyScopeId(ResourceId):
    pass


class CustomerPolicyScopeIdList(BaseModel):
    __root__: List[CustomerPolicyScopeId]


class CustomerPolicyScopeIdType(Enum):
    ACCOUNT = 'ACCOUNT'
    ORG_UNIT = 'ORG_UNIT'


class CustomerPolicyScopeMap(BaseModel):
    pass

    class Config:
        extra = Extra.allow


class PolicyId(ListId):
    pass


class DependentServiceName(Enum):
    AWSCONFIG = 'AWSCONFIG'
    AWSWAF = 'AWSWAF'
    AWSSHIELD_ADVANCED = 'AWSSHIELD_ADVANCED'
    AWSVPC = 'AWSVPC'


class DestinationType(Enum):
    IPV4 = 'IPV4'
    IPV6 = 'IPV6'
    PREFIX_LIST = 'PREFIX_LIST'


class DetailedInfo(BaseModel):
    __root__: Annotated[
        str,
        Field(
            max_length=1024, min_length=1, regex='^([\\p{L}\\p{Z}\\p{N}_.:/=,+\\-@]*)$'
        ),
    ]


class DnsDuplicateRuleGroupViolation(BaseModel):
    """
    A DNS Firewall rule group that Firewall Manager tried to associate with a VPC is already associated with the VPC and can't be associated again.
    """

    ViolationTarget: Optional[ViolationTarget] = None
    ViolationTargetDescription: Optional[LengthBoundedString] = None


class DnsRuleGroupLimitExceededViolation(BaseModel):
    """
    The VPC that Firewall Manager was applying a DNS Fireall policy to reached the limit for associated DNS Firewall rule groups. Firewall Manager tried to associate another rule group with the VPC and failed due to the limit.
    """

    ViolationTarget: Optional[ViolationTarget] = None
    ViolationTargetDescription: Optional[LengthBoundedString] = None
    NumberOfRuleGroupsAlreadyAssociated: Optional[BasicInteger] = None


class DnsRuleGroupPriority(BaseModel):
    __root__: Annotated[int, Field(ge=0.0, le=10000.0)]


class DnsRuleGroupPriorities(BaseModel):
    __root__: List[DnsRuleGroupPriority]


class DnsRuleGroupPriorityConflictViolation(BaseModel):
    """
    A rule group that Firewall Manager tried to associate with a VPC has the same priority as a rule group that's already associated.
    """

    ViolationTarget: Optional[ViolationTarget] = None
    ViolationTargetDescription: Optional[LengthBoundedString] = None
    ConflictingPriority: Optional[DnsRuleGroupPriority] = None
    ConflictingPolicyId: Optional[PolicyId] = None
    UnavailablePriorities: Optional[DnsRuleGroupPriorities] = None


class EC2AssociateRouteTableAction(BaseModel):
    """
    The action of associating an EC2 resource, such as a subnet or internet gateway, with a route table.
    """

    Description: Optional[LengthBoundedString] = None
    RouteTableId: ActionTarget
    SubnetId: Optional[ActionTarget] = None
    GatewayId: Optional[ActionTarget] = None


class EC2CopyRouteTableAction(BaseModel):
    """
    An action that copies the EC2 route table for use in remediation.
    """

    Description: Optional[LengthBoundedString] = None
    VpcId: ActionTarget
    RouteTableId: ActionTarget


class EC2CreateRouteAction(BaseModel):
    """
    Information about the CreateRoute action in Amazon EC2.
    """

    Description: Optional[LengthBoundedString] = None
    DestinationCidrBlock: Optional[CIDR] = None
    DestinationPrefixListId: Optional[ResourceId] = None
    DestinationIpv6CidrBlock: Optional[CIDR] = None
    VpcEndpointId: Optional[ActionTarget] = None
    GatewayId: Optional[ActionTarget] = None
    RouteTableId: ActionTarget


class EC2CreateRouteTableAction(BaseModel):
    """
    Information about the CreateRouteTable action in Amazon EC2.
    """

    Description: Optional[LengthBoundedString] = None
    VpcId: ActionTarget


class EC2DeleteRouteAction(BaseModel):
    """
    Information about the DeleteRoute action in Amazon EC2.
    """

    Description: Optional[LengthBoundedString] = None
    DestinationCidrBlock: Optional[CIDR] = None
    DestinationPrefixListId: Optional[ResourceId] = None
    DestinationIpv6CidrBlock: Optional[CIDR] = None
    RouteTableId: ActionTarget


class EC2ReplaceRouteAction(BaseModel):
    """
    Information about the ReplaceRoute action in Amazon EC2.
    """

    Description: Optional[LengthBoundedString] = None
    DestinationCidrBlock: Optional[CIDR] = None
    DestinationPrefixListId: Optional[ResourceId] = None
    DestinationIpv6CidrBlock: Optional[CIDR] = None
    GatewayId: Optional[ActionTarget] = None
    RouteTableId: ActionTarget


class EC2ReplaceRouteTableAssociationAction(BaseModel):
    """
    Information about the ReplaceRouteTableAssociation action in Amazon EC2.
    """

    Description: Optional[LengthBoundedString] = None
    AssociationId: ActionTarget
    RouteTableId: ActionTarget


class PolicyComplianceStatusType(Enum):
    COMPLIANT = 'COMPLIANT'
    NON_COMPLIANT = 'NON_COMPLIANT'


class ResourceCount(BaseModel):
    __root__: Annotated[int, Field(ge=0.0)]


class EvaluationResult(BaseModel):
    """
    Describes the compliance status for the account. An account is considered noncompliant if it includes resources that are not protected by the specified policy or that don't comply with the policy.
    """

    ComplianceStatus: Optional[PolicyComplianceStatusType] = None
    ViolatorCount: Optional[ResourceCount] = None
    EvaluationLimitExceeded: Optional[Boolean] = None


class EvaluationResults(BaseModel):
    __root__: List[EvaluationResult]


class LengthBoundedStringList(BaseModel):
    __root__: List[LengthBoundedString]


class ExpectedRoute(BaseModel):
    """
    Information about the expected route in the route table.
    """

    IpV4Cidr: Optional[CIDR] = None
    PrefixListId: Optional[CIDR] = None
    IpV6Cidr: Optional[CIDR] = None
    ContributingSubnets: Optional[ResourceIdList] = None
    AllowedTargets: Optional[LengthBoundedStringList] = None
    RouteTableId: Optional[ResourceId] = None


class ExpectedRoutes(BaseModel):
    __root__: List[ExpectedRoute]


class PaginationToken(BaseModel):
    __root__: Annotated[
        str,
        Field(
            max_length=4096, min_length=1, regex='^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-@]*)$'
        ),
    ]


class PaginationMaxResults(BaseModel):
    __root__: Annotated[int, Field(ge=1.0, le=100.0)]


class SecurityServiceType(Enum):
    WAF = 'WAF'
    WAFV2 = 'WAFV2'
    SHIELD_ADVANCED = 'SHIELD_ADVANCED'
    SECURITY_GROUPS_COMMON = 'SECURITY_GROUPS_COMMON'
    SECURITY_GROUPS_CONTENT_AUDIT = 'SECURITY_GROUPS_CONTENT_AUDIT'
    SECURITY_GROUPS_USAGE_AUDIT = 'SECURITY_GROUPS_USAGE_AUDIT'
    NETWORK_FIREWALL = 'NETWORK_FIREWALL'
    DNS_FIREWALL = 'DNS_FIREWALL'


class ProtectionData(BaseModel):
    __root__: str


class IssueInfoMap(BaseModel):
    pass

    class Config:
        extra = Extra.allow


class MemberAccounts(BaseModel):
    __root__: List[AWSAccountId]


class ManagedServiceData(BaseModel):
    __root__: Annotated[str, Field(max_length=4096, min_length=1, regex='.*')]


class NetworkFirewallAction(BaseModel):
    __root__: Annotated[
        str, Field(max_length=128, min_length=1, regex='^[a-zA-Z0-9]+$')
    ]


class NetworkFirewallActionList(BaseModel):
    __root__: List[NetworkFirewallAction]


class NetworkFirewallMissingExpectedRTViolation(BaseModel):
    """
    Violation detail for Network Firewall for a subnet that's not associated to the expected Firewall Manager managed route table.
    """

    ViolationTarget: Optional[ViolationTarget] = None
    VPC: Optional[ResourceId] = None
    AvailabilityZone: Optional[LengthBoundedString] = None
    CurrentRouteTable: Optional[ResourceId] = None
    ExpectedRouteTable: Optional[ResourceId] = None


class NetworkFirewallMissingExpectedRoutesViolation(BaseModel):
    """
    Violation detail for an expected route missing in Network Firewall.
    """

    ViolationTarget: Optional[ViolationTarget] = None
    ExpectedRoutes: Optional[ExpectedRoutes] = None
    VpcId: Optional[ResourceId] = None


class TargetViolationReason(BaseModel):
    __root__: Annotated[str, Field(max_length=256, min_length=0, regex='\\w+')]


class NetworkFirewallMissingFirewallViolation(BaseModel):
    """
    Violation detail for Network Firewall for a subnet that doesn't have a Firewall Manager managed firewall in its VPC.
    """

    ViolationTarget: Optional[ViolationTarget] = None
    VPC: Optional[ResourceId] = None
    AvailabilityZone: Optional[LengthBoundedString] = None
    TargetViolationReason: Optional[TargetViolationReason] = None


class NetworkFirewallMissingSubnetViolation(NetworkFirewallMissingFirewallViolation):
    """
    Violation detail for Network Firewall for an Availability Zone that's missing the expected Firewall Manager managed subnet.
    """

    pass


class NetworkFirewallResourceName(BaseModel):
    __root__: Annotated[
        str, Field(max_length=128, min_length=1, regex='^[a-zA-Z0-9-]+$')
    ]


class ReferenceRule(ProtectionData):
    pass


class TargetViolationReasons(BaseModel):
    __root__: List[TargetViolationReason]


class PartialMatch(BaseModel):
    """
    The reference rule that partially matches the <code>ViolationTarget</code> rule and violation reason.
    """

    Reference: Optional[ReferenceRule] = None
    TargetViolationReasons: Optional[TargetViolationReasons] = None


class PolicyUpdateToken(ResourceId):
    pass


class SecurityServicePolicyData(BaseModel):
    """
    Details about the security service that is being used to protect the resources.
    """

    Type: SecurityServiceType
    ManagedServiceData: Optional[ManagedServiceData] = None


class ResourceTypeList(BaseModel):
    __root__: List[ResourceType]


class PolicyComplianceStatus(BaseModel):
    """
    Indicates whether the account is compliant with the specified policy. An account is considered noncompliant if it includes resources that are not protected by the policy, for WAF and Shield Advanced policies, or that are noncompliant with the policy, for security group policies.
    """

    PolicyOwner: Optional[AWSAccountId] = None
    PolicyId: Optional[PolicyId] = None
    PolicyName: Optional[ResourceName] = None
    MemberAccount: Optional[AWSAccountId] = None
    EvaluationResults: Optional[EvaluationResults] = None
    LastUpdated: Optional[TimeStamp] = None
    IssueInfoMap: Optional[IssueInfoMap] = None


class PolicySummary(BaseModel):
    """
    Details of the Firewall Manager policy.
    """

    PolicyArn: Optional[ResourceArn] = None
    PolicyId: Optional[PolicyId] = None
    PolicyName: Optional[ResourceName] = None
    ResourceType: Optional[ResourceType] = None
    SecurityServiceType: Optional[SecurityServiceType] = None
    RemediationEnabled: Optional[Boolean] = None
    DeleteUnusedFMManagedResources: Optional[Boolean] = None


class PreviousListVersion(BaseModel):
    __root__: Annotated[str, Field(max_length=2, min_length=1, regex='^\\d{1,2}$')]


class ProtocolsList(BaseModel):
    __root__: List[Protocol]


class PreviousProtocolsList(BaseModel):
    pass

    class Config:
        extra = Extra.allow


class ProtocolsListDataSummary(BaseModel):
    """
    Details of the Firewall Manager protocols list.
    """

    ListArn: Optional[ResourceArn] = None
    ListId: Optional[ListId] = None
    ListName: Optional[ResourceName] = None
    ProtocolsList: Optional[ProtocolsList] = None


class RemediationAction(BaseModel):
    """
    Information about an individual action you can take to remediate a violation.
    """

    Description: Optional[LengthBoundedString] = None
    EC2CreateRouteAction: Optional[EC2CreateRouteAction] = None
    EC2ReplaceRouteAction: Optional[EC2ReplaceRouteAction] = None
    EC2DeleteRouteAction: Optional[EC2DeleteRouteAction] = None
    EC2CopyRouteTableAction: Optional[EC2CopyRouteTableAction] = None
    EC2ReplaceRouteTableAssociationAction: Optional[
        EC2ReplaceRouteTableAssociationAction
    ] = None
    EC2AssociateRouteTableAction: Optional[EC2AssociateRouteTableAction] = None
    EC2CreateRouteTableAction: Optional[EC2CreateRouteTableAction] = None


class RemediationActionDescription(ViolationTarget):
    pass


class RemediationActionType(Enum):
    REMOVE = 'REMOVE'
    MODIFY = 'MODIFY'


class ResourceTagKey(ResourceName):
    pass


class ResourceTagValue(BaseModel):
    __root__: Annotated[
        str, Field(max_length=256, regex='^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-@]*)$')
    ]


class ResourceTag(BaseModel):
    """
    The resource tags that Firewall Manager uses to determine if a particular resource should be included or excluded from the Firewall Manager policy. Tags enable you to categorize your Amazon Web Services resources in different ways, for example, by purpose, owner, or environment. Each tag consists of a key and an optional value. Firewall Manager combines the tags with "AND" so that, if you add more than one tag to a policy scope, a resource must have all the specified tags to be included or excluded. For more information, see <a href="https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/tag-editor.html">Working with Tag Editor</a>.
    """

    Key: ResourceTagKey
    Value: Optional[ResourceTagValue] = None


class TargetType(Enum):
    GATEWAY = 'GATEWAY'
    CARRIER_GATEWAY = 'CARRIER_GATEWAY'
    INSTANCE = 'INSTANCE'
    LOCAL_GATEWAY = 'LOCAL_GATEWAY'
    NAT_GATEWAY = 'NAT_GATEWAY'
    NETWORK_INTERFACE = 'NETWORK_INTERFACE'
    VPC_ENDPOINT = 'VPC_ENDPOINT'
    VPC_PEERING_CONNECTION = 'VPC_PEERING_CONNECTION'
    EGRESS_ONLY_INTERNET_GATEWAY = 'EGRESS_ONLY_INTERNET_GATEWAY'
    TRANSIT_GATEWAY = 'TRANSIT_GATEWAY'


class SecurityGroupRuleDescription(BaseModel):
    """
    Describes a set of permissions for a security group rule.
    """

    IPV4Range: Optional[CIDR] = None
    IPV6Range: Optional[CIDR] = None
    PrefixListId: Optional[ResourceId] = None
    Protocol: Optional[LengthBoundedString] = None
    FromPort: Optional[IPPortNumber] = None
    ToPort: Optional[IPPortNumber] = None


class SecurityGroupRemediationAction(BaseModel):
    """
    Remediation option for the rule specified in the <code>ViolationTarget</code>.
    """

    RemediationActionType: Optional[RemediationActionType] = None
    Description: Optional[RemediationActionDescription] = None
    RemediationResult: Optional[SecurityGroupRuleDescription] = None
    IsDefaultAction: Optional[Boolean] = None


class StatefulRuleGroup(BaseModel):
    """
    Network Firewall stateful rule group, used in a <a>NetworkFirewallPolicyDescription</a>.
    """

    RuleGroupName: Optional[NetworkFirewallResourceName] = None
    ResourceId: Optional[ResourceId] = None


class StatelessRuleGroupPriority(BaseModel):
    __root__: Annotated[int, Field(ge=1.0, le=65535.0)]


class StatelessRuleGroup(BaseModel):
    """
    Network Firewall stateless rule group, used in a <a>NetworkFirewallPolicyDescription</a>.
    """

    RuleGroupName: Optional[NetworkFirewallResourceName] = None
    ResourceId: Optional[ResourceId] = None
    Priority: Optional[StatelessRuleGroupPriority] = None


class TagKey(ResourceName):
    pass


class TagValue(BaseModel):
    __root__: Annotated[
        str,
        Field(
            max_length=256, min_length=0, regex='^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-@]*)$'
        ),
    ]


class Tag(BaseModel):
    """
    A collection of key:value pairs associated with an Amazon Web Services resource. The key:value pair can be anything you define. Typically, the tag key represents a category (such as "environment") and the tag value represents a specific value within that category (such as "test," "development," or "production"). You can add up to 50 tags to each Amazon Web Services resource.
    """

    Key: TagKey
    Value: TagValue


class TagKeyList(BaseModel):
    __root__: Annotated[List[TagKey], Field(max_items=200, min_items=0)]


class AssociateAdminAccountRequest(BaseModel):
    AdminAccount: AWSAccountId


class DeleteAppsListRequest(BaseModel):
    ListId: ListId


class DeletePolicyRequest(BaseModel):
    PolicyId: PolicyId
    DeleteAllPolicyResources: Optional[Boolean] = None


class DeleteProtocolsListRequest(BaseModel):
    ListId: ListId


class GetAdminAccountResponse(BaseModel):
    AdminAccount: Optional[AWSAccountId] = None
    RoleStatus: Optional[AccountRoleStatus] = None


class GetAppsListResponse(BaseModel):
    AppsList: Optional[AppsListData] = None
    AppsListArn: Optional[ResourceArn] = None


class GetAppsListRequest(BaseModel):
    ListId: ListId
    DefaultList: Optional[Boolean] = None


class GetComplianceDetailRequest(BaseModel):
    PolicyId: PolicyId
    MemberAccount: AWSAccountId


class GetNotificationChannelResponse(BaseModel):
    SnsTopicArn: Optional[ResourceArn] = None
    SnsRoleName: Optional[ResourceArn] = None


class GetPolicyRequest(BaseModel):
    PolicyId: PolicyId


class GetProtectionStatusResponse(BaseModel):
    AdminAccountId: Optional[AWSAccountId] = None
    ServiceType: Optional[SecurityServiceType] = None
    Data: Optional[ProtectionData] = None
    NextToken: Optional[PaginationToken] = None


class GetProtectionStatusRequest(BaseModel):
    PolicyId: PolicyId
    MemberAccountId: Optional[AWSAccountId] = None
    StartTime: Optional[TimeStamp] = None
    EndTime: Optional[TimeStamp] = None
    NextToken: Optional[PaginationToken] = None
    MaxResults: Optional[PaginationMaxResults] = None


class GetProtocolsListRequest(BaseModel):
    ListId: ListId
    DefaultList: Optional[Boolean] = None


class GetViolationDetailsRequest(BaseModel):
    PolicyId: PolicyId
    MemberAccount: AWSAccountId
    ResourceId: ResourceId
    ResourceType: ResourceType


class ListAppsListsResponse(BaseModel):
    AppsLists: Optional[AppsListsData] = None
    NextToken: Optional[PaginationToken] = None


class ListAppsListsRequest(BaseModel):
    DefaultLists: Optional[Boolean] = None
    NextToken: Optional[PaginationToken] = None
    MaxResults: PaginationMaxResults


class ListComplianceStatusRequest(BaseModel):
    PolicyId: PolicyId
    NextToken: Optional[PaginationToken] = None
    MaxResults: Optional[PaginationMaxResults] = None


class ListMemberAccountsResponse(BaseModel):
    MemberAccounts: Optional[MemberAccounts] = None
    NextToken: Optional[PaginationToken] = None


class ListMemberAccountsRequest(BaseModel):
    NextToken: Optional[PaginationToken] = None
    MaxResults: Optional[PaginationMaxResults] = None


class ListPoliciesRequest(BaseModel):
    NextToken: Optional[PaginationToken] = None
    MaxResults: Optional[PaginationMaxResults] = None


class ListProtocolsListsRequest(BaseModel):
    DefaultLists: Optional[Boolean] = None
    NextToken: Optional[PaginationToken] = None
    MaxResults: PaginationMaxResults


class ListTagsForResourceRequest(BaseModel):
    ResourceArn: ResourceArn


class PutAppsListResponse(GetAppsListResponse):
    pass


class PutNotificationChannelRequest(BaseModel):
    SnsTopicArn: ResourceArn
    SnsRoleName: ResourceArn


class UntagResourceRequest(BaseModel):
    ResourceArn: ResourceArn
    TagKeys: TagKeyList


class AwsEc2NetworkInterfaceViolations(BaseModel):
    __root__: List[AwsEc2NetworkInterfaceViolation]


class AwsEc2InstanceViolation(BaseModel):
    """
    Violation detail for an EC2 instance resource.
    """

    ViolationTarget: Optional[ViolationTarget] = None
    AwsEc2NetworkInterfaceViolations: Optional[AwsEc2NetworkInterfaceViolations] = None


class PartialMatches(BaseModel):
    __root__: List[PartialMatch]


class SecurityGroupRemediationActions(BaseModel):
    __root__: List[SecurityGroupRemediationAction]


class AwsVPCSecurityGroupViolation(BaseModel):
    """
    Violation detail for the rule violation in a security group when compared to the primary security group of the Firewall Manager policy.
    """

    ViolationTarget: Optional[ViolationTarget] = None
    ViolationTargetDescription: Optional[LengthBoundedString] = None
    PartialMatches: Optional[PartialMatches] = None
    PossibleSecurityGroupRemediationActions: Optional[
        SecurityGroupRemediationActions
    ] = None


class PolicyComplianceDetail(BaseModel):
    """
    Describes the noncompliant resources in a member account for a specific Firewall Manager policy. A maximum of 100 entries are displayed. If more than 100 resources are noncompliant, <code>EvaluationLimitExceeded</code> is set to <code>True</code>.
    """

    PolicyOwner: Optional[AWSAccountId] = None
    PolicyId: Optional[PolicyId] = None
    MemberAccount: Optional[AWSAccountId] = None
    Violators: Optional[ComplianceViolators] = None
    EvaluationLimitExceeded: Optional[Boolean] = None
    ExpiredAt: Optional[TimeStamp] = None
    IssueInfoMap: Optional[IssueInfoMap] = None


class ProtocolsListData(BaseModel):
    """
    An Firewall Manager protocols list.
    """

    ListId: Optional[ListId] = None
    ListName: ResourceName
    ListUpdateToken: Optional[UpdateToken] = None
    CreateTime: Optional[TimeStamp] = None
    LastUpdateTime: Optional[TimeStamp] = None
    ProtocolsList: ProtocolsList
    PreviousProtocolsList: Optional[PreviousProtocolsList] = None


class PolicyComplianceStatusList(BaseModel):
    __root__: List[PolicyComplianceStatus]


class PolicySummaryList(BaseModel):
    __root__: List[PolicySummary]


class ProtocolsListsData(BaseModel):
    __root__: List[ProtocolsListDataSummary]


class TagList(BaseModel):
    __root__: Annotated[List[Tag], Field(max_items=200, min_items=0)]


class Route(BaseModel):
    """
    Describes a route in a route table.
    """

    DestinationType: Optional[DestinationType] = None
    TargetType: Optional[TargetType] = None
    Destination: Optional[LengthBoundedString] = None
    Target: Optional[LengthBoundedString] = None


class StatelessRuleGroupList(BaseModel):
    __root__: List[StatelessRuleGroup]


class StatefulRuleGroupList(BaseModel):
    __root__: List[StatefulRuleGroup]


class NetworkFirewallPolicyDescription(BaseModel):
    """
    The definition of the Network Firewall firewall policy.
    """

    StatelessRuleGroups: Optional[StatelessRuleGroupList] = None
    StatelessDefaultActions: Optional[NetworkFirewallActionList] = None
    StatelessFragmentDefaultActions: Optional[NetworkFirewallActionList] = None
    StatelessCustomActions: Optional[NetworkFirewallActionList] = None
    StatefulRuleGroups: Optional[StatefulRuleGroupList] = None


class NetworkFirewallPolicyModifiedViolation(BaseModel):
    """
    Violation detail for Network Firewall for a firewall policy that has a different <a>NetworkFirewallPolicyDescription</a> than is required by the Firewall Manager policy.
    """

    ViolationTarget: Optional[ViolationTarget] = None
    CurrentPolicyDescription: Optional[NetworkFirewallPolicyDescription] = None
    ExpectedPolicyDescription: Optional[NetworkFirewallPolicyDescription] = None


class RemediationActionWithOrder(BaseModel):
    """
    An ordered list of actions you can take to remediate a violation.
    """

    RemediationAction: Optional[RemediationAction] = None
    Order: Optional[BasicInteger] = None


class OrderedRemediationActions(BaseModel):
    __root__: List[RemediationActionWithOrder]


class ResourceTags(BaseModel):
    __root__: Annotated[List[ResourceTag], Field(max_items=8, min_items=0)]


class PossibleRemediationAction(BaseModel):
    """
    A list of remediation actions.
    """

    Description: Optional[LengthBoundedString] = None
    OrderedRemediationActions: OrderedRemediationActions
    IsDefaultAction: Optional[Boolean] = None


class PossibleRemediationActionList(BaseModel):
    __root__: List[PossibleRemediationAction]


class PossibleRemediationActions(BaseModel):
    """
    A list of possible remediation action lists. Each individual possible remediation action is a list of individual remediation actions.
    """

    Description: Optional[LengthBoundedString] = None
    Actions: Optional[PossibleRemediationActionList] = None


class GetComplianceDetailResponse(BaseModel):
    PolicyComplianceDetail: Optional[PolicyComplianceDetail] = None


class GetProtocolsListResponse(BaseModel):
    ProtocolsList: Optional[ProtocolsListData] = None
    ProtocolsListArn: Optional[ResourceArn] = None


class ListComplianceStatusResponse(BaseModel):
    PolicyComplianceStatusList: Optional[PolicyComplianceStatusList] = None
    NextToken: Optional[PaginationToken] = None


class ListPoliciesResponse(BaseModel):
    PolicyList: Optional[PolicySummaryList] = None
    NextToken: Optional[PaginationToken] = None


class ListProtocolsListsResponse(BaseModel):
    ProtocolsLists: Optional[ProtocolsListsData] = None
    NextToken: Optional[PaginationToken] = None


class ListTagsForResourceResponse(BaseModel):
    TagList: Optional[TagList] = None


class PutAppsListRequest(BaseModel):
    AppsList: AppsListData
    TagList: Optional[TagList] = None


class PutProtocolsListResponse(GetProtocolsListResponse):
    pass


class PutProtocolsListRequest(BaseModel):
    ProtocolsList: ProtocolsListData
    TagList: Optional[TagList] = None


class TagResourceRequest(BaseModel):
    ResourceArn: ResourceArn
    TagList: TagList


class Policy(BaseModel):
    """
    An Firewall Manager policy.
    """

    PolicyId: Optional[PolicyId] = None
    PolicyName: ResourceName
    PolicyUpdateToken: Optional[PolicyUpdateToken] = None
    SecurityServicePolicyData: SecurityServicePolicyData
    ResourceType: ResourceType
    ResourceTypeList: Optional[ResourceTypeList] = None
    ResourceTags: Optional[ResourceTags] = None
    ExcludeResourceTags: Boolean
    RemediationEnabled: Boolean
    DeleteUnusedFMManagedResources: Optional[Boolean] = None
    IncludeMap: Optional[CustomerPolicyScopeMap] = None
    ExcludeMap: Optional[CustomerPolicyScopeMap] = None


class Routes(BaseModel):
    __root__: List[Route]


class NetworkFirewallBlackHoleRouteDetectedViolation(BaseModel):
    """
    Violation detail for an internet gateway route with an inactive state in the customer subnet route table or Network Firewall subnet route table.
    """

    ViolationTarget: Optional[ViolationTarget] = None
    RouteTableId: Optional[ResourceId] = None
    VpcId: Optional[ResourceId] = None
    ViolatingRoutes: Optional[Routes] = None


class NetworkFirewallInternetTrafficNotInspectedViolation(BaseModel):
    """
    Violation detail for the subnet for which internet traffic that hasn't been inspected.
    """

    SubnetId: Optional[ResourceId] = None
    SubnetAvailabilityZone: Optional[LengthBoundedString] = None
    RouteTableId: Optional[ResourceId] = None
    ViolatingRoutes: Optional[Routes] = None
    IsRouteTableUsedInDifferentAZ: Optional[Boolean] = None
    CurrentFirewallSubnetRouteTable: Optional[ResourceId] = None
    ExpectedFirewallEndpoint: Optional[ResourceId] = None
    FirewallSubnetId: Optional[ResourceId] = None
    ExpectedFirewallSubnetRoutes: Optional[ExpectedRoutes] = None
    ActualFirewallSubnetRoutes: Optional[Routes] = None
    InternetGatewayId: Optional[ResourceId] = None
    CurrentInternetGatewayRouteTable: Optional[ResourceId] = None
    ExpectedInternetGatewayRoutes: Optional[ExpectedRoutes] = None
    ActualInternetGatewayRoutes: Optional[Routes] = None
    VpcId: Optional[ResourceId] = None


class NetworkFirewallInvalidRouteConfigurationViolation(BaseModel):
    """
    Violation detail for the improperly configured subnet route. It's possible there is a missing route table route, or a configuration that causes traffic to cross an Availability Zone boundary.
    """

    AffectedSubnets: Optional[ResourceIdList] = None
    RouteTableId: Optional[ResourceId] = None
    IsRouteTableUsedInDifferentAZ: Optional[Boolean] = None
    ViolatingRoute: Optional[Route] = None
    CurrentFirewallSubnetRouteTable: Optional[ResourceId] = None
    ExpectedFirewallEndpoint: Optional[ResourceId] = None
    ActualFirewallEndpoint: Optional[ResourceId] = None
    ExpectedFirewallSubnetId: Optional[ResourceId] = None
    ActualFirewallSubnetId: Optional[ResourceId] = None
    ExpectedFirewallSubnetRoutes: Optional[ExpectedRoutes] = None
    ActualFirewallSubnetRoutes: Optional[Routes] = None
    InternetGatewayId: Optional[ResourceId] = None
    CurrentInternetGatewayRouteTable: Optional[ResourceId] = None
    ExpectedInternetGatewayRoutes: Optional[ExpectedRoutes] = None
    ActualInternetGatewayRoutes: Optional[Routes] = None
    VpcId: Optional[ResourceId] = None


class NetworkFirewallUnexpectedFirewallRoutesViolation(BaseModel):
    """
    Violation detail for an unexpected route that's present in a route table.
    """

    FirewallSubnetId: Optional[ResourceId] = None
    ViolatingRoutes: Optional[Routes] = None
    RouteTableId: Optional[ResourceId] = None
    FirewallEndpoint: Optional[ResourceId] = None
    VpcId: Optional[ResourceId] = None


class NetworkFirewallUnexpectedGatewayRoutesViolation(BaseModel):
    """
    Violation detail for an unexpected gateway route that???s present in a route table.
    """

    GatewayId: Optional[ResourceId] = None
    ViolatingRoutes: Optional[Routes] = None
    RouteTableId: Optional[ResourceId] = None
    VpcId: Optional[ResourceId] = None


class ResourceViolation(BaseModel):
    """
    Violation detail based on resource type.
    """

    AwsVPCSecurityGroupViolation: Optional[AwsVPCSecurityGroupViolation] = None
    AwsEc2NetworkInterfaceViolation: Optional[AwsEc2NetworkInterfaceViolation] = None
    AwsEc2InstanceViolation: Optional[AwsEc2InstanceViolation] = None
    NetworkFirewallMissingFirewallViolation: Optional[
        NetworkFirewallMissingFirewallViolation
    ] = None
    NetworkFirewallMissingSubnetViolation: Optional[
        NetworkFirewallMissingSubnetViolation
    ] = None
    NetworkFirewallMissingExpectedRTViolation: Optional[
        NetworkFirewallMissingExpectedRTViolation
    ] = None
    NetworkFirewallPolicyModifiedViolation: Optional[
        NetworkFirewallPolicyModifiedViolation
    ] = None
    NetworkFirewallInternetTrafficNotInspectedViolation: Optional[
        NetworkFirewallInternetTrafficNotInspectedViolation
    ] = None
    NetworkFirewallInvalidRouteConfigurationViolation: Optional[
        NetworkFirewallInvalidRouteConfigurationViolation
    ] = None
    NetworkFirewallBlackHoleRouteDetectedViolation: Optional[
        NetworkFirewallBlackHoleRouteDetectedViolation
    ] = None
    NetworkFirewallUnexpectedFirewallRoutesViolation: Optional[
        NetworkFirewallUnexpectedFirewallRoutesViolation
    ] = None
    NetworkFirewallUnexpectedGatewayRoutesViolation: Optional[
        NetworkFirewallUnexpectedGatewayRoutesViolation
    ] = None
    NetworkFirewallMissingExpectedRoutesViolation: Optional[
        NetworkFirewallMissingExpectedRoutesViolation
    ] = None
    DnsRuleGroupPriorityConflictViolation: Optional[
        DnsRuleGroupPriorityConflictViolation
    ] = None
    DnsDuplicateRuleGroupViolation: Optional[DnsDuplicateRuleGroupViolation] = None
    DnsRuleGroupLimitExceededViolation: Optional[
        DnsRuleGroupLimitExceededViolation
    ] = None
    PossibleRemediationActions: Optional[PossibleRemediationActions] = None


class ResourceViolations(BaseModel):
    __root__: List[ResourceViolation]


class GetPolicyResponse(BaseModel):
    Policy: Optional[Policy] = None
    PolicyArn: Optional[ResourceArn] = None


class PutPolicyResponse(GetPolicyResponse):
    pass


class PutPolicyRequest(BaseModel):
    Policy: Policy
    TagList: Optional[TagList] = None


class ViolationDetail(BaseModel):
    """
    Violations for a resource based on the specified Firewall Manager policy and Amazon Web Services account.
    """

    PolicyId: PolicyId
    MemberAccount: AWSAccountId
    ResourceId: ResourceId
    ResourceType: ResourceType
    ResourceViolations: ResourceViolations
    ResourceTags: Optional[TagList] = None
    ResourceDescription: Optional[LengthBoundedString] = None


class GetViolationDetailsResponse(BaseModel):
    ViolationDetail: Optional[ViolationDetail] = None
