# generated by datamodel-codegen:
#   filename:  openapi.yaml
#   timestamp: 2021-12-31T02:50:11+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Annotated, Any, List, Optional

from pydantic import BaseModel, Extra, Field


class InvalidParameterException(BaseModel):
    __root__: Any


class DependencyException(InvalidParameterException):
    pass


class ResourceNotFoundException(InvalidParameterException):
    pass


class String(BaseModel):
    __root__: str


class ResourceLimitExceededException(InvalidParameterException):
    pass


class DataflowEndpointGroupIdResponse(BaseModel):
    """
    <p/>
    """

    dataflowEndpointGroupId: Optional[String] = None


class MissionProfileIdResponse(BaseModel):
    """
    <p/>
    """

    missionProfileId: Optional[String] = None


class ContactStatus(Enum):
    AVAILABLE = 'AVAILABLE'
    AWS_CANCELLED = 'AWS_CANCELLED'
    AWS_FAILED = 'AWS_FAILED'
    CANCELLED = 'CANCELLED'
    CANCELLING = 'CANCELLING'
    COMPLETED = 'COMPLETED'
    FAILED = 'FAILED'
    FAILED_TO_SCHEDULE = 'FAILED_TO_SCHEDULE'
    PASS = 'PASS'
    POSTPASS = 'POSTPASS'
    PREPASS = 'PREPASS'
    SCHEDULED = 'SCHEDULED'
    SCHEDULING = 'SCHEDULING'


class TagResourceResponse(BaseModel):
    """
    <p/>
    """

    pass


class UntagResourceResponse(TagResourceResponse):
    """
    <p/>
    """

    pass


class AngleUnits(Enum):
    DEGREE_ANGLE = 'DEGREE_ANGLE'
    RADIAN = 'RADIAN'


class AntennaDemodDecodeDetails(BaseModel):
    """
    Details about an antenna demod decode <code>Config</code> used in a contact.
    """

    outputNode: Optional[String] = None


class Boolean(BaseModel):
    __root__: bool


class BandwidthUnits(Enum):
    GHz = 'GHz'
    MHz = 'MHz'
    kHz = 'kHz'


class BucketArn(String):
    pass


class CancelContactRequest(BaseModel):
    """
    <p/>
    """

    pass


class ConfigArn(String):
    pass


class ConfigCapabilityType(Enum):
    antenna_downlink = 'antenna-downlink'
    antenna_downlink_demod_decode = 'antenna-downlink-demod-decode'
    antenna_uplink = 'antenna-uplink'
    dataflow_endpoint = 'dataflow-endpoint'
    tracking = 'tracking'
    uplink_echo = 'uplink-echo'
    s3_recording = 's3-recording'


class S3RecordingDetails(BaseModel):
    """
    Details about an S3 recording <code>Config</code> used in a contact.
    """

    bucketArn: Optional[BucketArn] = None
    keyTemplate: Optional[String] = None


class ConfigListItem(BaseModel):
    """
    An item in a list of <code>Config</code> objects.
    """

    configArn: Optional[ConfigArn] = None
    configId: Optional[String] = None
    configType: Optional[ConfigCapabilityType] = None
    name: Optional[String] = None


class ConfigList(BaseModel):
    __root__: List[ConfigListItem]


class Timestamp(BaseModel):
    __root__: datetime


class MissionProfileArn(String):
    pass


class SatelliteArn(String):
    pass


class TagsMap(BaseModel):
    pass

    class Config:
        extra = Extra.allow


class SafeName(BaseModel):
    __root__: Annotated[
        str, Field(max_length=256, min_length=1, regex='^[ a-zA-Z0-9_:-]{1,256}$')
    ]


class DurationInSeconds(BaseModel):
    __root__: Annotated[int, Field(ge=1.0, le=21600.0)]


class Criticality(Enum):
    PREFERRED = 'PREFERRED'
    REMOVED = 'REMOVED'
    REQUIRED = 'REQUIRED'


class DataflowEndpointMtuInteger(BaseModel):
    __root__: Annotated[int, Field(ge=1400.0, le=1500.0)]


class EndpointStatus(Enum):
    created = 'created'
    creating = 'creating'
    deleted = 'deleted'
    deleting = 'deleting'
    failed = 'failed'


class DataflowEndpointGroupArn(String):
    pass


class DataflowEndpointListItem(BaseModel):
    """
    Item in a list of <code>DataflowEndpoint</code> groups.
    """

    dataflowEndpointGroupArn: Optional[DataflowEndpointGroupArn] = None
    dataflowEndpointGroupId: Optional[String] = None


class DataflowEndpointGroupList(BaseModel):
    __root__: List[DataflowEndpointListItem]


class JsonString(BaseModel):
    __root__: Annotated[
        str,
        Field(
            max_length=8192, min_length=2, regex='^[{}\\[\\]:.,"0-9A-z\\-_\\s]{2,8192}$'
        ),
    ]


class DeleteConfigRequest(BaseModel):
    """
    <p/>
    """

    pass


class DeleteDataflowEndpointGroupRequest(BaseModel):
    """
    <p/>
    """

    pass


class DeleteMissionProfileRequest(BaseModel):
    """
    <p/>
    """

    pass


class DescribeContactRequest(BaseModel):
    """
    <p/>
    """

    pass


class Double(BaseModel):
    __root__: float


class EirpUnits(Enum):
    dBW = 'dBW'


class Frequency(BaseModel):
    """
    Object that describes the frequency.
    """

    units: BandwidthUnits
    value: Double


class FrequencyBandwidth(Frequency):
    """
    Object that describes the frequency bandwidth.
    """

    pass


class GetConfigRequest(BaseModel):
    """
    <p/>
    """

    pass


class GetDataflowEndpointGroupRequest(BaseModel):
    """
    <p/>
    """

    pass


class Integer(BaseModel):
    __root__: int


class GetMinuteUsageRequest(BaseModel):
    """
    <p/>
    """

    month: Integer
    year: Integer


class GetMissionProfileRequest(BaseModel):
    """
    <p/>
    """

    pass


class GetSatelliteRequest(BaseModel):
    """
    <p/>
    """

    pass


class GroundStationIdList(BaseModel):
    __root__: List[String]


class NoradSatelliteID(BaseModel):
    __root__: Annotated[int, Field(ge=1.0, le=99999.0)]


class Uuid(BaseModel):
    __root__: Annotated[
        str,
        Field(
            max_length=128,
            min_length=1,
            regex='[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}',
        ),
    ]


class GroundStationData(BaseModel):
    """
    Information about the ground station data.
    """

    groundStationId: Optional[String] = None
    groundStationName: Optional[String] = None
    region: Optional[String] = None


class GroundStationList(BaseModel):
    __root__: List[GroundStationData]


class ListConfigsRequest(BaseModel):
    """
    <p/>
    """

    pass


class StatusList(BaseModel):
    __root__: List[ContactStatus]


class ListContactsRequest(BaseModel):
    """
    <p/>
    """

    endTime: Timestamp
    groundStation: Optional[String] = None
    maxResults: Optional[Integer] = None
    missionProfileArn: Optional[MissionProfileArn] = None
    nextToken: Optional[String] = None
    satelliteArn: Optional[SatelliteArn] = None
    startTime: Timestamp
    statusList: StatusList


class ListDataflowEndpointGroupsRequest(BaseModel):
    """
    <p/>
    """

    pass


class ListGroundStationsRequest(BaseModel):
    """
    <p/>
    """

    pass


class ListMissionProfilesRequest(BaseModel):
    """
    <p/>
    """

    pass


class ListSatellitesRequest(BaseModel):
    """
    <p/>
    """

    pass


class ListTagsForResourceRequest(BaseModel):
    """
    <p/>
    """

    pass


class MissionProfileListItem(BaseModel):
    """
    Item in a list of mission profiles.
    """

    missionProfileArn: Optional[MissionProfileArn] = None
    missionProfileId: Optional[String] = None
    name: Optional[String] = None
    region: Optional[String] = None


class Polarization(Enum):
    LEFT_HAND = 'LEFT_HAND'
    NONE = 'NONE'
    RIGHT_HAND = 'RIGHT_HAND'


class ReserveContactRequest(BaseModel):
    """
    <p/>
    """

    endTime: Timestamp
    groundStation: String
    missionProfileArn: MissionProfileArn
    satelliteArn: SatelliteArn
    startTime: Timestamp
    tags: Optional[TagsMap] = None


class RoleArn(String):
    pass


class S3KeyPrefix(BaseModel):
    __root__: Annotated[
        str,
        Field(
            max_length=900,
            min_length=1,
            regex='^([a-zA-Z0-9_\\-=/]|\\{satellite_id\\}|\\{config\\-name}|\\{s3\\-config-id}|\\{year\\}|\\{month\\}|\\{day\\}){1,900}$',
        ),
    ]


class SatelliteListItem(BaseModel):
    """
    Item in a list of satellites.
    """

    groundStations: Optional[GroundStationIdList] = None
    noradSatelliteID: Optional[NoradSatelliteID] = None
    satelliteArn: Optional[SatelliteArn] = None
    satelliteId: Optional[Uuid] = None


class SecurityGroupIdList(GroundStationIdList):
    pass


class SubnetList(GroundStationIdList):
    pass


class TagKeys(GroundStationIdList):
    pass


class TagResourceRequest(BaseModel):
    """
    <p/>
    """

    tags: TagsMap


class UntagResourceRequest(BaseModel):
    """
    <p/>
    """

    pass


class ContactIdResponse(BaseModel):
    """
    <p/>
    """

    contactId: Optional[String] = None


class ConfigIdResponse(BaseModel):
    """
    <p/>
    """

    configArn: Optional[ConfigArn] = None
    configId: Optional[String] = None
    configType: Optional[ConfigCapabilityType] = None


class DataflowEndpointConfig(BaseModel):
    """
    Information about the dataflow endpoint <code>Config</code>.
    """

    dataflowEndpointName: String
    dataflowEndpointRegion: Optional[String] = None


class S3RecordingConfig(BaseModel):
    """
    Information about an S3 recording <code>Config</code>.
    """

    bucketArn: BucketArn
    prefix: Optional[S3KeyPrefix] = None
    roleArn: RoleArn


class TrackingConfig(BaseModel):
    """
    Object that determines whether tracking should be used during a contact executed with this <code>Config</code> in the mission profile.
    """

    autotrack: Criticality


class UplinkEchoConfig(BaseModel):
    """
    <p>Information about an uplink echo <code>Config</code>.</p> <p>Parameters from the <code>AntennaUplinkConfig</code>, corresponding to the specified <code>AntennaUplinkConfigArn</code>, are used when this <code>UplinkEchoConfig</code> is used in a contact.</p>
    """

    antennaUplinkConfigArn: ConfigArn
    enabled: Boolean


class DataflowEdge(BaseModel):
    __root__: Annotated[List[ConfigArn], Field(max_items=2, min_items=2)]


class GetMinuteUsageResponse(BaseModel):
    """
    <p/>
    """

    estimatedMinutesRemaining: Optional[Integer] = None
    isReservedMinutesCustomer: Optional[Boolean] = None
    totalReservedMinuteAllocation: Optional[Integer] = None
    totalScheduledMinutes: Optional[Integer] = None
    upcomingMinutesScheduled: Optional[Integer] = None


class GetSatelliteResponse(SatelliteListItem):
    """
    <p/>
    """

    pass


class ListConfigsResponse(BaseModel):
    """
    <p/>
    """

    configList: Optional[ConfigList] = None
    nextToken: Optional[String] = None


class ListDataflowEndpointGroupsResponse(BaseModel):
    """
    <p/>
    """

    dataflowEndpointGroupList: Optional[DataflowEndpointGroupList] = None
    nextToken: Optional[String] = None


class ListGroundStationsResponse(BaseModel):
    """
    <p/>
    """

    groundStationList: Optional[GroundStationList] = None
    nextToken: Optional[String] = None


class ListTagsForResourceResponse(BaseModel):
    """
    <p/>
    """

    tags: Optional[TagsMap] = None


class SpectrumConfig(BaseModel):
    """
    Object that describes a spectral <code>Config</code>.
    """

    bandwidth: FrequencyBandwidth
    centerFrequency: Frequency
    polarization: Optional[Polarization] = None


class DecodeConfig(BaseModel):
    """
    Information about the decode <code>Config</code>.
    """

    unvalidatedJSON: JsonString


class DemodulationConfig(DecodeConfig):
    """
    Information about the demodulation <code>Config</code>.
    """

    pass


class UplinkSpectrumConfig(BaseModel):
    """
    Information about the uplink spectral <code>Config</code>.
    """

    centerFrequency: Frequency
    polarization: Optional[Polarization] = None


class Eirp(BaseModel):
    """
    Object that represents EIRP.
    """

    units: EirpUnits
    value: Double


class Elevation(BaseModel):
    """
    Elevation angle of the satellite in the sky during a contact.
    """

    unit: AngleUnits
    value: Double


class ContactData(BaseModel):
    """
    Data describing a contact.
    """

    contactId: Optional[String] = None
    contactStatus: Optional[ContactStatus] = None
    endTime: Optional[Timestamp] = None
    errorMessage: Optional[String] = None
    groundStation: Optional[String] = None
    maximumElevation: Optional[Elevation] = None
    missionProfileArn: Optional[MissionProfileArn] = None
    postPassEndTime: Optional[Timestamp] = None
    prePassStartTime: Optional[Timestamp] = None
    region: Optional[String] = None
    satelliteArn: Optional[SatelliteArn] = None
    startTime: Optional[Timestamp] = None
    tags: Optional[TagsMap] = None


class ContactList(BaseModel):
    __root__: List[ContactData]


class DataflowEdgeList(BaseModel):
    __root__: List[DataflowEdge]


class CreateMissionProfileRequest(BaseModel):
    """
    <p/>
    """

    contactPostPassDurationSeconds: Optional[DurationInSeconds] = None
    contactPrePassDurationSeconds: Optional[DurationInSeconds] = None
    dataflowEdges: DataflowEdgeList
    minimumViableContactDurationSeconds: DurationInSeconds
    name: SafeName
    tags: Optional[TagsMap] = None
    trackingConfigArn: ConfigArn


class SocketAddress(BaseModel):
    """
    Information about the socket address.
    """

    name: String
    port: Integer


class DataflowEndpoint(BaseModel):
    """
    Information about a dataflow endpoint.
    """

    address: Optional[SocketAddress] = None
    mtu: Optional[DataflowEndpointMtuInteger] = None
    name: Optional[SafeName] = None
    status: Optional[EndpointStatus] = None


class SecurityDetails(BaseModel):
    """
    Information about endpoints.
    """

    roleArn: RoleArn
    securityGroupIds: SecurityGroupIdList
    subnetIds: SubnetList


class MissionProfileList(BaseModel):
    __root__: List[MissionProfileListItem]


class SatelliteList(BaseModel):
    __root__: List[SatelliteListItem]


class UpdateMissionProfileRequest(BaseModel):
    """
    <p/>
    """

    contactPostPassDurationSeconds: Optional[DurationInSeconds] = None
    contactPrePassDurationSeconds: Optional[DurationInSeconds] = None
    dataflowEdges: Optional[DataflowEdgeList] = None
    minimumViableContactDurationSeconds: Optional[DurationInSeconds] = None
    name: Optional[SafeName] = None
    trackingConfigArn: Optional[ConfigArn] = None


class AntennaDownlinkConfig(BaseModel):
    """
    Information about how AWS Ground Station should configure an antenna for downlink during a contact.
    """

    spectrumConfig: SpectrumConfig


class AntennaDownlinkDemodDecodeConfig(BaseModel):
    """
    Information about how AWS Ground Station should conﬁgure an antenna for downlink demod decode during a contact.
    """

    decodeConfig: DecodeConfig
    demodulationConfig: DemodulationConfig
    spectrumConfig: SpectrumConfig


class AntennaUplinkConfig(BaseModel):
    """
    Information about the uplink <code>Config</code> of an antenna.
    """

    spectrumConfig: UplinkSpectrumConfig
    targetEirp: Eirp
    transmitDisabled: Optional[Boolean] = None


class EndpointDetails(BaseModel):
    """
    Information about the endpoint details.
    """

    endpoint: Optional[DataflowEndpoint] = None
    securityDetails: Optional[SecurityDetails] = None


class GetMissionProfileResponse(BaseModel):
    """
    <p/>
    """

    contactPostPassDurationSeconds: Optional[DurationInSeconds] = None
    contactPrePassDurationSeconds: Optional[DurationInSeconds] = None
    dataflowEdges: Optional[DataflowEdgeList] = None
    minimumViableContactDurationSeconds: Optional[DurationInSeconds] = None
    missionProfileArn: Optional[MissionProfileArn] = None
    missionProfileId: Optional[String] = None
    name: Optional[String] = None
    region: Optional[String] = None
    tags: Optional[TagsMap] = None
    trackingConfigArn: Optional[ConfigArn] = None


class ListContactsResponse(BaseModel):
    """
    <p/>
    """

    contactList: Optional[ContactList] = None
    nextToken: Optional[String] = None


class ListMissionProfilesResponse(BaseModel):
    """
    <p/>
    """

    missionProfileList: Optional[MissionProfileList] = None
    nextToken: Optional[String] = None


class ListSatellitesResponse(BaseModel):
    """
    <p/>
    """

    nextToken: Optional[String] = None
    satellites: Optional[SatelliteList] = None


class ConfigDetails(BaseModel):
    """
    Details for certain <code>Config</code> object types in a contact.
    """

    antennaDemodDecodeDetails: Optional[AntennaDemodDecodeDetails] = None
    endpointDetails: Optional[EndpointDetails] = None
    s3RecordingDetails: Optional[S3RecordingDetails] = None


class ConfigTypeData(BaseModel):
    """
    <p>Object containing the parameters of a <code>Config</code>.</p> <p>See the subtype definitions for what each type of <code>Config</code> contains.</p>
    """

    antennaDownlinkConfig: Optional[AntennaDownlinkConfig] = None
    antennaDownlinkDemodDecodeConfig: Optional[AntennaDownlinkDemodDecodeConfig] = None
    antennaUplinkConfig: Optional[AntennaUplinkConfig] = None
    dataflowEndpointConfig: Optional[DataflowEndpointConfig] = None
    s3RecordingConfig: Optional[S3RecordingConfig] = None
    trackingConfig: Optional[TrackingConfig] = None
    uplinkEchoConfig: Optional[UplinkEchoConfig] = None


class CreateConfigRequest(BaseModel):
    """
    <p/>
    """

    configData: ConfigTypeData
    name: SafeName
    tags: Optional[TagsMap] = None


class EndpointDetailsList(BaseModel):
    __root__: List[EndpointDetails]


class CreateDataflowEndpointGroupRequest(BaseModel):
    """
    <p/>
    """

    endpointDetails: EndpointDetailsList
    tags: Optional[TagsMap] = None


class Destination(BaseModel):
    """
    Dataflow details for the destination side.
    """

    configDetails: Optional[ConfigDetails] = None
    configId: Optional[String] = None
    configType: Optional[ConfigCapabilityType] = None
    dataflowDestinationRegion: Optional[String] = None


class Source(BaseModel):
    """
    Dataflow details for the source side.
    """

    configDetails: Optional[ConfigDetails] = None
    configId: Optional[String] = None
    configType: Optional[ConfigCapabilityType] = None
    dataflowSourceRegion: Optional[String] = None


class DataflowDetail(BaseModel):
    """
    Information about a dataflow edge used in a contact.
    """

    destination: Optional[Destination] = None
    errorMessage: Optional[String] = None
    source: Optional[Source] = None


class DataflowList(BaseModel):
    __root__: List[DataflowDetail]


class UpdateConfigRequest(BaseModel):
    """
    <p/>
    """

    configData: ConfigTypeData
    name: SafeName


class DescribeContactResponse(BaseModel):
    """
    <p/>
    """

    contactId: Optional[String] = None
    contactStatus: Optional[ContactStatus] = None
    dataflowList: Optional[DataflowList] = None
    endTime: Optional[Timestamp] = None
    errorMessage: Optional[String] = None
    groundStation: Optional[String] = None
    maximumElevation: Optional[Elevation] = None
    missionProfileArn: Optional[MissionProfileArn] = None
    postPassEndTime: Optional[Timestamp] = None
    prePassStartTime: Optional[Timestamp] = None
    region: Optional[String] = None
    satelliteArn: Optional[SatelliteArn] = None
    startTime: Optional[Timestamp] = None
    tags: Optional[TagsMap] = None


class GetConfigResponse(BaseModel):
    """
    <p/>
    """

    configArn: ConfigArn
    configData: ConfigTypeData
    configId: String
    configType: Optional[ConfigCapabilityType] = None
    name: String
    tags: Optional[TagsMap] = None


class GetDataflowEndpointGroupResponse(BaseModel):
    """
    <p/>
    """

    dataflowEndpointGroupArn: Optional[DataflowEndpointGroupArn] = None
    dataflowEndpointGroupId: Optional[String] = None
    endpointsDetails: Optional[EndpointDetailsList] = None
    tags: Optional[TagsMap] = None
