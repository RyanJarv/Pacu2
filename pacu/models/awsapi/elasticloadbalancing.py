# generated by datamodel-codegen:
#   filename:  openapi.yaml
#   timestamp: 2021-12-31T02:49:01+00:00

from __future__ import annotations

from datetime import datetime
from typing import Annotated, Any, List, Optional

from pydantic import BaseModel, Field


class AddTagsOutput(BaseModel):
    """
    Contains the output of AddTags.
    """

    pass


class AccessPointName(BaseModel):
    __root__: str


class AccessPointNotFoundException(BaseModel):
    __root__: Any


class TooManyTagsException(AccessPointNotFoundException):
    pass


class DuplicateTagKeysException(AccessPointNotFoundException):
    pass


class SecurityGroupId(AccessPointName):
    pass


class InvalidConfigurationRequestException(AccessPointNotFoundException):
    pass


class InvalidSecurityGroupException(AccessPointNotFoundException):
    pass


class SubnetId(AccessPointName):
    pass


class SubnetNotFoundException(AccessPointNotFoundException):
    pass


class InvalidSubnetException(AccessPointNotFoundException):
    pass


class HealthCheckTarget(AccessPointName):
    pass


class HealthCheckInterval(BaseModel):
    __root__: Annotated[int, Field(ge=5.0, le=300.0)]


class HealthCheckTimeout(BaseModel):
    __root__: Annotated[int, Field(ge=2.0, le=60.0)]


class UnhealthyThreshold(BaseModel):
    __root__: Annotated[int, Field(ge=2.0, le=10.0)]


class HealthyThreshold(UnhealthyThreshold):
    pass


class CreateAppCookieStickinessPolicyOutput(AddTagsOutput):
    """
    Contains the output for CreateAppCookieStickinessPolicy.
    """

    pass


class DuplicatePolicyNameException(AccessPointNotFoundException):
    pass


class TooManyPoliciesException(AccessPointNotFoundException):
    pass


class CreateLBCookieStickinessPolicyOutput(AddTagsOutput):
    """
    Contains the output for CreateLBCookieStickinessPolicy.
    """

    pass


class AvailabilityZone(AccessPointName):
    pass


class DuplicateAccessPointNameException(AccessPointNotFoundException):
    pass


class TooManyAccessPointsException(AccessPointNotFoundException):
    pass


class CertificateNotFoundException(AccessPointNotFoundException):
    pass


class InvalidSchemeException(AccessPointNotFoundException):
    pass


class UnsupportedProtocolException(AccessPointNotFoundException):
    pass


class OperationNotPermittedException(AccessPointNotFoundException):
    pass


class CreateLoadBalancerListenerOutput(AddTagsOutput):
    """
    Contains the parameters for CreateLoadBalancerListener.
    """

    pass


class DuplicateListenerException(AccessPointNotFoundException):
    pass


class CreateLoadBalancerPolicyOutput(AddTagsOutput):
    """
    Contains the output of CreateLoadBalancerPolicy.
    """

    pass


class PolicyTypeNotFoundException(AccessPointNotFoundException):
    pass


class DeleteAccessPointOutput(AddTagsOutput):
    """
    Contains the output of DeleteLoadBalancer.
    """

    pass


class DeleteLoadBalancerListenerOutput(AddTagsOutput):
    """
    Contains the output of DeleteLoadBalancerListeners.
    """

    pass


class AccessPointPort(BaseModel):
    __root__: int


class DeleteLoadBalancerPolicyOutput(AddTagsOutput):
    """
    Contains the output of DeleteLoadBalancerPolicy.
    """

    pass


class InvalidEndPointException(AccessPointNotFoundException):
    pass


class LoadBalancerAttributeNotFoundException(AccessPointNotFoundException):
    pass


class PolicyName(AccessPointName):
    pass


class PolicyNotFoundException(AccessPointNotFoundException):
    pass


class PolicyTypeName(AccessPointName):
    pass


class DependencyThrottleException(AccessPointNotFoundException):
    pass


class RemoveTagsOutput(AddTagsOutput):
    """
    Contains the output of RemoveTags.
    """

    pass


class SetLoadBalancerListenerSSLCertificateOutput(AddTagsOutput):
    """
    Contains the output of SetLoadBalancerListenerSSLCertificate.
    """

    pass


class ListenerNotFoundException(AccessPointNotFoundException):
    pass


class SetLoadBalancerPoliciesForBackendServerOutput(AddTagsOutput):
    """
    Contains the output of SetLoadBalancerPoliciesForBackendServer.
    """

    pass


class SetLoadBalancerPoliciesOfListenerOutput(AddTagsOutput):
    """
    Contains the output of SetLoadBalancePoliciesOfListener.
    """

    pass


class AccessLogEnabled(BaseModel):
    __root__: bool


class S3BucketName(AccessPointName):
    pass


class AccessLogInterval(AccessPointPort):
    pass


class AccessLogPrefix(AccessPointName):
    pass


class AvailabilityZones(BaseModel):
    __root__: List[AvailabilityZone]


class AddAvailabilityZonesInput(BaseModel):
    """
    Contains the parameters for EnableAvailabilityZonesForLoadBalancer.
    """

    LoadBalancerName: AccessPointName
    AvailabilityZones: AvailabilityZones


class LoadBalancerNames(BaseModel):
    __root__: List[AccessPointName]


class AdditionalAttributeKey(BaseModel):
    __root__: Annotated[str, Field(max_length=256, regex='^[a-zA-Z0-9.]+$')]


class AdditionalAttributeValue(AdditionalAttributeKey):
    pass


class AdditionalAttribute(BaseModel):
    """
    Information about additional load balancer attributes.
    """

    Key: Optional[AdditionalAttributeKey] = None
    Value: Optional[AdditionalAttributeValue] = None


class CookieName(AccessPointName):
    pass


class SecurityGroups(BaseModel):
    __root__: List[SecurityGroupId]


class ApplySecurityGroupsToLoadBalancerInput(BaseModel):
    """
    Contains the parameters for ApplySecurityGroupsToLoadBalancer.
    """

    LoadBalancerName: AccessPointName
    SecurityGroups: SecurityGroups


class Subnets(BaseModel):
    __root__: List[SubnetId]


class AttachLoadBalancerToSubnetsInput(BaseModel):
    """
    Contains the parameters for AttachLoaBalancerToSubnets.
    """

    LoadBalancerName: AccessPointName
    Subnets: Subnets


class AttributeName(AccessPointName):
    pass


class AttributeType(AccessPointName):
    pass


class AttributeValue(AccessPointName):
    pass


class InstancePort(BaseModel):
    __root__: Annotated[int, Field(ge=1.0, le=65535.0)]


class PolicyNames(BaseModel):
    __root__: List[PolicyName]


class BackendServerDescription(BaseModel):
    """
    Information about the configuration of an EC2 instance.
    """

    InstancePort: Optional[InstancePort] = None
    PolicyNames: Optional[PolicyNames] = None


class BackendServerDescriptions(BaseModel):
    __root__: List[BackendServerDescription]


class Cardinality(AccessPointName):
    pass


class HealthCheck(BaseModel):
    """
    Information about a health check.
    """

    Target: HealthCheckTarget
    Interval: HealthCheckInterval
    Timeout: HealthCheckTimeout
    UnhealthyThreshold: UnhealthyThreshold
    HealthyThreshold: HealthyThreshold


class ConfigureHealthCheckInput(BaseModel):
    """
    Contains the parameters for ConfigureHealthCheck.
    """

    LoadBalancerName: AccessPointName
    HealthCheck: HealthCheck


class ConnectionDrainingEnabled(AccessLogEnabled):
    pass


class ConnectionDrainingTimeout(AccessPointPort):
    pass


class IdleTimeout(BaseModel):
    __root__: Annotated[int, Field(ge=1.0, le=3600.0)]


class CookieExpirationPeriod(AccessPointPort):
    pass


class LoadBalancerScheme(AccessPointName):
    pass


class DNSName(AccessPointName):
    pass


class CreateAppCookieStickinessPolicyInput(BaseModel):
    """
    Contains the parameters for CreateAppCookieStickinessPolicy.
    """

    LoadBalancerName: AccessPointName
    PolicyName: PolicyName
    CookieName: CookieName


class CreateLBCookieStickinessPolicyInput(BaseModel):
    """
    Contains the parameters for CreateLBCookieStickinessPolicy.
    """

    LoadBalancerName: AccessPointName
    PolicyName: PolicyName
    CookieExpirationPeriod: Optional[CookieExpirationPeriod] = None


class CreatedTime(BaseModel):
    __root__: datetime


class CrossZoneLoadBalancingEnabled(AccessLogEnabled):
    pass


class DefaultValue(AccessPointName):
    pass


class DeleteAccessPointInput(BaseModel):
    """
    Contains the parameters for DeleteLoadBalancer.
    """

    LoadBalancerName: AccessPointName


class Ports(BaseModel):
    __root__: List[AccessPointPort]


class DeleteLoadBalancerListenerInput(BaseModel):
    """
    Contains the parameters for DeleteLoadBalancerListeners.
    """

    LoadBalancerName: AccessPointName
    LoadBalancerPorts: Ports


class DeleteLoadBalancerPolicyInput(BaseModel):
    """
    Contains the parameters for DeleteLoadBalancerPolicy.
    """

    LoadBalancerName: AccessPointName
    PolicyName: PolicyName


class Marker(AccessPointName):
    pass


class PageSize(BaseModel):
    __root__: Annotated[int, Field(ge=1.0, le=400.0)]


class DescribeAccessPointsInput(BaseModel):
    """
    Contains the parameters for DescribeLoadBalancers.
    """

    LoadBalancerNames: Optional[LoadBalancerNames] = None
    Marker: Optional[Marker] = None
    PageSize: Optional[PageSize] = None


class DescribeAccountLimitsInput(BaseModel):
    Marker: Optional[Marker] = None
    PageSize: Optional[PageSize] = None


class DescribeLoadBalancerAttributesInput(BaseModel):
    """
    Contains the parameters for DescribeLoadBalancerAttributes.
    """

    LoadBalancerName: AccessPointName


class DescribeLoadBalancerPoliciesInput(BaseModel):
    """
    Contains the parameters for DescribeLoadBalancerPolicies.
    """

    LoadBalancerName: Optional[AccessPointName] = None
    PolicyNames: Optional[PolicyNames] = None


class PolicyTypeNames(BaseModel):
    __root__: List[PolicyTypeName]


class DescribeLoadBalancerPolicyTypesInput(BaseModel):
    """
    Contains the parameters for DescribeLoadBalancerPolicyTypes.
    """

    PolicyTypeNames: Optional[PolicyTypeNames] = None


class LoadBalancerNamesMax20(BaseModel):
    __root__: Annotated[List[AccessPointName], Field(max_items=20, min_items=1)]


class DescribeTagsInput(BaseModel):
    """
    Contains the parameters for DescribeTags.
    """

    LoadBalancerNames: LoadBalancerNamesMax20


class Description(AccessPointName):
    pass


class DetachLoadBalancerFromSubnetsInput(BaseModel):
    """
    Contains the parameters for DetachLoadBalancerFromSubnets.
    """

    LoadBalancerName: AccessPointName
    Subnets: Subnets


class EndPointPort(AccessPointPort):
    pass


class InstanceId(AccessPointName):
    pass


class State(AccessPointName):
    pass


class ReasonCode(AccessPointName):
    pass


class InstanceState(BaseModel):
    """
    Information about the state of an EC2 instance.
    """

    InstanceId: Optional[InstanceId] = None
    State: Optional[State] = None
    ReasonCode: Optional[ReasonCode] = None
    Description: Optional[Description] = None


class LBCookieStickinessPolicy(BaseModel):
    """
    Information about a policy for duration-based session stickiness.
    """

    PolicyName: Optional[PolicyName] = None
    CookieExpirationPeriod: Optional[CookieExpirationPeriod] = None


class LBCookieStickinessPolicies(BaseModel):
    __root__: List[LBCookieStickinessPolicy]


class Name(AccessPointName):
    pass


class Max(AccessPointName):
    pass


class Limit(BaseModel):
    """
    Information about an Elastic Load Balancing resource limit for your AWS account.
    """

    Name: Optional[Name] = None
    Max: Optional[Max] = None


class Protocol(AccessPointName):
    pass


class SSLCertificateId(AccessPointName):
    pass


class VPCId(AccessPointName):
    pass


class PolicyAttributeDescription(BaseModel):
    """
    Information about a policy attribute.
    """

    AttributeName: Optional[AttributeName] = None
    AttributeValue: Optional[AttributeValue] = None


class PolicyAttributeDescriptions(BaseModel):
    __root__: List[PolicyAttributeDescription]


class PolicyAttributeTypeDescription(BaseModel):
    """
    Information about a policy attribute type.
    """

    AttributeName: Optional[AttributeName] = None
    AttributeType: Optional[AttributeType] = None
    Description: Optional[Description] = None
    DefaultValue: Optional[DefaultValue] = None
    Cardinality: Optional[Cardinality] = None


class PolicyAttributeTypeDescriptions(BaseModel):
    __root__: List[PolicyAttributeTypeDescription]


class PolicyDescription(BaseModel):
    """
    Information about a policy.
    """

    PolicyName: Optional[PolicyName] = None
    PolicyTypeName: Optional[PolicyTypeName] = None
    PolicyAttributeDescriptions: Optional[PolicyAttributeDescriptions] = None


class PolicyTypeDescription(BaseModel):
    """
    Information about a policy type.
    """

    PolicyTypeName: Optional[PolicyTypeName] = None
    Description: Optional[Description] = None
    PolicyAttributeTypeDescriptions: Optional[PolicyAttributeTypeDescriptions] = None


class RemoveAvailabilityZonesInput(BaseModel):
    """
    Contains the parameters for DisableAvailabilityZonesForLoadBalancer.
    """

    LoadBalancerName: AccessPointName
    AvailabilityZones: AvailabilityZones


class SecurityGroupName(AccessPointName):
    pass


class SecurityGroupOwnerAlias(AccessPointName):
    pass


class SetLoadBalancerListenerSSLCertificateInput(BaseModel):
    """
    Contains the parameters for SetLoadBalancerListenerSSLCertificate.
    """

    LoadBalancerName: AccessPointName
    LoadBalancerPort: AccessPointPort
    SSLCertificateId: SSLCertificateId


class SetLoadBalancerPoliciesForBackendServerInput(BaseModel):
    """
    Contains the parameters for SetLoadBalancerPoliciesForBackendServer.
    """

    LoadBalancerName: AccessPointName
    InstancePort: EndPointPort
    PolicyNames: PolicyNames


class SetLoadBalancerPoliciesOfListenerInput(BaseModel):
    """
    Contains the parameters for SetLoadBalancePoliciesOfListener.
    """

    LoadBalancerName: AccessPointName
    LoadBalancerPort: AccessPointPort
    PolicyNames: PolicyNames


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
    Information about a tag.
    """

    Key: TagKey
    Value: Optional[TagValue] = None


class ApplySecurityGroupsToLoadBalancerOutput(BaseModel):
    """
    Contains the output of ApplySecurityGroupsToLoadBalancer.
    """

    SecurityGroups: Optional[SecurityGroups] = None


class AttachLoadBalancerToSubnetsOutput(BaseModel):
    """
    Contains the output of AttachLoadBalancerToSubnets.
    """

    Subnets: Optional[Subnets] = None


class ConfigureHealthCheckOutput(BaseModel):
    """
    Contains the output of ConfigureHealthCheck.
    """

    HealthCheck: Optional[HealthCheck] = None


class CreateAccessPointOutput(BaseModel):
    """
    Contains the output for CreateLoadBalancer.
    """

    DNSName: Optional[DNSName] = None


class Listener(BaseModel):
    """
    <p>Information about a listener.</p> <p>For information about the protocols and the ports supported by Elastic Load Balancing, see <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-listener-config.html">Listeners for Your Classic Load Balancer</a> in the <i>Classic Load Balancers Guide</i>.</p>
    """

    Protocol: Protocol
    LoadBalancerPort: AccessPointPort
    InstanceProtocol: Optional[Protocol] = None
    InstancePort: InstancePort
    SSLCertificateId: Optional[SSLCertificateId] = None


class PolicyAttribute(PolicyAttributeDescription):
    """
    Information about a policy attribute.
    """

    pass


class Instance(BaseModel):
    """
    The ID of an EC2 instance.
    """

    InstanceId: Optional[InstanceId] = None


class DetachLoadBalancerFromSubnetsOutput(AttachLoadBalancerToSubnetsOutput):
    """
    Contains the output of DetachLoadBalancerFromSubnets.
    """

    pass


class RemoveAvailabilityZonesOutput(BaseModel):
    """
    Contains the output for DisableAvailabilityZonesForLoadBalancer.
    """

    AvailabilityZones: Optional[AvailabilityZones] = None


class AddAvailabilityZonesOutput(RemoveAvailabilityZonesOutput):
    """
    Contains the output of EnableAvailabilityZonesForLoadBalancer.
    """

    pass


class CrossZoneLoadBalancing(BaseModel):
    """
    Information about the <code>CrossZoneLoadBalancing</code> attribute.
    """

    Enabled: CrossZoneLoadBalancingEnabled


class AccessLog(BaseModel):
    """
    Information about the <code>AccessLog</code> attribute.
    """

    Enabled: AccessLogEnabled
    S3BucketName: Optional[S3BucketName] = None
    EmitInterval: Optional[AccessLogInterval] = None
    S3BucketPrefix: Optional[AccessLogPrefix] = None


class ConnectionDraining(BaseModel):
    """
    Information about the <code>ConnectionDraining</code> attribute.
    """

    Enabled: ConnectionDrainingEnabled
    Timeout: Optional[ConnectionDrainingTimeout] = None


class ConnectionSettings(BaseModel):
    """
    Information about the <code>ConnectionSettings</code> attribute.
    """

    IdleTimeout: IdleTimeout


class AdditionalAttributes(BaseModel):
    __root__: Annotated[List[AdditionalAttribute], Field(max_items=10)]


class TagKeyOnly(BaseModel):
    """
    The key of a tag.
    """

    Key: Optional[TagKey] = None


class TagList(BaseModel):
    __root__: Annotated[List[Tag], Field(min_items=1)]


class AddTagsInput(BaseModel):
    """
    Contains the parameters for AddTags.
    """

    LoadBalancerNames: LoadBalancerNames
    Tags: TagList


class AppCookieStickinessPolicy(BaseModel):
    """
    Information about a policy for application-controlled session stickiness.
    """

    PolicyName: Optional[PolicyName] = None
    CookieName: Optional[CookieName] = None


class AppCookieStickinessPolicies(BaseModel):
    __root__: List[AppCookieStickinessPolicy]


class Listeners(BaseModel):
    __root__: List[Listener]


class CreateAccessPointInput(BaseModel):
    """
    Contains the parameters for CreateLoadBalancer.
    """

    LoadBalancerName: AccessPointName
    Listeners: Listeners
    AvailabilityZones: Optional[AvailabilityZones] = None
    Subnets: Optional[Subnets] = None
    SecurityGroups: Optional[SecurityGroups] = None
    Scheme: Optional[LoadBalancerScheme] = None
    Tags: Optional[TagList] = None


class CreateLoadBalancerListenerInput(BaseModel):
    """
    Contains the parameters for CreateLoadBalancerListeners.
    """

    LoadBalancerName: AccessPointName
    Listeners: Listeners


class PolicyAttributes(BaseModel):
    __root__: List[PolicyAttribute]


class CreateLoadBalancerPolicyInput(BaseModel):
    """
    Contains the parameters for CreateLoadBalancerPolicy.
    """

    LoadBalancerName: AccessPointName
    PolicyName: PolicyName
    PolicyTypeName: PolicyTypeName
    PolicyAttributes: Optional[PolicyAttributes] = None


class Instances(BaseModel):
    __root__: List[Instance]


class DeregisterEndPointsInput(BaseModel):
    """
    Contains the parameters for DeregisterInstancesFromLoadBalancer.
    """

    LoadBalancerName: AccessPointName
    Instances: Instances


class Limits(BaseModel):
    __root__: List[Limit]


class DescribeEndPointStateInput(BaseModel):
    """
    Contains the parameters for DescribeInstanceHealth.
    """

    LoadBalancerName: AccessPointName
    Instances: Optional[Instances] = None


class InstanceStates(BaseModel):
    __root__: List[InstanceState]


class LoadBalancerAttributes(BaseModel):
    """
    The attributes for a load balancer.
    """

    CrossZoneLoadBalancing: Optional[CrossZoneLoadBalancing] = None
    AccessLog: Optional[AccessLog] = None
    ConnectionDraining: Optional[ConnectionDraining] = None
    ConnectionSettings: Optional[ConnectionSettings] = None
    AdditionalAttributes: Optional[AdditionalAttributes] = None


class PolicyDescriptions(BaseModel):
    __root__: List[PolicyDescription]


class PolicyTypeDescriptions(BaseModel):
    __root__: List[PolicyTypeDescription]


class ListenerDescription(BaseModel):
    """
    The policies enabled for a listener.
    """

    Listener: Optional[Listener] = None
    PolicyNames: Optional[PolicyNames] = None


class ListenerDescriptions(BaseModel):
    __root__: List[ListenerDescription]


class Policies(BaseModel):
    """
    The policies for a load balancer.
    """

    AppCookieStickinessPolicies: Optional[AppCookieStickinessPolicies] = None
    LBCookieStickinessPolicies: Optional[LBCookieStickinessPolicies] = None
    OtherPolicies: Optional[PolicyNames] = None


class SourceSecurityGroup(BaseModel):
    """
    Information about a source security group.
    """

    OwnerAlias: Optional[SecurityGroupOwnerAlias] = None
    GroupName: Optional[SecurityGroupName] = None


class LoadBalancerDescription(BaseModel):
    """
    Information about a load balancer.
    """

    LoadBalancerName: Optional[AccessPointName] = None
    DNSName: Optional[DNSName] = None
    CanonicalHostedZoneName: Optional[DNSName] = None
    CanonicalHostedZoneNameID: Optional[DNSName] = None
    ListenerDescriptions: Optional[ListenerDescriptions] = None
    Policies: Optional[Policies] = None
    BackendServerDescriptions: Optional[BackendServerDescriptions] = None
    AvailabilityZones: Optional[AvailabilityZones] = None
    Subnets: Optional[Subnets] = None
    VPCId: Optional[VPCId] = None
    Instances: Optional[Instances] = None
    HealthCheck: Optional[HealthCheck] = None
    SourceSecurityGroup: Optional[SourceSecurityGroup] = None
    SecurityGroups: Optional[SecurityGroups] = None
    CreatedTime: Optional[CreatedTime] = None
    Scheme: Optional[LoadBalancerScheme] = None


class ModifyLoadBalancerAttributesInput(BaseModel):
    """
    Contains the parameters for ModifyLoadBalancerAttributes.
    """

    LoadBalancerName: AccessPointName
    LoadBalancerAttributes: LoadBalancerAttributes


class RegisterEndPointsInput(BaseModel):
    """
    Contains the parameters for RegisterInstancesWithLoadBalancer.
    """

    LoadBalancerName: AccessPointName
    Instances: Instances


class TagKeyList(BaseModel):
    __root__: Annotated[List[TagKeyOnly], Field(min_items=1)]


class RemoveTagsInput(BaseModel):
    """
    Contains the parameters for RemoveTags.
    """

    LoadBalancerNames: LoadBalancerNames
    Tags: TagKeyList


class TagDescription(BaseModel):
    """
    The tags associated with a load balancer.
    """

    LoadBalancerName: Optional[AccessPointName] = None
    Tags: Optional[TagList] = None


class DeregisterEndPointsOutput(BaseModel):
    """
    Contains the output of DeregisterInstancesFromLoadBalancer.
    """

    Instances: Optional[Instances] = None


class DescribeAccountLimitsOutput(BaseModel):
    Limits: Optional[Limits] = None
    NextMarker: Optional[Marker] = None


class DescribeEndPointStateOutput(BaseModel):
    """
    Contains the output for DescribeInstanceHealth.
    """

    InstanceStates: Optional[InstanceStates] = None


class DescribeLoadBalancerAttributesOutput(BaseModel):
    """
    Contains the output of DescribeLoadBalancerAttributes.
    """

    LoadBalancerAttributes: Optional[LoadBalancerAttributes] = None


class DescribeLoadBalancerPoliciesOutput(BaseModel):
    """
    Contains the output of DescribeLoadBalancerPolicies.
    """

    PolicyDescriptions: Optional[PolicyDescriptions] = None


class DescribeLoadBalancerPolicyTypesOutput(BaseModel):
    """
    Contains the output of DescribeLoadBalancerPolicyTypes.
    """

    PolicyTypeDescriptions: Optional[PolicyTypeDescriptions] = None


class ModifyLoadBalancerAttributesOutput(BaseModel):
    """
    Contains the output of ModifyLoadBalancerAttributes.
    """

    LoadBalancerName: Optional[AccessPointName] = None
    LoadBalancerAttributes: Optional[LoadBalancerAttributes] = None


class RegisterEndPointsOutput(DeregisterEndPointsOutput):
    """
    Contains the output of RegisterInstancesWithLoadBalancer.
    """

    pass


class LoadBalancerDescriptions(BaseModel):
    __root__: List[LoadBalancerDescription]


class TagDescriptions(BaseModel):
    __root__: List[TagDescription]


class DescribeAccessPointsOutput(BaseModel):
    """
    Contains the parameters for DescribeLoadBalancers.
    """

    LoadBalancerDescriptions: Optional[LoadBalancerDescriptions] = None
    NextMarker: Optional[Marker] = None


class DescribeTagsOutput(BaseModel):
    """
    Contains the output for DescribeTags.
    """

    TagDescriptions: Optional[TagDescriptions] = None
