# generated by datamodel-codegen:
#   filename:  openapi.yaml
#   timestamp: 2021-12-31T02:51:09+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Annotated, Any, List, Optional

from pydantic import BaseModel, Extra, Field


class ChannelArn(BaseModel):
    __root__: Annotated[
        str,
        Field(
            max_length=128,
            min_length=1,
            regex='^arn:aws:[is]vs:[a-z0-9-]+:[0-9]+:channel/[a-zA-Z0-9-]+$',
        ),
    ]


class StreamKeyArn(BaseModel):
    __root__: Annotated[
        str,
        Field(
            max_length=128,
            min_length=1,
            regex='^arn:aws:[is]vs:[a-z0-9-]+:[0-9]+:stream-key/[a-zA-Z0-9-]+$',
        ),
    ]


class TagValue(BaseModel):
    __root__: Annotated[str, Field(max_length=256)]


class ValidationException(BaseModel):
    __root__: Any


class AccessDeniedException(ValidationException):
    pass


class ResourceNotFoundException(ValidationException):
    pass


class ServiceQuotaExceededException(ValidationException):
    pass


class PendingVerification(ValidationException):
    pass


class ConflictException(ValidationException):
    pass


class InternalServerException(ValidationException):
    pass


class DeletePlaybackKeyPairResponse(BaseModel):
    pass


class ChannelNotBroadcasting(ValidationException):
    pass


class ThrottlingException(ValidationException):
    pass


class StopStreamResponse(DeletePlaybackKeyPairResponse):
    pass


class StreamUnavailable(ValidationException):
    pass


class TagResourceResponse(DeletePlaybackKeyPairResponse):
    pass


class UntagResourceResponse(DeletePlaybackKeyPairResponse):
    pass


class TagKey(BaseModel):
    __root__: Annotated[str, Field(max_length=128, min_length=1)]


class ResourceArn(BaseModel):
    __root__: Annotated[
        str,
        Field(
            max_length=128,
            min_length=1,
            regex='^arn:aws:[is]vs:[a-z0-9-]+:[0-9]+:[a-z-]/[a-zA-Z0-9-]+$',
        ),
    ]


class ErrorCode(BaseModel):
    __root__: str


class ErrorMessage(ErrorCode):
    pass


class BatchError(BaseModel):
    """
    Error related to a specific channel, specified by its ARN.
    """

    arn: Optional[ResourceArn] = None
    code: Optional[ErrorCode] = None
    message: Optional[ErrorMessage] = None


class BatchErrors(BaseModel):
    __root__: List[BatchError]


class ChannelArnList(BaseModel):
    __root__: Annotated[List[ChannelArn], Field(max_items=50, min_items=1)]


class BatchGetChannelRequest(BaseModel):
    arns: ChannelArnList


class StreamKeyArnList(BaseModel):
    __root__: Annotated[List[StreamKeyArn], Field(max_items=50, min_items=1)]


class BatchGetStreamKeyRequest(BaseModel):
    arns: StreamKeyArnList


class Boolean(BaseModel):
    __root__: bool


class ChannelName(BaseModel):
    __root__: Annotated[
        str, Field(max_length=128, min_length=0, regex='^[a-zA-Z0-9-_]*$')
    ]


class ChannelLatencyMode(Enum):
    NORMAL = 'NORMAL'
    LOW = 'LOW'


class ChannelType(Enum):
    BASIC = 'BASIC'
    STANDARD = 'STANDARD'


class ChannelRecordingConfigurationArn(BaseModel):
    __root__: Annotated[
        str,
        Field(
            max_length=128,
            min_length=0,
            regex='^$|^arn:aws:ivs:[a-z0-9-]+:[0-9]+:recording-configuration/[a-zA-Z0-9-]+$',
        ),
    ]


class IngestEndpoint(ErrorCode):
    pass


class PlaybackURL(ErrorCode):
    pass


class IsAuthorized(Boolean):
    pass


class Tags(BaseModel):
    pass

    class Config:
        extra = Extra.allow


class Channel(BaseModel):
    """
    Object specifying a channel.
    """

    arn: Optional[ChannelArn] = None
    name: Optional[ChannelName] = None
    latencyMode: Optional[ChannelLatencyMode] = None
    type: Optional[ChannelType] = None
    recordingConfigurationArn: Optional[ChannelRecordingConfigurationArn] = None
    ingestEndpoint: Optional[IngestEndpoint] = None
    playbackUrl: Optional[PlaybackURL] = None
    authorized: Optional[IsAuthorized] = None
    tags: Optional[Tags] = None


class ChannelSummary(BaseModel):
    """
    Summary information about a channel.
    """

    arn: Optional[ChannelArn] = None
    name: Optional[ChannelName] = None
    latencyMode: Optional[ChannelLatencyMode] = None
    authorized: Optional[IsAuthorized] = None
    recordingConfigurationArn: Optional[ChannelRecordingConfigurationArn] = None
    tags: Optional[Tags] = None


class ChannelList(BaseModel):
    __root__: List[ChannelSummary]


class CreateChannelRequest(BaseModel):
    name: Optional[ChannelName] = None
    latencyMode: Optional[ChannelLatencyMode] = None
    type: Optional[ChannelType] = None
    authorized: Optional[Boolean] = None
    recordingConfigurationArn: Optional[ChannelRecordingConfigurationArn] = None
    tags: Optional[Tags] = None


class RecordingConfigurationName(ChannelName):
    pass


class CreateStreamKeyRequest(BaseModel):
    channelArn: ChannelArn
    tags: Optional[Tags] = None


class DeleteChannelRequest(BaseModel):
    arn: ChannelArn


class PlaybackKeyPairArn(BaseModel):
    __root__: Annotated[
        str,
        Field(
            max_length=128,
            min_length=1,
            regex='^arn:aws:[is]vs:[a-z0-9-]+:[0-9]+:playback-key/[a-zA-Z0-9-]+$',
        ),
    ]


class DeletePlaybackKeyPairRequest(BaseModel):
    arn: PlaybackKeyPairArn


class RecordingConfigurationArn(BaseModel):
    __root__: Annotated[
        str,
        Field(
            max_length=128,
            min_length=0,
            regex='^arn:aws:ivs:[a-z0-9-]+:[0-9]+:recording-configuration/[a-zA-Z0-9-]+$',
        ),
    ]


class DeleteRecordingConfigurationRequest(BaseModel):
    arn: RecordingConfigurationArn


class DeleteStreamKeyRequest(BaseModel):
    arn: StreamKeyArn


class GetChannelRequest(BaseModel):
    arn: ChannelArn


class GetPlaybackKeyPairRequest(BaseModel):
    arn: PlaybackKeyPairArn


class GetRecordingConfigurationRequest(BaseModel):
    arn: RecordingConfigurationArn


class GetStreamKeyRequest(BaseModel):
    arn: StreamKeyArn


class GetStreamRequest(BaseModel):
    channelArn: ChannelArn


class PlaybackPublicKeyMaterial(ErrorCode):
    pass


class PlaybackKeyPairName(ChannelName):
    pass


class ImportPlaybackKeyPairRequest(BaseModel):
    publicKeyMaterial: PlaybackPublicKeyMaterial
    name: Optional[PlaybackKeyPairName] = None
    tags: Optional[Tags] = None


class PaginationToken(BaseModel):
    __root__: Annotated[str, Field(max_length=500, min_length=0)]


class MaxChannelResults(BaseModel):
    __root__: Annotated[int, Field(ge=1.0, le=50.0)]


class ListChannelsRequest(BaseModel):
    filterByName: Optional[ChannelName] = None
    filterByRecordingConfigurationArn: Optional[ChannelRecordingConfigurationArn] = None
    nextToken: Optional[PaginationToken] = None
    maxResults: Optional[MaxChannelResults] = None


class MaxPlaybackKeyPairResults(MaxChannelResults):
    pass


class ListPlaybackKeyPairsRequest(BaseModel):
    nextToken: Optional[PaginationToken] = None
    maxResults: Optional[MaxPlaybackKeyPairResults] = None


class MaxRecordingConfigurationResults(MaxChannelResults):
    pass


class ListRecordingConfigurationsRequest(BaseModel):
    nextToken: Optional[PaginationToken] = None
    maxResults: Optional[MaxRecordingConfigurationResults] = None


class MaxStreamKeyResults(MaxChannelResults):
    pass


class ListStreamKeysRequest(BaseModel):
    channelArn: ChannelArn
    nextToken: Optional[PaginationToken] = None
    maxResults: Optional[MaxStreamKeyResults] = None


class MaxStreamResults(MaxChannelResults):
    pass


class ListStreamsRequest(BaseModel):
    nextToken: Optional[PaginationToken] = None
    maxResults: Optional[MaxStreamResults] = None


class String(ErrorCode):
    pass


class MaxTagResults(MaxChannelResults):
    pass


class ListTagsForResourceRequest(BaseModel):
    nextToken: Optional[String] = None
    maxResults: Optional[MaxTagResults] = None


class PlaybackKeyPairFingerprint(ErrorCode):
    pass


class PlaybackKeyPairSummary(BaseModel):
    """
    Summary information about a playback key pair.
    """

    arn: Optional[PlaybackKeyPairArn] = None
    name: Optional[PlaybackKeyPairName] = None
    tags: Optional[Tags] = None


class StreamMetadata(BaseModel):
    __root__: Annotated[str, Field(min_length=1)]


class PutMetadataRequest(BaseModel):
    channelArn: ChannelArn
    metadata: StreamMetadata


class RecordingConfigurationState(Enum):
    CREATING = 'CREATING'
    CREATE_FAILED = 'CREATE_FAILED'
    ACTIVE = 'ACTIVE'


class S3DestinationBucketName(BaseModel):
    __root__: Annotated[str, Field(max_length=63, min_length=3, regex='^[a-z0-9-.]+$')]


class StopStreamRequest(BaseModel):
    channelArn: ChannelArn


class StreamStartTime(BaseModel):
    __root__: datetime


class StreamState(Enum):
    LIVE = 'LIVE'
    OFFLINE = 'OFFLINE'


class StreamHealth(Enum):
    HEALTHY = 'HEALTHY'
    STARVING = 'STARVING'
    UNKNOWN = 'UNKNOWN'


class StreamViewerCount(BaseModel):
    __root__: int


class StreamKeyValue(ErrorCode):
    pass


class StreamKeySummary(BaseModel):
    """
    Summary information about a stream key.
    """

    arn: Optional[StreamKeyArn] = None
    channelArn: Optional[ChannelArn] = None
    tags: Optional[Tags] = None


class StreamSummary(BaseModel):
    """
    Summary information about a stream.
    """

    channelArn: Optional[ChannelArn] = None
    state: Optional[StreamState] = None
    health: Optional[StreamHealth] = None
    viewerCount: Optional[StreamViewerCount] = None
    startTime: Optional[StreamStartTime] = None


class TagKeyList(BaseModel):
    __root__: Annotated[List[TagKey], Field(max_items=50, min_items=0)]


class TagResourceRequest(BaseModel):
    tags: Tags


class UntagResourceRequest(BaseModel):
    pass


class UpdateChannelRequest(BaseModel):
    arn: ChannelArn
    name: Optional[ChannelName] = None
    latencyMode: Optional[ChannelLatencyMode] = None
    type: Optional[ChannelType] = None
    authorized: Optional[Boolean] = None
    recordingConfigurationArn: Optional[ChannelRecordingConfigurationArn] = None


class S3DestinationConfiguration(BaseModel):
    """
    A complex type that describes an S3 location where recorded videos will be stored.
    """

    bucketName: S3DestinationBucketName


class GetChannelResponse(BaseModel):
    channel: Optional[Channel] = None


class ListChannelsResponse(BaseModel):
    channels: ChannelList
    nextToken: Optional[PaginationToken] = None


class ListTagsForResourceResponse(BaseModel):
    tags: Tags
    nextToken: Optional[String] = None


class UpdateChannelResponse(GetChannelResponse):
    pass


class Channels(BaseModel):
    __root__: List[Channel]


class StreamKey(BaseModel):
    """
    Object specifying a stream key.
    """

    arn: Optional[StreamKeyArn] = None
    value: Optional[StreamKeyValue] = None
    channelArn: Optional[ChannelArn] = None
    tags: Optional[Tags] = None


class DestinationConfiguration(BaseModel):
    """
    A complex type that describes a location where recorded videos will be stored. Each member represents a type of destination configuration. For recording, you define one and only one type of destination configuration.
    """

    s3: Optional[S3DestinationConfiguration] = None


class CreateRecordingConfigurationRequest(BaseModel):
    name: Optional[RecordingConfigurationName] = None
    destinationConfiguration: DestinationConfiguration
    tags: Optional[Tags] = None


class RecordingConfiguration(BaseModel):
    """
    An object representing a configuration to record a channel stream.
    """

    arn: RecordingConfigurationArn
    name: Optional[RecordingConfigurationName] = None
    destinationConfiguration: DestinationConfiguration
    state: RecordingConfigurationState
    tags: Optional[Tags] = None


class PlaybackKeyPair(BaseModel):
    """
    A key pair used to sign and validate a playback authorization token.
    """

    arn: Optional[PlaybackKeyPairArn] = None
    name: Optional[PlaybackKeyPairName] = None
    fingerprint: Optional[PlaybackKeyPairFingerprint] = None
    tags: Optional[Tags] = None


class Stream(BaseModel):
    """
    Specifies a live video stream that has been ingested and distributed.
    """

    channelArn: Optional[ChannelArn] = None
    playbackUrl: Optional[PlaybackURL] = None
    startTime: Optional[StreamStartTime] = None
    state: Optional[StreamState] = None
    health: Optional[StreamHealth] = None
    viewerCount: Optional[StreamViewerCount] = None


class PlaybackKeyPairList(BaseModel):
    __root__: List[PlaybackKeyPairSummary]


class StreamKeyList(BaseModel):
    __root__: List[StreamKeySummary]


class StreamList(BaseModel):
    __root__: List[StreamSummary]


class RecordingConfigurationSummary(RecordingConfiguration):
    """
    Summary information about a RecordingConfiguration.
    """

    pass


class BatchGetChannelResponse(BaseModel):
    channels: Optional[Channels] = None
    errors: Optional[BatchErrors] = None


class CreateChannelResponse(BaseModel):
    channel: Optional[Channel] = None
    streamKey: Optional[StreamKey] = None


class CreateRecordingConfigurationResponse(BaseModel):
    recordingConfiguration: Optional[RecordingConfiguration] = None


class CreateStreamKeyResponse(BaseModel):
    streamKey: Optional[StreamKey] = None


class GetPlaybackKeyPairResponse(BaseModel):
    keyPair: Optional[PlaybackKeyPair] = None


class GetRecordingConfigurationResponse(CreateRecordingConfigurationResponse):
    pass


class GetStreamResponse(BaseModel):
    stream: Optional[Stream] = None


class GetStreamKeyResponse(CreateStreamKeyResponse):
    pass


class ImportPlaybackKeyPairResponse(GetPlaybackKeyPairResponse):
    pass


class ListPlaybackKeyPairsResponse(BaseModel):
    keyPairs: PlaybackKeyPairList
    nextToken: Optional[PaginationToken] = None


class ListStreamKeysResponse(BaseModel):
    streamKeys: StreamKeyList
    nextToken: Optional[PaginationToken] = None


class ListStreamsResponse(BaseModel):
    streams: StreamList
    nextToken: Optional[PaginationToken] = None


class StreamKeys(BaseModel):
    __root__: List[StreamKey]


class RecordingConfigurationList(BaseModel):
    __root__: List[RecordingConfigurationSummary]


class BatchGetStreamKeyResponse(BaseModel):
    streamKeys: Optional[StreamKeys] = None
    errors: Optional[BatchErrors] = None


class ListRecordingConfigurationsResponse(BaseModel):
    recordingConfigurations: RecordingConfigurationList
    nextToken: Optional[PaginationToken] = None