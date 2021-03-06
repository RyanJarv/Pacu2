# generated by datamodel-codegen:
#   filename:  openapi.yaml
#   timestamp: 2021-12-31T02:51:21+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Annotated, Any, Optional

from pydantic import BaseModel, Field


class StartSelectorType(Enum):
    FRAGMENT_NUMBER = 'FRAGMENT_NUMBER'
    SERVER_TIMESTAMP = 'SERVER_TIMESTAMP'
    PRODUCER_TIMESTAMP = 'PRODUCER_TIMESTAMP'
    NOW = 'NOW'
    EARLIEST = 'EARLIEST'
    CONTINUATION_TOKEN = 'CONTINUATION_TOKEN'


class FragmentNumberString(BaseModel):
    __root__: Annotated[str, Field(max_length=128, min_length=1, regex='^[0-9]+$')]


class Timestamp(BaseModel):
    __root__: datetime


class ContinuationToken(BaseModel):
    __root__: Annotated[
        str, Field(max_length=128, min_length=1, regex='^[a-zA-Z0-9_\\.\\-]+$')
    ]


class ResourceNotFoundException(BaseModel):
    __root__: Any


class NotAuthorizedException(ResourceNotFoundException):
    pass


class InvalidEndpointException(ResourceNotFoundException):
    pass


class ClientLimitExceededException(ResourceNotFoundException):
    pass


class ConnectionLimitExceededException(ResourceNotFoundException):
    pass


class InvalidArgumentException(ResourceNotFoundException):
    pass


class ContentType(ContinuationToken):
    pass


class StreamName(BaseModel):
    __root__: Annotated[
        str, Field(max_length=256, min_length=1, regex='[a-zA-Z0-9_.-]+')
    ]


class ResourceARN(BaseModel):
    __root__: Annotated[
        str,
        Field(
            max_length=1024,
            min_length=1,
            regex='arn:aws:kinesisvideo:[a-z0-9-]+:[0-9]+:[a-z]+/[a-zA-Z0-9_.-]+/[0-9]+',
        ),
    ]


class StartSelector(BaseModel):
    """
    <p>Identifies the chunk on the Kinesis video stream where you want the <code>GetMedia</code> API to start returning media data. You have the following options to identify the starting chunk: </p> <ul> <li> <p>Choose the latest (or oldest) chunk.</p> </li> <li> <p>Identify a specific chunk. You can identify a specific chunk either by providing a fragment number or timestamp (server or producer). </p> </li> <li> <p>Each chunk's metadata includes a continuation token as a Matroska (MKV) tag (<code>AWS_KINESISVIDEO_CONTINUATION_TOKEN</code>). If your previous <code>GetMedia</code> request terminated, you can use this tag value in your next <code>GetMedia</code> request. The API then starts returning chunks starting where the last API ended.</p> </li> </ul>
    """

    StartSelectorType: StartSelectorType
    AfterFragmentNumber: Optional[FragmentNumberString] = None
    StartTimestamp: Optional[Timestamp] = None
    ContinuationToken: Optional[ContinuationToken] = None


class GetMediaInput(BaseModel):
    StreamName: Optional[StreamName] = None
    StreamARN: Optional[ResourceARN] = None
    StartSelector: StartSelector


class Payload(BaseModel):
    __root__: str


class GetMediaOutput(BaseModel):
    Payload: Optional[Payload] = None
