# generated by datamodel-codegen:
#   filename:  openapi.yaml
#   timestamp: 2021-12-31T02:53:28+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Annotated, Any, List, Optional

from pydantic import BaseModel, Field


class ValidationException(BaseModel):
    __root__: Any


class ServiceQuotaExceededException(ValidationException):
    pass


class AccessDeniedException(ValidationException):
    pass


class ResourceNotFoundException(ValidationException):
    pass


class ConflictException(ValidationException):
    pass


class ThrottlingException(ValidationException):
    pass


class InternalServerException(ValidationException):
    pass


class String(BaseModel):
    __root__: str


class Integer(BaseModel):
    __root__: int


class TagResourceResponse(BaseModel):
    pass


class UntagResourceResponse(TagResourceResponse):
    pass


class TagKey(String):
    pass


class AWSLocation(BaseModel):
    """
    Specifies a location in AWS.
    """

    Zone: Optional[String] = None
    SubnetArn: Optional[String] = None


class AssociateCustomerGatewayRequest(BaseModel):
    CustomerGatewayArn: String
    DeviceId: String
    LinkId: Optional[String] = None


class AssociateLinkRequest(BaseModel):
    DeviceId: String
    LinkId: String


class AssociateTransitGatewayConnectPeerRequest(BaseModel):
    TransitGatewayConnectPeerArn: String
    DeviceId: String
    LinkId: Optional[String] = None


class Bandwidth(BaseModel):
    """
    Describes bandwidth information.
    """

    UploadSpeed: Optional[Integer] = None
    DownloadSpeed: Optional[Integer] = None


class DateTime(BaseModel):
    __root__: datetime


class ConnectionState(Enum):
    PENDING = 'PENDING'
    AVAILABLE = 'AVAILABLE'
    DELETING = 'DELETING'
    UPDATING = 'UPDATING'


class Location(BaseModel):
    """
    Describes a location.
    """

    Address: Optional[String] = None
    Latitude: Optional[String] = None
    Longitude: Optional[String] = None


class CustomerGatewayAssociationState(Enum):
    PENDING = 'PENDING'
    AVAILABLE = 'AVAILABLE'
    DELETING = 'DELETING'
    DELETED = 'DELETED'


class DeleteConnectionRequest(BaseModel):
    pass


class DeleteDeviceRequest(BaseModel):
    pass


class DeleteGlobalNetworkRequest(BaseModel):
    pass


class DeleteLinkRequest(BaseModel):
    pass


class DeleteSiteRequest(BaseModel):
    pass


class DeregisterTransitGatewayRequest(BaseModel):
    pass


class StringList(BaseModel):
    __root__: List[String]


class MaxResults(BaseModel):
    __root__: Annotated[int, Field(ge=1.0, le=500.0)]


class DescribeGlobalNetworksRequest(BaseModel):
    pass


class DisassociateCustomerGatewayRequest(BaseModel):
    pass


class DisassociateLinkRequest(BaseModel):
    pass


class DisassociateTransitGatewayConnectPeerRequest(BaseModel):
    pass


class GetConnectionsRequest(BaseModel):
    pass


class GetCustomerGatewayAssociationsRequest(BaseModel):
    pass


class GetDevicesRequest(BaseModel):
    pass


class GetLinkAssociationsRequest(BaseModel):
    pass


class GetLinksRequest(BaseModel):
    pass


class GetSitesRequest(BaseModel):
    pass


class GetTransitGatewayConnectPeerAssociationsRequest(BaseModel):
    pass


class GetTransitGatewayRegistrationsRequest(BaseModel):
    pass


class ResourceARN(String):
    pass


class ListTagsForResourceRequest(BaseModel):
    pass


class RegisterTransitGatewayRequest(BaseModel):
    TransitGatewayArn: String


class TagValue(String):
    pass


class TagKeyList(BaseModel):
    __root__: List[TagKey]


class TransitGatewayRegistrationState(Enum):
    PENDING = 'PENDING'
    AVAILABLE = 'AVAILABLE'
    DELETING = 'DELETING'
    DELETED = 'DELETED'
    FAILED = 'FAILED'


class UntagResourceRequest(BaseModel):
    pass


class UpdateConnectionRequest(BaseModel):
    LinkId: Optional[String] = None
    ConnectedLinkId: Optional[String] = None
    Description: Optional[String] = None


class UpdateDeviceRequest(BaseModel):
    AWSLocation: Optional[AWSLocation] = None
    Description: Optional[String] = None
    Type: Optional[String] = None
    Vendor: Optional[String] = None
    Model: Optional[String] = None
    SerialNumber: Optional[String] = None
    Location: Optional[Location] = None
    SiteId: Optional[String] = None


class UpdateGlobalNetworkRequest(BaseModel):
    Description: Optional[String] = None


class UpdateLinkRequest(BaseModel):
    Description: Optional[String] = None
    Type: Optional[String] = None
    Bandwidth: Optional[Bandwidth] = None
    Provider: Optional[String] = None


class UpdateSiteRequest(BaseModel):
    Description: Optional[String] = None
    Location: Optional[Location] = None


class Tag(BaseModel):
    """
    Describes a tag.
    """

    Key: Optional[TagKey] = None
    Value: Optional[TagValue] = None


class CustomerGatewayAssociation(BaseModel):
    """
    Describes the association between a customer gateway, a device, and a link.
    """

    CustomerGatewayArn: Optional[String] = None
    GlobalNetworkId: Optional[String] = None
    DeviceId: Optional[String] = None
    LinkId: Optional[String] = None
    State: Optional[CustomerGatewayAssociationState] = None


class LinkAssociation(BaseModel):
    """
    Describes the association between a device and a link.
    """

    GlobalNetworkId: Optional[String] = None
    DeviceId: Optional[String] = None
    LinkId: Optional[String] = None
    LinkAssociationState: Optional[CustomerGatewayAssociationState] = None


class TransitGatewayConnectPeerAssociation(BaseModel):
    """
    Describes a transit gateway Connect peer association.
    """

    TransitGatewayConnectPeerArn: Optional[String] = None
    GlobalNetworkId: Optional[String] = None
    DeviceId: Optional[String] = None
    LinkId: Optional[String] = None
    State: Optional[CustomerGatewayAssociationState] = None


class TagList(BaseModel):
    __root__: List[Tag]


class Connection(BaseModel):
    """
    Describes a connection.
    """

    ConnectionId: Optional[String] = None
    ConnectionArn: Optional[String] = None
    GlobalNetworkId: Optional[String] = None
    DeviceId: Optional[String] = None
    ConnectedDeviceId: Optional[String] = None
    LinkId: Optional[String] = None
    ConnectedLinkId: Optional[String] = None
    Description: Optional[String] = None
    CreatedAt: Optional[DateTime] = None
    State: Optional[ConnectionState] = None
    Tags: Optional[TagList] = None


class ConnectionList(BaseModel):
    __root__: List[Connection]


class CreateConnectionRequest(BaseModel):
    DeviceId: String
    ConnectedDeviceId: String
    LinkId: Optional[String] = None
    ConnectedLinkId: Optional[String] = None
    Description: Optional[String] = None
    Tags: Optional[TagList] = None


class CreateDeviceRequest(BaseModel):
    AWSLocation: Optional[AWSLocation] = None
    Description: Optional[String] = None
    Type: Optional[String] = None
    Vendor: Optional[String] = None
    Model: Optional[String] = None
    SerialNumber: Optional[String] = None
    Location: Optional[Location] = None
    SiteId: Optional[String] = None
    Tags: Optional[TagList] = None


class Device(BaseModel):
    """
    Describes a device.
    """

    DeviceId: Optional[String] = None
    DeviceArn: Optional[String] = None
    GlobalNetworkId: Optional[String] = None
    AWSLocation: Optional[AWSLocation] = None
    Description: Optional[String] = None
    Type: Optional[String] = None
    Vendor: Optional[String] = None
    Model: Optional[String] = None
    SerialNumber: Optional[String] = None
    Location: Optional[Location] = None
    SiteId: Optional[String] = None
    CreatedAt: Optional[DateTime] = None
    State: Optional[ConnectionState] = None
    Tags: Optional[TagList] = None


class CreateGlobalNetworkRequest(BaseModel):
    Description: Optional[String] = None
    Tags: Optional[TagList] = None


class GlobalNetwork(BaseModel):
    """
    Describes a global network.
    """

    GlobalNetworkId: Optional[String] = None
    GlobalNetworkArn: Optional[String] = None
    Description: Optional[String] = None
    CreatedAt: Optional[DateTime] = None
    State: Optional[ConnectionState] = None
    Tags: Optional[TagList] = None


class CreateLinkRequest(BaseModel):
    Description: Optional[String] = None
    Type: Optional[String] = None
    Bandwidth: Bandwidth
    Provider: Optional[String] = None
    SiteId: String
    Tags: Optional[TagList] = None


class Link(BaseModel):
    """
    Describes a link.
    """

    LinkId: Optional[String] = None
    LinkArn: Optional[String] = None
    GlobalNetworkId: Optional[String] = None
    SiteId: Optional[String] = None
    Description: Optional[String] = None
    Type: Optional[String] = None
    Bandwidth: Optional[Bandwidth] = None
    Provider: Optional[String] = None
    CreatedAt: Optional[DateTime] = None
    State: Optional[ConnectionState] = None
    Tags: Optional[TagList] = None


class CreateSiteRequest(BaseModel):
    Description: Optional[String] = None
    Location: Optional[Location] = None
    Tags: Optional[TagList] = None


class Site(BaseModel):
    """
    Describes a site.
    """

    SiteId: Optional[String] = None
    SiteArn: Optional[String] = None
    GlobalNetworkId: Optional[String] = None
    Description: Optional[String] = None
    Location: Optional[Location] = None
    CreatedAt: Optional[DateTime] = None
    State: Optional[ConnectionState] = None
    Tags: Optional[TagList] = None


class CustomerGatewayAssociationList(BaseModel):
    __root__: List[CustomerGatewayAssociation]


class GlobalNetworkList(BaseModel):
    __root__: List[GlobalNetwork]


class DeviceList(BaseModel):
    __root__: List[Device]


class LinkAssociationList(BaseModel):
    __root__: List[LinkAssociation]


class LinkList(BaseModel):
    __root__: List[Link]


class SiteList(BaseModel):
    __root__: List[Site]


class TransitGatewayConnectPeerAssociationList(BaseModel):
    __root__: List[TransitGatewayConnectPeerAssociation]


class TagResourceRequest(BaseModel):
    Tags: TagList


class TransitGatewayRegistrationStateReason(BaseModel):
    """
    Describes the status of a transit gateway registration.
    """

    Code: Optional[TransitGatewayRegistrationState] = None
    Message: Optional[String] = None


class AssociateCustomerGatewayResponse(BaseModel):
    CustomerGatewayAssociation: Optional[CustomerGatewayAssociation] = None


class AssociateLinkResponse(BaseModel):
    LinkAssociation: Optional[LinkAssociation] = None


class AssociateTransitGatewayConnectPeerResponse(BaseModel):
    TransitGatewayConnectPeerAssociation: Optional[
        TransitGatewayConnectPeerAssociation
    ] = None


class CreateConnectionResponse(BaseModel):
    Connection: Optional[Connection] = None


class CreateDeviceResponse(BaseModel):
    Device: Optional[Device] = None


class CreateGlobalNetworkResponse(BaseModel):
    GlobalNetwork: Optional[GlobalNetwork] = None


class CreateLinkResponse(BaseModel):
    Link: Optional[Link] = None


class CreateSiteResponse(BaseModel):
    Site: Optional[Site] = None


class DeleteConnectionResponse(CreateConnectionResponse):
    pass


class DeleteDeviceResponse(CreateDeviceResponse):
    pass


class DeleteGlobalNetworkResponse(CreateGlobalNetworkResponse):
    pass


class DeleteLinkResponse(CreateLinkResponse):
    pass


class DeleteSiteResponse(CreateSiteResponse):
    pass


class DescribeGlobalNetworksResponse(BaseModel):
    GlobalNetworks: Optional[GlobalNetworkList] = None
    NextToken: Optional[String] = None


class DisassociateCustomerGatewayResponse(AssociateCustomerGatewayResponse):
    pass


class DisassociateLinkResponse(AssociateLinkResponse):
    pass


class DisassociateTransitGatewayConnectPeerResponse(
    AssociateTransitGatewayConnectPeerResponse
):
    pass


class GetConnectionsResponse(BaseModel):
    Connections: Optional[ConnectionList] = None
    NextToken: Optional[String] = None


class GetCustomerGatewayAssociationsResponse(BaseModel):
    CustomerGatewayAssociations: Optional[CustomerGatewayAssociationList] = None
    NextToken: Optional[String] = None


class GetDevicesResponse(BaseModel):
    Devices: Optional[DeviceList] = None
    NextToken: Optional[String] = None


class GetLinkAssociationsResponse(BaseModel):
    LinkAssociations: Optional[LinkAssociationList] = None
    NextToken: Optional[String] = None


class GetLinksResponse(BaseModel):
    Links: Optional[LinkList] = None
    NextToken: Optional[String] = None


class GetSitesResponse(BaseModel):
    Sites: Optional[SiteList] = None
    NextToken: Optional[String] = None


class GetTransitGatewayConnectPeerAssociationsResponse(BaseModel):
    TransitGatewayConnectPeerAssociations: Optional[
        TransitGatewayConnectPeerAssociationList
    ] = None
    NextToken: Optional[String] = None


class ListTagsForResourceResponse(BaseModel):
    TagList: Optional[TagList] = None


class UpdateConnectionResponse(CreateConnectionResponse):
    pass


class UpdateDeviceResponse(CreateDeviceResponse):
    pass


class UpdateGlobalNetworkResponse(CreateGlobalNetworkResponse):
    pass


class UpdateLinkResponse(CreateLinkResponse):
    pass


class UpdateSiteResponse(CreateSiteResponse):
    pass


class TransitGatewayRegistration(BaseModel):
    """
    Describes the registration of a transit gateway to a global network.
    """

    GlobalNetworkId: Optional[String] = None
    TransitGatewayArn: Optional[String] = None
    State: Optional[TransitGatewayRegistrationStateReason] = None


class TransitGatewayRegistrationList(BaseModel):
    __root__: List[TransitGatewayRegistration]


class DeregisterTransitGatewayResponse(BaseModel):
    TransitGatewayRegistration: Optional[TransitGatewayRegistration] = None


class GetTransitGatewayRegistrationsResponse(BaseModel):
    TransitGatewayRegistrations: Optional[TransitGatewayRegistrationList] = None
    NextToken: Optional[String] = None


class RegisterTransitGatewayResponse(DeregisterTransitGatewayResponse):
    pass
