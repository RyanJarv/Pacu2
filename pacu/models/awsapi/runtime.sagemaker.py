# generated by datamodel-codegen:
#   filename:  openapi.yaml
#   timestamp: 2021-12-31T02:57:19+00:00

from __future__ import annotations

from typing import Annotated, Any, Optional

from pydantic import BaseModel, Field, SecretStr


class InternalFailure(BaseModel):
    __root__: Any


class ServiceUnavailable(InternalFailure):
    pass


class ValidationError(InternalFailure):
    pass


class ModelError(InternalFailure):
    pass


class BodyBlob(BaseModel):
    __root__: Annotated[SecretStr, Field(max_length=6291456)]


class CustomAttributesHeader(BaseModel):
    __root__: Annotated[SecretStr, Field(max_length=1024, regex='\\p{ASCII}*')]


class EndpointName(BaseModel):
    __root__: Annotated[str, Field(max_length=63, regex='^[a-zA-Z0-9](-*[a-zA-Z0-9])*')]


class Header(BaseModel):
    __root__: Annotated[str, Field(max_length=1024, regex='\\p{ASCII}*')]


class InferenceId1(BaseModel):
    __root__: Annotated[
        str, Field(max_length=64, min_length=1, regex='\\A\\S[\\p{Print}]*\\z')
    ]


class InputLocationHeader(BaseModel):
    __root__: Annotated[
        str, Field(max_length=1024, min_length=1, regex='^(https|s3)://([^/]+)/?(.*)$')
    ]


class RequestTTLSecondsHeader(BaseModel):
    __root__: Annotated[int, Field(ge=60.0, le=21600.0)]


class InvokeEndpointAsyncInput(BaseModel):
    pass


class TargetModelHeader(BaseModel):
    __root__: Annotated[
        str, Field(max_length=1024, min_length=1, regex='\\A\\S[\\p{Print}]*\\z')
    ]


class TargetVariantHeader(EndpointName):
    pass


class TargetContainerHostnameHeader(EndpointName):
    pass


class InvokeEndpointInput(BaseModel):
    Body: BodyBlob


class InvokeEndpointOutput(BaseModel):
    Body: BodyBlob


class InvokeEndpointAsyncOutput(BaseModel):
    InferenceId: Optional[Header] = None
