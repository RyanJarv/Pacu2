# generated by datamodel-codegen:
#   filename:  openapi.yaml
#   timestamp: 2021-12-31T02:50:14+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Annotated, Any, List, Optional

from pydantic import BaseModel, Extra, Field


class AcceptInvitationResponse(BaseModel):
    pass


class BadRequestException(BaseModel):
    __root__: Any


class InternalServerErrorException(BadRequestException):
    pass


class ArchiveFindingsResponse(AcceptInvitationResponse):
    pass


class FindingId(BaseModel):
    __root__: Annotated[str, Field(max_length=300, min_length=1)]


class TagValue(BaseModel):
    __root__: Annotated[str, Field(max_length=256)]


class Criterion(BaseModel):
    pass

    class Config:
        extra = Extra.allow


class String(BaseModel):
    __root__: str


class CreateSampleFindingsResponse(AcceptInvitationResponse):
    pass


class FindingType(BaseModel):
    __root__: Annotated[str, Field(max_length=50, min_length=1)]


class CreateThreatIntelSetResponse(BaseModel):
    ThreatIntelSetId: String


class AccountId(BaseModel):
    __root__: Annotated[str, Field(max_length=12, min_length=12)]


class DeleteDetectorResponse(AcceptInvitationResponse):
    pass


class DeleteFilterResponse(AcceptInvitationResponse):
    pass


class DeleteIPSetResponse(AcceptInvitationResponse):
    pass


class DeletePublishingDestinationResponse(AcceptInvitationResponse):
    pass


class DeleteThreatIntelSetResponse(AcceptInvitationResponse):
    pass


class DisableOrganizationAdminAccountResponse(AcceptInvitationResponse):
    pass


class DisassociateFromMasterAccountResponse(AcceptInvitationResponse):
    pass


class EnableOrganizationAdminAccountResponse(AcceptInvitationResponse):
    pass


class OrderBy(Enum):
    ASC = 'ASC'
    DESC = 'DESC'


class FindingStatisticType(Enum):
    COUNT_BY_SEVERITY = 'COUNT_BY_SEVERITY'


class AccountIds(BaseModel):
    __root__: Annotated[List[AccountId], Field(max_items=50, min_items=1)]


class ResourceList(BaseModel):
    __root__: List[String]


class TagResourceResponse(AcceptInvitationResponse):
    pass


class UnarchiveFindingsResponse(AcceptInvitationResponse):
    pass


class UntagResourceResponse(AcceptInvitationResponse):
    pass


class TagKey(BaseModel):
    __root__: Annotated[
        str, Field(max_length=128, min_length=1, regex='^(?!aws:)[a-zA-Z+-=._:/]+$')
    ]


class UpdateDetectorResponse(AcceptInvitationResponse):
    pass


class UpdateFindingsFeedbackResponse(AcceptInvitationResponse):
    pass


class UpdateIPSetResponse(AcceptInvitationResponse):
    pass


class UpdateOrganizationConfigurationResponse(AcceptInvitationResponse):
    pass


class UpdatePublishingDestinationResponse(AcceptInvitationResponse):
    pass


class UpdateThreatIntelSetResponse(AcceptInvitationResponse):
    pass


class DetectorId(FindingId):
    pass


class AcceptInvitationRequest(BaseModel):
    MasterId: String
    InvitationId: String


class Boolean(BaseModel):
    __root__: bool


class AccessControlList(BaseModel):
    """
    Contains information on the current access control policies for the bucket.
    """

    AllowsPublicReadAccess: Optional[Boolean] = None
    AllowsPublicWriteAccess: Optional[Boolean] = None


class AccessKeyDetails(BaseModel):
    """
    Contains information about the access keys.
    """

    AccessKeyId: Optional[String] = None
    PrincipalId: Optional[String] = None
    UserName: Optional[String] = None
    UserType: Optional[String] = None


class Email(BaseModel):
    __root__: Annotated[str, Field(max_length=64, min_length=1)]


class BlockPublicAccess(BaseModel):
    """
    Contains information on how the bucker owner's S3 Block Public Access settings are being applied to the S3 bucket. See <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html">S3 Block Public Access</a> for more information.
    """

    IgnorePublicAcls: Optional[Boolean] = None
    RestrictPublicBuckets: Optional[Boolean] = None
    BlockPublicAcls: Optional[Boolean] = None
    BlockPublicPolicy: Optional[Boolean] = None


class AccountLevelPermissions(BaseModel):
    """
    Contains information about the account level permissions on the S3 bucket.
    """

    BlockPublicAccess: Optional[BlockPublicAccess] = None


class DnsRequestAction(BaseModel):
    """
    Contains information about the DNS_REQUEST action described in this finding.
    """

    Domain: Optional[String] = None


class AdminStatus(Enum):
    ENABLED = 'ENABLED'
    DISABLE_IN_PROGRESS = 'DISABLE_IN_PROGRESS'


class AdminAccount(BaseModel):
    """
    The account within the organization specified as the GuardDuty delegated administrator.
    """

    AdminAccountId: Optional[String] = None
    AdminStatus: Optional[AdminStatus] = None


class AdminAccounts(BaseModel):
    __root__: Annotated[List[AdminAccount], Field(max_items=1, min_items=0)]


class FindingIds(BaseModel):
    __root__: Annotated[List[FindingId], Field(max_items=50, min_items=0)]


class ArchiveFindingsRequest(BaseModel):
    FindingIds: FindingIds


class DomainDetails(DnsRequestAction):
    """
    Contains information about the domain.
    """

    pass


class BucketPolicy(AccessControlList):
    """
    Contains information on the current bucket policies for the S3 bucket.
    """

    pass


class BucketLevelPermissions(BaseModel):
    """
    Contains information about the bucket level permissions for the S3 bucket.
    """

    AccessControlList: Optional[AccessControlList] = None
    BucketPolicy: Optional[BucketPolicy] = None
    BlockPublicAccess: Optional[BlockPublicAccess] = None


class City(BaseModel):
    """
    Contains information about the city associated with the IP address.
    """

    CityName: Optional[String] = None


class ClientToken(BaseModel):
    __root__: Annotated[str, Field(max_length=64, min_length=0)]


class DataSourceStatus(Enum):
    ENABLED = 'ENABLED'
    DISABLED = 'DISABLED'


class CloudTrailConfigurationResult(BaseModel):
    """
    Contains information on the status of CloudTrail as a data source for the detector.
    """

    Status: DataSourceStatus


class Eq(ResourceList):
    pass


class Neq(ResourceList):
    pass


class Integer(BaseModel):
    __root__: int


class Equals(ResourceList):
    pass


class NotEquals(ResourceList):
    pass


class Long(Integer):
    pass


class Condition(BaseModel):
    """
    Contains information about the condition.
    """

    Eq: Optional[Eq] = None
    Neq: Optional[Neq] = None
    Gt: Optional[Integer] = None
    Gte: Optional[Integer] = None
    Lt: Optional[Integer] = None
    Lte: Optional[Integer] = None
    Equals: Optional[Equals] = None
    NotEquals: Optional[NotEquals] = None
    GreaterThan: Optional[Long] = None
    GreaterThanOrEqual: Optional[Long] = None
    LessThan: Optional[Long] = None
    LessThanOrEqual: Optional[Long] = None


class CountBySeverity(BaseModel):
    pass

    class Config:
        extra = Extra.allow


class Country(BaseModel):
    """
    Contains information about the country where the remote IP address is located.
    """

    CountryCode: Optional[String] = None
    CountryName: Optional[String] = None


class FindingPublishingFrequency(Enum):
    FIFTEEN_MINUTES = 'FIFTEEN_MINUTES'
    ONE_HOUR = 'ONE_HOUR'
    SIX_HOURS = 'SIX_HOURS'


class TagMap(BaseModel):
    pass

    class Config:
        extra = Extra.allow


class FilterName(BaseModel):
    __root__: Annotated[str, Field(max_length=64, min_length=3)]


class FilterDescription(BaseModel):
    __root__: Annotated[str, Field(max_length=512, min_length=0)]


class FilterAction(Enum):
    NOOP = 'NOOP'
    ARCHIVE = 'ARCHIVE'


class FilterRank(BaseModel):
    __root__: Annotated[int, Field(ge=1.0, le=100.0)]


class FindingCriteria(BaseModel):
    """
    Contains information about the criteria used for querying findings.
    """

    Criterion: Optional[Criterion] = None


class CreateFilterRequest(BaseModel):
    Name: FilterName
    Description: Optional[FilterDescription] = None
    Action: Optional[FilterAction] = None
    Rank: Optional[FilterRank] = None
    FindingCriteria: FindingCriteria
    ClientToken: Optional[ClientToken] = None
    Tags: Optional[TagMap] = None


class Name(FindingId):
    pass


class IpSetFormat(Enum):
    TXT = 'TXT'
    STIX = 'STIX'
    OTX_CSV = 'OTX_CSV'
    ALIEN_VAULT = 'ALIEN_VAULT'
    PROOF_POINT = 'PROOF_POINT'
    FIRE_EYE = 'FIRE_EYE'


class Location(FindingId):
    pass


class CreateIPSetRequest(BaseModel):
    Name: Name
    Format: IpSetFormat
    Location: Location
    Activate: Boolean
    ClientToken: Optional[ClientToken] = None
    Tags: Optional[TagMap] = None


class DestinationType(Enum):
    S3 = 'S3'


class DestinationProperties(BaseModel):
    """
    Contains the Amazon Resource Name (ARN) of the resource to publish to, such as an S3 bucket, and the ARN of the KMS key to use to encrypt published findings.
    """

    DestinationArn: Optional[String] = None
    KmsKeyArn: Optional[String] = None


class CreatePublishingDestinationRequest(BaseModel):
    DestinationType: DestinationType
    DestinationProperties: DestinationProperties
    ClientToken: Optional[ClientToken] = None


class FindingTypes(BaseModel):
    __root__: Annotated[List[FindingType], Field(max_items=50, min_items=0)]


class CreateSampleFindingsRequest(BaseModel):
    FindingTypes: Optional[FindingTypes] = None


class CreateThreatIntelSetRequest(BaseModel):
    Name: Name
    Format: IpSetFormat
    Location: Location
    Activate: Boolean
    ClientToken: Optional[ClientToken] = None
    Tags: Optional[TagMap] = None


class DNSLogsConfigurationResult(CloudTrailConfigurationResult):
    """
    Contains information on the status of DNS logs as a data source.
    """

    pass


class DataSource(Enum):
    FLOW_LOGS = 'FLOW_LOGS'
    CLOUD_TRAIL = 'CLOUD_TRAIL'
    DNS_LOGS = 'DNS_LOGS'
    S3_LOGS = 'S3_LOGS'


class FlowLogsConfigurationResult(CloudTrailConfigurationResult):
    """
    Contains information on the status of VPC flow logs as a data source.
    """

    pass


class S3LogsConfigurationResult(CloudTrailConfigurationResult):
    """
    Describes whether S3 data event logs will be enabled as a data source.
    """

    pass


class DataSourceConfigurationsResult(BaseModel):
    """
    Contains information on the status of data sources for the detector.
    """

    CloudTrail: CloudTrailConfigurationResult
    DNSLogs: DNSLogsConfigurationResult
    FlowLogs: FlowLogsConfigurationResult
    S3Logs: S3LogsConfigurationResult


class DeclineInvitationsRequest(BaseModel):
    AccountIds: AccountIds


class DefaultServerSideEncryption(BaseModel):
    """
    Contains information on the server side encryption method used in the S3 bucket. See <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/serv-side-encryption.html">S3 Server-Side Encryption</a> for more information.
    """

    EncryptionType: Optional[String] = None
    KmsMasterKeyArn: Optional[String] = None


class DeleteDetectorRequest(BaseModel):
    pass


class DeleteFilterRequest(BaseModel):
    pass


class DeleteIPSetRequest(BaseModel):
    pass


class DeleteInvitationsRequest(BaseModel):
    AccountIds: AccountIds


class DeleteMembersRequest(BaseModel):
    AccountIds: AccountIds


class DeletePublishingDestinationRequest(BaseModel):
    pass


class DeleteThreatIntelSetRequest(BaseModel):
    pass


class DescribeOrganizationConfigurationRequest(BaseModel):
    pass


class DescribePublishingDestinationRequest(BaseModel):
    pass


class PublishingStatus(Enum):
    PENDING_VERIFICATION = 'PENDING_VERIFICATION'
    PUBLISHING = 'PUBLISHING'
    UNABLE_TO_PUBLISH_FIX_DESTINATION_PROPERTY = (
        'UNABLE_TO_PUBLISH_FIX_DESTINATION_PROPERTY'
    )
    STOPPED = 'STOPPED'


class Destination(BaseModel):
    """
    Contains information about the publishing destination, including the ID, type, and status.
    """

    DestinationId: String
    DestinationType: DestinationType
    Status: PublishingStatus


class Destinations(BaseModel):
    __root__: List[Destination]


class DetectorIds(BaseModel):
    __root__: Annotated[List[DetectorId], Field(max_items=50, min_items=0)]


class DisableOrganizationAdminAccountRequest(BaseModel):
    AdminAccountId: String


class DisassociateFromMasterAccountRequest(BaseModel):
    pass


class DisassociateMembersRequest(BaseModel):
    AccountIds: AccountIds


class Double(BaseModel):
    __root__: float


class EnableOrganizationAdminAccountRequest(BaseModel):
    AdminAccountId: String


class Feedback(Enum):
    USEFUL = 'USEFUL'
    NOT_USEFUL = 'NOT_USEFUL'


class FilterNames(BaseModel):
    __root__: Annotated[List[FilterName], Field(max_items=50, min_items=0)]


class FindingStatisticTypes(BaseModel):
    __root__: Annotated[List[FindingStatisticType], Field(max_items=10, min_items=0)]


class FindingStatistics(BaseModel):
    """
    Contains information about finding statistics.
    """

    CountBySeverity: Optional[CountBySeverity] = None


class GeoLocation(BaseModel):
    """
    Contains information about the location of the remote IP address.
    """

    Lat: Optional[Double] = None
    Lon: Optional[Double] = None


class GetDetectorRequest(BaseModel):
    pass


class GetFilterRequest(BaseModel):
    pass


class SortCriteria(BaseModel):
    """
    Contains information about the criteria used for sorting findings.
    """

    AttributeName: Optional[String] = None
    OrderBy: Optional[OrderBy] = None


class GetFindingsRequest(BaseModel):
    FindingIds: FindingIds
    SortCriteria: Optional[SortCriteria] = None


class GetFindingsStatisticsRequest(BaseModel):
    FindingStatisticTypes: FindingStatisticTypes
    FindingCriteria: Optional[FindingCriteria] = None


class GetIPSetRequest(BaseModel):
    pass


class IpSetStatus(Enum):
    INACTIVE = 'INACTIVE'
    ACTIVATING = 'ACTIVATING'
    ACTIVE = 'ACTIVE'
    DEACTIVATING = 'DEACTIVATING'
    ERROR = 'ERROR'
    DELETE_PENDING = 'DELETE_PENDING'
    DELETED = 'DELETED'


class GetInvitationsCountRequest(BaseModel):
    pass


class GetMasterAccountRequest(BaseModel):
    pass


class Master(BaseModel):
    """
    Contains information about the administrator account and invitation.
    """

    AccountId: Optional[AccountId] = None
    InvitationId: Optional[String] = None
    RelationshipStatus: Optional[String] = None
    InvitedAt: Optional[String] = None


class GetMemberDetectorsRequest(BaseModel):
    AccountIds: AccountIds


class GetMembersRequest(BaseModel):
    AccountIds: AccountIds


class GetThreatIntelSetRequest(BaseModel):
    pass


class UsageStatisticType(Enum):
    SUM_BY_ACCOUNT = 'SUM_BY_ACCOUNT'
    SUM_BY_DATA_SOURCE = 'SUM_BY_DATA_SOURCE'
    SUM_BY_RESOURCE = 'SUM_BY_RESOURCE'
    TOP_RESOURCES = 'TOP_RESOURCES'


class MaxResults(BaseModel):
    __root__: Annotated[int, Field(ge=1.0, le=50.0)]


class GuardDutyArn(BaseModel):
    __root__: Annotated[
        str,
        Field(
            regex='^arn:[A-Za-z_.-]{1,20}:guardduty:[A-Za-z0-9_/.-]{0,63}:\\d+:detector/[A-Za-z0-9_/.-]{32,264}$'
        ),
    ]


class IamInstanceProfile(BaseModel):
    """
    Contains information about the EC2 instance profile.
    """

    Arn: Optional[String] = None
    Id: Optional[String] = None


class Invitation(Master):
    """
    Contains information about the invitation to become a member account.
    """

    pass


class Invitations(BaseModel):
    __root__: Annotated[List[Invitation], Field(max_items=50, min_items=0)]


class InviteMembersRequest(BaseModel):
    AccountIds: AccountIds
    DisableEmailNotification: Optional[Boolean] = None
    Message: Optional[String] = None


class IpSetIds(BaseModel):
    __root__: Annotated[List[String], Field(max_items=50, min_items=0)]


class Ipv6Addresses(ResourceList):
    pass


class ListDetectorsRequest(BaseModel):
    pass


class ListFiltersRequest(BaseModel):
    pass


class ListFindingsRequest(BaseModel):
    FindingCriteria: Optional[FindingCriteria] = None
    SortCriteria: Optional[SortCriteria] = None
    MaxResults: Optional[MaxResults] = None
    NextToken: Optional[String] = None


class ListIPSetsRequest(BaseModel):
    pass


class ListInvitationsRequest(BaseModel):
    pass


class ListMembersRequest(BaseModel):
    pass


class ListOrganizationAdminAccountsRequest(BaseModel):
    pass


class ListPublishingDestinationsRequest(BaseModel):
    pass


class ListTagsForResourceRequest(BaseModel):
    pass


class ListThreatIntelSetsRequest(BaseModel):
    pass


class ThreatIntelSetIds(IpSetIds):
    pass


class LocalIpDetails(BaseModel):
    """
    Contains information about the local IP address of the connection.
    """

    IpAddressV4: Optional[String] = None


class LocalPortDetails(BaseModel):
    """
    Contains information about the port for the local connection.
    """

    Port: Optional[Integer] = None
    PortName: Optional[String] = None


class Member(BaseModel):
    """
    Contains information about the member account.
    """

    AccountId: AccountId
    DetectorId: Optional[DetectorId] = None
    MasterId: String
    Email: Email
    RelationshipStatus: String
    InvitedAt: Optional[String] = None
    UpdatedAt: String


class MemberDataSourceConfiguration(BaseModel):
    """
    Contains information on which data sources are enabled for a member account.
    """

    AccountId: AccountId
    DataSources: DataSourceConfigurationsResult


class RemotePortDetails(LocalPortDetails):
    """
    Contains information about the remote port.
    """

    pass


class Organization(BaseModel):
    """
    Contains information about the ISP organization of the remote IP address.
    """

    Asn: Optional[String] = None
    AsnOrg: Optional[String] = None
    Isp: Optional[String] = None
    Org: Optional[String] = None


class OrganizationS3LogsConfigurationResult(BaseModel):
    """
    The current configuration of S3 data event logs as a data source for the organization.
    """

    AutoEnable: Boolean


class Owner(BaseModel):
    """
    Contains information on the owner of the bucket.
    """

    Id: Optional[String] = None


class PermissionConfiguration(BaseModel):
    """
    Contains information about how permissions are configured for the S3 bucket.
    """

    BucketLevelPermissions: Optional[BucketLevelPermissions] = None
    AccountLevelPermissions: Optional[AccountLevelPermissions] = None


class PrivateIpAddressDetails(BaseModel):
    """
    Contains other private IP address information of the EC2 instance.
    """

    PrivateDnsName: Optional[String] = None
    PrivateIpAddress: Optional[String] = None


class ProductCode(BaseModel):
    """
    Contains information about the product code for the EC2 instance.
    """

    Code: Optional[String] = None
    ProductType: Optional[String] = None


class PublicAccess(BaseModel):
    """
    Describes the public access policies that apply to the S3 bucket.
    """

    PermissionConfiguration: Optional[PermissionConfiguration] = None
    EffectivePermission: Optional[String] = None


class Timestamp(BaseModel):
    __root__: datetime


class SecurityGroup(BaseModel):
    """
    Contains information about the security groups associated with the EC2 instance.
    """

    GroupId: Optional[String] = None
    GroupName: Optional[String] = None


class StartMonitoringMembersRequest(BaseModel):
    AccountIds: AccountIds


class StopMonitoringMembersRequest(BaseModel):
    AccountIds: AccountIds


class Tag(BaseModel):
    """
    Contains information about a tag associated with the EC2 instance.
    """

    Key: Optional[String] = None
    Value: Optional[String] = None


class TagKeyList(BaseModel):
    __root__: Annotated[List[TagKey], Field(max_items=200, min_items=1)]


class TagResourceRequest(BaseModel):
    Tags: TagMap


class ThreatNames(ResourceList):
    pass


class ThreatIntelligenceDetail(BaseModel):
    """
    An instance of a threat intelligence detail that constitutes evidence for the finding.
    """

    ThreatListName: Optional[String] = None
    ThreatNames: Optional[ThreatNames] = None


class Total(BaseModel):
    """
    Contains the total usage with the corresponding currency unit for that value.
    """

    Amount: Optional[String] = None
    Unit: Optional[String] = None


class UnarchiveFindingsRequest(BaseModel):
    FindingIds: FindingIds


class UnprocessedAccount(BaseModel):
    """
    Contains information about the accounts that weren't processed.
    """

    AccountId: AccountId
    Result: String


class UntagResourceRequest(BaseModel):
    pass


class UpdateFilterRequest(BaseModel):
    Description: Optional[FilterDescription] = None
    Action: Optional[FilterAction] = None
    Rank: Optional[FilterRank] = None
    FindingCriteria: Optional[FindingCriteria] = None


class UpdateFindingsFeedbackRequest(BaseModel):
    FindingIds: FindingIds
    Feedback: Feedback
    Comments: Optional[String] = None


class UpdateIPSetRequest(BaseModel):
    Name: Optional[Name] = None
    Location: Optional[Location] = None
    Activate: Optional[Boolean] = None


class UpdatePublishingDestinationRequest(BaseModel):
    DestinationProperties: Optional[DestinationProperties] = None


class UpdateThreatIntelSetRequest(BaseModel):
    Name: Optional[Name] = None
    Location: Optional[Location] = None
    Activate: Optional[Boolean] = None


class UsageAccountResult(BaseModel):
    """
    Contains information on the total of usage based on account IDs.
    """

    AccountId: Optional[AccountId] = None
    Total: Optional[Total] = None


class UsageAccountResultList(BaseModel):
    __root__: List[UsageAccountResult]


class UsageDataSourceResult(BaseModel):
    """
    Contains information on the result of usage based on data source type.
    """

    DataSource: Optional[DataSource] = None
    Total: Optional[Total] = None


class UsageDataSourceResultList(BaseModel):
    __root__: List[UsageDataSourceResult]


class UsageResourceResult(BaseModel):
    """
    Contains information on the sum of usage based on an AWS resource.
    """

    Resource: Optional[String] = None
    Total: Optional[Total] = None


class UsageResourceResultList(BaseModel):
    __root__: List[UsageResourceResult]


class CreateDetectorResponse(BaseModel):
    DetectorId: Optional[DetectorId] = None


class S3LogsConfiguration(BaseModel):
    """
    Describes whether S3 data event logs will be enabled as a data source.
    """

    Enable: Boolean


class CreateFilterResponse(BaseModel):
    Name: FilterName


class CreateIPSetResponse(BaseModel):
    IpSetId: String


class AccountDetail(BaseModel):
    """
    Contains information about the account.
    """

    AccountId: AccountId
    Email: Email


class CreatePublishingDestinationResponse(BaseModel):
    DestinationId: String


class DescribePublishingDestinationResponse(BaseModel):
    DestinationId: String
    DestinationType: DestinationType
    Status: PublishingStatus
    PublishingFailureStartTimestamp: Long
    DestinationProperties: DestinationProperties


class GetDetectorResponse(BaseModel):
    CreatedAt: Optional[String] = None
    FindingPublishingFrequency: Optional[FindingPublishingFrequency] = None
    ServiceRole: String
    Status: DataSourceStatus
    UpdatedAt: Optional[String] = None
    DataSources: Optional[DataSourceConfigurationsResult] = None
    Tags: Optional[TagMap] = None


class GetFilterResponse(BaseModel):
    Name: FilterName
    Description: Optional[FilterDescription] = None
    Action: FilterAction
    Rank: Optional[FilterRank] = None
    FindingCriteria: FindingCriteria
    Tags: Optional[TagMap] = None


class GetFindingsStatisticsResponse(BaseModel):
    FindingStatistics: FindingStatistics


class GetIPSetResponse(BaseModel):
    Name: Name
    Format: IpSetFormat
    Location: Location
    Status: IpSetStatus
    Tags: Optional[TagMap] = None


class GetInvitationsCountResponse(BaseModel):
    InvitationsCount: Optional[Integer] = None


class GetMasterAccountResponse(BaseModel):
    Master: Master


class GetThreatIntelSetResponse(GetIPSetResponse):
    pass


class DataSourceList(BaseModel):
    __root__: List[DataSource]


class ListDetectorsResponse(BaseModel):
    DetectorIds: DetectorIds
    NextToken: Optional[String] = None


class ListFiltersResponse(BaseModel):
    FilterNames: FilterNames
    NextToken: Optional[String] = None


class ListFindingsResponse(BaseModel):
    FindingIds: FindingIds
    NextToken: Optional[String] = None


class ListIPSetsResponse(BaseModel):
    IpSetIds: IpSetIds
    NextToken: Optional[String] = None


class ListInvitationsResponse(BaseModel):
    Invitations: Optional[Invitations] = None
    NextToken: Optional[String] = None


class ListOrganizationAdminAccountsResponse(BaseModel):
    AdminAccounts: Optional[AdminAccounts] = None
    NextToken: Optional[String] = None


class ListPublishingDestinationsResponse(BaseModel):
    Destinations: Destinations
    NextToken: Optional[String] = None


class ListTagsForResourceResponse(BaseModel):
    Tags: Optional[TagMap] = None


class ListThreatIntelSetsResponse(BaseModel):
    ThreatIntelSetIds: ThreatIntelSetIds
    NextToken: Optional[String] = None


class UpdateFilterResponse(CreateFilterResponse):
    pass


class OrganizationS3LogsConfiguration(OrganizationS3LogsConfigurationResult):
    """
    Describes whether S3 data event logs will be automatically enabled for new members of the organization.
    """

    pass


class AccountDetails(BaseModel):
    __root__: Annotated[List[AccountDetail], Field(max_items=50, min_items=1)]


class RemoteIpDetails(BaseModel):
    """
    Contains information about the remote IP address of the connection.
    """

    City: Optional[City] = None
    Country: Optional[Country] = None
    GeoLocation: Optional[GeoLocation] = None
    IpAddressV4: Optional[String] = None
    Organization: Optional[Organization] = None


class DataSourceConfigurations(BaseModel):
    """
    Contains information about which data sources are enabled.
    """

    S3Logs: Optional[S3LogsConfiguration] = None


class CreateDetectorRequest(BaseModel):
    Enable: Boolean
    ClientToken: Optional[ClientToken] = None
    FindingPublishingFrequency: Optional[FindingPublishingFrequency] = None
    DataSources: Optional[DataSourceConfigurations] = None
    Tags: Optional[TagMap] = None


class CreateMembersRequest(BaseModel):
    AccountDetails: AccountDetails


class UnprocessedAccounts(BaseModel):
    __root__: Annotated[List[UnprocessedAccount], Field(max_items=50, min_items=0)]


class OrganizationDataSourceConfigurationsResult(BaseModel):
    """
    An object that contains information on which data sources are automatically enabled for new members within the organization.
    """

    S3Logs: OrganizationS3LogsConfigurationResult


class ThreatIntelligenceDetails(BaseModel):
    __root__: List[ThreatIntelligenceDetail]


class Evidence(BaseModel):
    """
    Contains information about the reason that the finding was generated.
    """

    ThreatIntelligenceDetails: Optional[ThreatIntelligenceDetails] = None


class MemberDataSourceConfigurations(BaseModel):
    __root__: Annotated[
        List[MemberDataSourceConfiguration], Field(max_items=50, min_items=1)
    ]


class Members(BaseModel):
    __root__: Annotated[List[Member], Field(max_items=50, min_items=0)]


class UsageCriteria(BaseModel):
    """
    Contains information about the criteria used to query usage statistics.
    """

    AccountIds: Optional[AccountIds] = None
    DataSources: DataSourceList
    Resources: Optional[ResourceList] = None


class GetUsageStatisticsRequest(BaseModel):
    UsageStatisticType: UsageStatisticType
    UsageCriteria: UsageCriteria
    Unit: Optional[String] = None
    MaxResults: Optional[MaxResults] = None
    NextToken: Optional[String] = None


class UsageStatistics(BaseModel):
    """
    Contains the result of GuardDuty usage. If a UsageStatisticType is provided the result for other types will be null.
    """

    SumByAccount: Optional[UsageAccountResultList] = None
    SumByDataSource: Optional[UsageDataSourceResultList] = None
    SumByResource: Optional[UsageResourceResultList] = None
    TopResources: Optional[UsageResourceResultList] = None


class ProductCodes(BaseModel):
    __root__: List[ProductCode]


class Tags9(BaseModel):
    __root__: List[Tag]


class PrivateIpAddresses(BaseModel):
    __root__: List[PrivateIpAddressDetails]


class SecurityGroups(BaseModel):
    __root__: List[SecurityGroup]


class NetworkInterface(BaseModel):
    """
    Contains information about the elastic network interface of the EC2 instance.
    """

    Ipv6Addresses: Optional[Ipv6Addresses] = None
    NetworkInterfaceId: Optional[String] = None
    PrivateDnsName: Optional[String] = None
    PrivateIpAddress: Optional[String] = None
    PrivateIpAddresses: Optional[PrivateIpAddresses] = None
    PublicDnsName: Optional[String] = None
    PublicIp: Optional[String] = None
    SecurityGroups: Optional[SecurityGroups] = None
    SubnetId: Optional[String] = None
    VpcId: Optional[String] = None


class OrganizationDataSourceConfigurations(BaseModel):
    """
    An object that contains information on which data sources will be configured to be automatically enabled for new members within the organization.
    """

    S3Logs: Optional[OrganizationS3LogsConfiguration] = None


class PortProbeDetail(BaseModel):
    """
    Contains information about the port probe details.
    """

    LocalPortDetails: Optional[LocalPortDetails] = None
    LocalIpDetails: Optional[LocalIpDetails] = None
    RemoteIpDetails: Optional[RemoteIpDetails] = None


class S3BucketDetail(BaseModel):
    """
    Contains information on the S3 bucket.
    """

    Arn: Optional[String] = None
    Name: Optional[String] = None
    Type: Optional[String] = None
    CreatedAt: Optional[Timestamp] = None
    Owner: Optional[Owner] = None
    Tags: Optional[Tags9] = None
    DefaultServerSideEncryption: Optional[DefaultServerSideEncryption] = None
    PublicAccess: Optional[PublicAccess] = None


class UpdateDetectorRequest(BaseModel):
    Enable: Optional[Boolean] = None
    FindingPublishingFrequency: Optional[FindingPublishingFrequency] = None
    DataSources: Optional[DataSourceConfigurations] = None


class UpdateMemberDetectorsRequest(BaseModel):
    AccountIds: AccountIds
    DataSources: Optional[DataSourceConfigurations] = None


class UpdateOrganizationConfigurationRequest(BaseModel):
    AutoEnable: Boolean
    DataSources: Optional[OrganizationDataSourceConfigurations] = None


class CreateMembersResponse(BaseModel):
    UnprocessedAccounts: UnprocessedAccounts


class DeclineInvitationsResponse(CreateMembersResponse):
    pass


class DeleteInvitationsResponse(CreateMembersResponse):
    pass


class DeleteMembersResponse(CreateMembersResponse):
    pass


class DescribeOrganizationConfigurationResponse(BaseModel):
    AutoEnable: Boolean
    MemberAccountLimitReached: Boolean
    DataSources: Optional[OrganizationDataSourceConfigurationsResult] = None


class DisassociateMembersResponse(CreateMembersResponse):
    pass


class GetMemberDetectorsResponse(BaseModel):
    MemberDataSourceConfigurations: MemberDataSourceConfigurations
    UnprocessedAccounts: UnprocessedAccounts


class GetMembersResponse(BaseModel):
    Members: Members
    UnprocessedAccounts: UnprocessedAccounts


class GetUsageStatisticsResponse(BaseModel):
    UsageStatistics: Optional[UsageStatistics] = None
    NextToken: Optional[String] = None


class InviteMembersResponse(CreateMembersResponse):
    pass


class ListMembersResponse(BaseModel):
    Members: Optional[Members] = None
    NextToken: Optional[String] = None


class StartMonitoringMembersResponse(CreateMembersResponse):
    pass


class StopMonitoringMembersResponse(CreateMembersResponse):
    pass


class UpdateMemberDetectorsResponse(CreateMembersResponse):
    pass


class AwsApiCallAction(BaseModel):
    """
    Contains information about the API action.
    """

    Api: Optional[String] = None
    CallerType: Optional[String] = None
    DomainDetails: Optional[DomainDetails] = None
    ErrorCode: Optional[String] = None
    RemoteIpDetails: Optional[RemoteIpDetails] = None
    ServiceName: Optional[String] = None


class NetworkConnectionAction(BaseModel):
    """
    Contains information about the NETWORK_CONNECTION action described in the finding.
    """

    Blocked: Optional[Boolean] = None
    ConnectionDirection: Optional[String] = None
    LocalPortDetails: Optional[LocalPortDetails] = None
    Protocol: Optional[String] = None
    LocalIpDetails: Optional[LocalIpDetails] = None
    RemoteIpDetails: Optional[RemoteIpDetails] = None
    RemotePortDetails: Optional[RemotePortDetails] = None


class NetworkInterfaces(BaseModel):
    __root__: List[NetworkInterface]


class InstanceDetails(BaseModel):
    """
    Contains information about the details of an instance.
    """

    AvailabilityZone: Optional[String] = None
    IamInstanceProfile: Optional[IamInstanceProfile] = None
    ImageDescription: Optional[String] = None
    ImageId: Optional[String] = None
    InstanceId: Optional[String] = None
    InstanceState: Optional[String] = None
    InstanceType: Optional[String] = None
    OutpostArn: Optional[String] = None
    LaunchTime: Optional[String] = None
    NetworkInterfaces: Optional[NetworkInterfaces] = None
    Platform: Optional[String] = None
    ProductCodes: Optional[ProductCodes] = None
    Tags: Optional[Tags9] = None


class PortProbeDetails(BaseModel):
    __root__: List[PortProbeDetail]


class S3BucketDetails(BaseModel):
    __root__: List[S3BucketDetail]


class PortProbeAction(BaseModel):
    """
    Contains information about the PORT_PROBE action described in the finding.
    """

    Blocked: Optional[Boolean] = None
    PortProbeDetails: Optional[PortProbeDetails] = None


class Action1(BaseModel):
    """
    Contains information about actions.
    """

    ActionType: Optional[String] = None
    AwsApiCallAction: Optional[AwsApiCallAction] = None
    DnsRequestAction: Optional[DnsRequestAction] = None
    NetworkConnectionAction: Optional[NetworkConnectionAction] = None
    PortProbeAction: Optional[PortProbeAction] = None


class Resource(BaseModel):
    """
    Contains information about the AWS resource associated with the activity that prompted GuardDuty to generate a finding.
    """

    AccessKeyDetails: Optional[AccessKeyDetails] = None
    S3BucketDetails: Optional[S3BucketDetails] = None
    InstanceDetails: Optional[InstanceDetails] = None
    ResourceType: Optional[String] = None


class Service(BaseModel):
    """
    Contains additional information about the generated finding.
    """

    Action: Optional[Action1] = None
    Evidence: Optional[Evidence] = None
    Archived: Optional[Boolean] = None
    Count: Optional[Integer] = None
    DetectorId: Optional[DetectorId] = None
    EventFirstSeen: Optional[String] = None
    EventLastSeen: Optional[String] = None
    ResourceRole: Optional[String] = None
    ServiceName: Optional[String] = None
    UserFeedback: Optional[String] = None


class Finding(BaseModel):
    """
    Contains information about the finding, which is generated when abnormal or suspicious activity is detected.
    """

    AccountId: String
    Arn: String
    Confidence: Optional[Double] = None
    CreatedAt: String
    Description: Optional[String] = None
    Id: String
    Partition: Optional[String] = None
    Region: String
    Resource: Resource
    SchemaVersion: String
    Service: Optional[Service] = None
    Severity: Double
    Title: Optional[String] = None
    Type: FindingType
    UpdatedAt: String


class Findings(BaseModel):
    __root__: Annotated[List[Finding], Field(max_items=50, min_items=0)]


class GetFindingsResponse(BaseModel):
    Findings: Findings