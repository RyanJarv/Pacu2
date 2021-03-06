# generated by datamodel-codegen:
#   filename:  openapi.yaml
#   timestamp: 2021-12-31T02:50:59+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Annotated, Any, List, Optional

from pydantic import BaseModel, Field, SecretStr


class CloseTunnelResponse(BaseModel):
    pass


class ResourceNotFoundException(BaseModel):
    __root__: Any


class LimitExceededException(ResourceNotFoundException):
    pass


class TagResourceResponse(CloseTunnelResponse):
    pass


class UntagResourceResponse(CloseTunnelResponse):
    pass


class AmazonResourceName(BaseModel):
    __root__: Annotated[str, Field(max_length=1011, min_length=1)]


class ClientAccessToken(BaseModel):
    __root__: SecretStr


class TunnelId(BaseModel):
    __root__: Annotated[str, Field(regex='[a-zA-Z0-9_\\-+=:]{1,128}')]


class DeleteFlag(BaseModel):
    __root__: bool


class ConnectionStatus(Enum):
    CONNECTED = 'CONNECTED'
    DISCONNECTED = 'DISCONNECTED'


class DateType(BaseModel):
    __root__: datetime


class ConnectionState(BaseModel):
    """
    The state of a connection.
    """

    status: Optional[ConnectionStatus] = None
    lastUpdatedAt: Optional[DateType] = None


class Description(BaseModel):
    __root__: Annotated[str, Field(regex='[^\\p{C}]{1,2048}')]


class ThingName(BaseModel):
    __root__: Annotated[
        str, Field(max_length=128, min_length=1, regex='[a-zA-Z0-9:_-]+')
    ]


class MaxResults(BaseModel):
    __root__: Annotated[int, Field(ge=1.0, le=100.0)]


class NextToken(BaseModel):
    __root__: Annotated[str, Field(regex='[a-zA-Z0-9_=-]{1,4096}')]


class TunnelArn(BaseModel):
    __root__: Annotated[str, Field(max_length=1600, min_length=1)]


class Service(ThingName):
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
    An arbitary key/value pair used to add searchable metadata to secure tunnel resources.
    """

    key: TagKey
    value: TagValue


class TagKeyList(BaseModel):
    __root__: Annotated[List[TagKey], Field(max_items=200, min_items=0)]


class TimeoutInMin(BaseModel):
    __root__: Annotated[int, Field(ge=1.0, le=720.0)]


class TunnelStatus(Enum):
    OPEN = 'OPEN'
    CLOSED = 'CLOSED'


class TunnelSummary(BaseModel):
    """
    Information about the tunnel.
    """

    tunnelId: Optional[TunnelId] = None
    tunnelArn: Optional[TunnelArn] = None
    status: Optional[TunnelStatus] = None
    description: Optional[Description] = None
    createdAt: Optional[DateType] = None
    lastUpdatedAt: Optional[DateType] = None


class CloseTunnelRequest(BaseModel):
    tunnelId: TunnelId
    delete: Optional[DeleteFlag] = None


class DescribeTunnelRequest(BaseModel):
    tunnelId: TunnelId


class ListTagsForResourceRequest(BaseModel):
    resourceArn: AmazonResourceName


class ListTunnelsRequest(BaseModel):
    thingName: Optional[ThingName] = None
    maxResults: Optional[MaxResults] = None
    nextToken: Optional[NextToken] = None


class OpenTunnelResponse(BaseModel):
    tunnelId: Optional[TunnelId] = None
    tunnelArn: Optional[TunnelArn] = None
    sourceAccessToken: Optional[ClientAccessToken] = None
    destinationAccessToken: Optional[ClientAccessToken] = None


class UntagResourceRequest(BaseModel):
    resourceArn: AmazonResourceName
    tagKeys: TagKeyList


class ServiceList(BaseModel):
    __root__: Annotated[List[Service], Field(min_items=1)]


class DestinationConfig(BaseModel):
    """
    The destination configuration.
    """

    thingName: Optional[ThingName] = None
    services: ServiceList


class TagList(BaseModel):
    __root__: Annotated[List[Tag], Field(max_items=200, min_items=1)]


class TunnelSummaryList(BaseModel):
    __root__: List[TunnelSummary]


class TimeoutConfig(BaseModel):
    """
    Tunnel timeout configuration.
    """

    maxLifetimeTimeoutMinutes: Optional[TimeoutInMin] = None


class ListTagsForResourceResponse(BaseModel):
    tags: Optional[TagList] = None


class ListTunnelsResponse(BaseModel):
    tunnelSummaries: Optional[TunnelSummaryList] = None
    nextToken: Optional[NextToken] = None


class OpenTunnelRequest(BaseModel):
    description: Optional[Description] = None
    tags: Optional[TagList] = None
    destinationConfig: Optional[DestinationConfig] = None
    timeoutConfig: Optional[TimeoutConfig] = None


class TagResourceRequest(BaseModel):
    resourceArn: AmazonResourceName
    tags: TagList


class Tunnel(BaseModel):
    """
    A connection between a source computer and a destination device.
    """

    tunnelId: Optional[TunnelId] = None
    tunnelArn: Optional[TunnelArn] = None
    status: Optional[TunnelStatus] = None
    sourceConnectionState: Optional[ConnectionState] = None
    destinationConnectionState: Optional[ConnectionState] = None
    description: Optional[Description] = None
    destinationConfig: Optional[DestinationConfig] = None
    timeoutConfig: Optional[TimeoutConfig] = None
    tags: Optional[TagList] = None
    createdAt: Optional[DateType] = None
    lastUpdatedAt: Optional[DateType] = None


class DescribeTunnelResponse(BaseModel):
    tunnel: Optional[Tunnel] = None
