# generated by datamodel-codegen:
#   filename:  openapi.yaml
#   timestamp: 2021-12-31T02:46:09+00:00

from __future__ import annotations

from enum import Enum
from typing import Annotated, Any, List, Optional

from pydantic import BaseModel, Field


class CloudHsmServiceException(BaseModel):
    __root__: Any


class CloudHsmInternalException(CloudHsmServiceException):
    pass


class InvalidRequestException(CloudHsmServiceException):
    pass


class ListAvailableZonesRequest(BaseModel):
    """
    Contains the inputs for the <a>ListAvailableZones</a> action.
    """

    pass


class AZ(BaseModel):
    __root__: Annotated[str, Field(regex='[a-zA-Z0-9\\-]*')]


class AZList(BaseModel):
    __root__: List[AZ]


class String(BaseModel):
    __root__: Annotated[str, Field(regex='[\\w :+=./\\\\-]*')]


class Certificate(BaseModel):
    __root__: Annotated[
        str, Field(max_length=2400, min_length=600, regex='[\\w :+=./\\n-]*')
    ]


class CertificateFingerprint(BaseModel):
    __root__: Annotated[
        str, Field(regex='([0-9a-fA-F][0-9a-fA-F]:){15}[0-9a-fA-F][0-9a-fA-F]')
    ]


class ClientArn(BaseModel):
    __root__: Annotated[
        str,
        Field(
            regex='arn:aws(-iso)?:cloudhsm:[a-zA-Z0-9\\-]*:[0-9]{12}:client-[0-9a-f]{8}'
        ),
    ]


class ClientLabel(BaseModel):
    __root__: Annotated[str, Field(regex='[a-zA-Z0-9_.-]{2,64}')]


class ClientList(BaseModel):
    __root__: List[ClientArn]


class ClientToken(BaseModel):
    __root__: Annotated[str, Field(regex='[a-zA-Z0-9]{1,64}')]


class ClientVersion(Enum):
    field_5_1 = '5.1'
    field_5_3 = '5.3'


class CloudHsmObjectState(Enum):
    READY = 'READY'
    UPDATING = 'UPDATING'
    DEGRADED = 'DEGRADED'


class Label(BaseModel):
    __root__: Annotated[str, Field(regex='[a-zA-Z0-9_.-]{1,64}')]


class HapgArn(BaseModel):
    __root__: Annotated[
        str,
        Field(
            regex='arn:aws(-iso)?:cloudhsm:[a-zA-Z0-9\\-]*:[0-9]{12}:hapg-[0-9a-f]{8}'
        ),
    ]


class SubnetId(BaseModel):
    __root__: Annotated[str, Field(regex='subnet-[0-9a-f]{8}')]


class SshKey(BaseModel):
    __root__: Annotated[str, Field(regex='[a-zA-Z0-9+/= ._:\\\\@-]*')]


class IpAddress(BaseModel):
    __root__: Annotated[str, Field(regex='\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}')]


class IamRoleArn(BaseModel):
    __root__: Annotated[
        str,
        Field(
            regex='arn:aws(-iso)?:iam::[0-9]{12}:role/[a-zA-Z0-9_\\+=,\\.\\-@]{1,64}'
        ),
    ]


class ExternalId(BaseModel):
    __root__: Annotated[str, Field(regex='[\\w :+=./-]*')]


class SubscriptionType(Enum):
    """
    <p>Specifies the type of subscription for the HSM.</p> <ul> <li> <p> <b>PRODUCTION</b> - The HSM is being used in a production environment.</p> </li> <li> <p> <b>TRIAL</b> - The HSM is being used in a product trial.</p> </li> </ul>
    """

    PRODUCTION = 'PRODUCTION'


class HsmArn(BaseModel):
    __root__: Annotated[
        str,
        Field(
            description='An ARN that identifies an HSM.',
            regex='arn:aws(-iso)?:cloudhsm:[a-zA-Z0-9\\-]*:[0-9]{12}:hsm-[0-9a-f]{8}',
        ),
    ]


class HsmList(BaseModel):
    """
    Contains a list of ARNs that identify the HSMs.
    """

    __root__: Annotated[
        List[HsmArn],
        Field(description='Contains a list of ARNs that identify the HSMs.'),
    ]


class Timestamp(BaseModel):
    __root__: Annotated[str, Field(regex='\\d*')]


class HsmSerialNumber(BaseModel):
    __root__: Annotated[str, Field(regex='\\d{1,16}')]


class HsmStatus(Enum):
    PENDING = 'PENDING'
    RUNNING = 'RUNNING'
    UPDATING = 'UPDATING'
    SUSPENDED = 'SUSPENDED'
    TERMINATING = 'TERMINATING'
    TERMINATED = 'TERMINATED'
    DEGRADED = 'DEGRADED'


class EniId(BaseModel):
    __root__: Annotated[str, Field(regex='eni-[0-9a-f]{8}')]


class VpcId(BaseModel):
    __root__: Annotated[str, Field(regex='vpc-[0-9a-f]{8}')]


class HapgList(BaseModel):
    __root__: List[HapgArn]


class PaginationToken(BaseModel):
    __root__: Annotated[str, Field(regex='[a-zA-Z0-9+/]*')]


class PartitionArn(BaseModel):
    __root__: Annotated[
        str,
        Field(
            regex='arn:aws(-iso)?:cloudhsm:[a-zA-Z0-9\\-]*:[0-9]{12}:hsm-[0-9a-f]{8}/partition-[0-9]{6,12}'
        ),
    ]


class PartitionSerial(BaseModel):
    __root__: Annotated[str, Field(regex='\\d{6,12}')]


class TagKey(BaseModel):
    __root__: Annotated[str, Field(max_length=128, min_length=1)]


class TagValue(BaseModel):
    __root__: Annotated[str, Field(max_length=256, min_length=0)]


class Tag(BaseModel):
    """
    A key-value pair that identifies or specifies metadata about an AWS CloudHSM resource.
    """

    Key: TagKey
    Value: TagValue


class AddTagsToResourceResponse(BaseModel):
    Status: String


class CreateHapgResponse(BaseModel):
    """
    Contains the output of the <a>CreateHAPartitionGroup</a> action.
    """

    HapgArn: Optional[HapgArn] = None


class CreateHapgRequest(BaseModel):
    """
    Contains the inputs for the <a>CreateHapgRequest</a> action.
    """

    Label: Label


class CreateHsmResponse(BaseModel):
    """
    Contains the output of the <code>CreateHsm</code> operation.
    """

    HsmArn: Optional[HsmArn] = None


class CreateHsmRequest(BaseModel):
    """
    Contains the inputs for the <code>CreateHsm</code> operation.
    """

    SubnetId: SubnetId
    SshKey: SshKey
    EniIp: Optional[IpAddress] = None
    IamRoleArn: IamRoleArn
    ExternalId: Optional[ExternalId] = None
    SubscriptionType: SubscriptionType
    ClientToken: Optional[ClientToken] = None
    SyslogIp: Optional[IpAddress] = None


class CreateLunaClientResponse(BaseModel):
    """
    Contains the output of the <a>CreateLunaClient</a> action.
    """

    ClientArn: Optional[ClientArn] = None


class CreateLunaClientRequest(BaseModel):
    """
    Contains the inputs for the <a>CreateLunaClient</a> action.
    """

    Label: Optional[ClientLabel] = None
    Certificate: Certificate


class DeleteHapgResponse(AddTagsToResourceResponse):
    """
    Contains the output of the <a>DeleteHapg</a> action.
    """

    pass


class DeleteHapgRequest(BaseModel):
    """
    Contains the inputs for the <a>DeleteHapg</a> action.
    """

    HapgArn: HapgArn


class DeleteHsmResponse(AddTagsToResourceResponse):
    """
    Contains the output of the <a>DeleteHsm</a> operation.
    """

    pass


class DeleteHsmRequest(BaseModel):
    """
    Contains the inputs for the <a>DeleteHsm</a> operation.
    """

    HsmArn: HsmArn


class DeleteLunaClientResponse(AddTagsToResourceResponse):
    pass


class DeleteLunaClientRequest(BaseModel):
    ClientArn: ClientArn


class DescribeHapgRequest(BaseModel):
    """
    Contains the inputs for the <a>DescribeHapg</a> action.
    """

    HapgArn: HapgArn


class DescribeHsmRequest(BaseModel):
    """
    Contains the inputs for the <a>DescribeHsm</a> operation.
    """

    HsmArn: Optional[HsmArn] = None
    HsmSerialNumber: Optional[HsmSerialNumber] = None


class DescribeLunaClientResponse(BaseModel):
    ClientArn: Optional[ClientArn] = None
    Certificate: Optional[Certificate] = None
    CertificateFingerprint: Optional[CertificateFingerprint] = None
    LastModifiedTimestamp: Optional[Timestamp] = None
    Label: Optional[Label] = None


class DescribeLunaClientRequest(BaseModel):
    ClientArn: Optional[ClientArn] = None
    CertificateFingerprint: Optional[CertificateFingerprint] = None


class GetConfigResponse(BaseModel):
    ConfigType: Optional[String] = None
    ConfigFile: Optional[String] = None
    ConfigCred: Optional[String] = None


class GetConfigRequest(BaseModel):
    ClientArn: ClientArn
    ClientVersion: ClientVersion
    HapgList: HapgList


class ListAvailableZonesResponse(BaseModel):
    AZList: Optional[AZList] = None


class ListHapgsResponse(BaseModel):
    HapgList: HapgList
    NextToken: Optional[PaginationToken] = None


class ListHapgsRequest(BaseModel):
    NextToken: Optional[PaginationToken] = None


class ListHsmsResponse(BaseModel):
    """
    Contains the output of the <code>ListHsms</code> operation.
    """

    HsmList: Optional[HsmList] = None
    NextToken: Optional[PaginationToken] = None


class ListHsmsRequest(BaseModel):
    NextToken: Optional[PaginationToken] = None


class ListLunaClientsResponse(BaseModel):
    ClientList: ClientList
    NextToken: Optional[PaginationToken] = None


class ListLunaClientsRequest(BaseModel):
    NextToken: Optional[PaginationToken] = None


class ListTagsForResourceRequest(BaseModel):
    ResourceArn: String


class ModifyHapgResponse(CreateHapgResponse):
    pass


class ModifyHsmResponse(CreateHsmResponse):
    """
    Contains the output of the <a>ModifyHsm</a> operation.
    """

    pass


class ModifyHsmRequest(BaseModel):
    """
    Contains the inputs for the <a>ModifyHsm</a> operation.
    """

    HsmArn: HsmArn
    SubnetId: Optional[SubnetId] = None
    EniIp: Optional[IpAddress] = None
    IamRoleArn: Optional[IamRoleArn] = None
    ExternalId: Optional[ExternalId] = None
    SyslogIp: Optional[IpAddress] = None


class ModifyLunaClientResponse(CreateLunaClientResponse):
    pass


class ModifyLunaClientRequest(BaseModel):
    ClientArn: ClientArn
    Certificate: Certificate


class RemoveTagsFromResourceResponse(AddTagsToResourceResponse):
    pass


class TagList(BaseModel):
    __root__: List[Tag]


class PartitionSerialList(BaseModel):
    __root__: List[PartitionSerial]


class PartitionList(BaseModel):
    __root__: List[PartitionArn]


class TagKeyList(BaseModel):
    __root__: List[TagKey]


class AddTagsToResourceRequest(BaseModel):
    ResourceArn: String
    TagList: TagList


class DescribeHapgResponse(BaseModel):
    """
    Contains the output of the <a>DescribeHapg</a> action.
    """

    HapgArn: Optional[HapgArn] = None
    HapgSerial: Optional[String] = None
    HsmsLastActionFailed: Optional[HsmList] = None
    HsmsPendingDeletion: Optional[HsmList] = None
    HsmsPendingRegistration: Optional[HsmList] = None
    Label: Optional[Label] = None
    LastModifiedTimestamp: Optional[Timestamp] = None
    PartitionSerialList: Optional[PartitionSerialList] = None
    State: Optional[CloudHsmObjectState] = None


class DescribeHsmResponse(BaseModel):
    """
    Contains the output of the <a>DescribeHsm</a> operation.
    """

    HsmArn: Optional[HsmArn] = None
    Status: Optional[HsmStatus] = None
    StatusDetails: Optional[String] = None
    AvailabilityZone: Optional[AZ] = None
    EniId: Optional[EniId] = None
    EniIp: Optional[IpAddress] = None
    SubscriptionType: Optional[SubscriptionType] = None
    SubscriptionStartDate: Optional[Timestamp] = None
    SubscriptionEndDate: Optional[Timestamp] = None
    VpcId: Optional[VpcId] = None
    SubnetId: Optional[SubnetId] = None
    IamRoleArn: Optional[IamRoleArn] = None
    SerialNumber: Optional[HsmSerialNumber] = None
    VendorName: Optional[String] = None
    HsmType: Optional[String] = None
    SoftwareVersion: Optional[String] = None
    SshPublicKey: Optional[SshKey] = None
    SshKeyLastUpdated: Optional[Timestamp] = None
    ServerCertUri: Optional[String] = None
    ServerCertLastUpdated: Optional[Timestamp] = None
    Partitions: Optional[PartitionList] = None


class ListTagsForResourceResponse(BaseModel):
    TagList: TagList


class ModifyHapgRequest(BaseModel):
    HapgArn: HapgArn
    Label: Optional[Label] = None
    PartitionSerialList: Optional[PartitionSerialList] = None


class RemoveTagsFromResourceRequest(BaseModel):
    ResourceArn: String
    TagKeyList: TagKeyList
