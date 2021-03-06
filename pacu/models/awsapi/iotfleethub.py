# generated by datamodel-codegen:
#   filename:  openapi.yaml
#   timestamp: 2021-12-31T02:50:58+00:00

from __future__ import annotations

from enum import Enum
from typing import Annotated, Any, List, Optional

from pydantic import BaseModel, Extra, Field


class TagValue(BaseModel):
    __root__: Annotated[str, Field(max_length=256, min_length=1)]


class InvalidRequestException(BaseModel):
    __root__: Any


class InternalFailureException(InvalidRequestException):
    pass


class ThrottlingException(InvalidRequestException):
    pass


class LimitExceededException(InvalidRequestException):
    pass


class DeleteApplicationResponse(BaseModel):
    pass


class ResourceNotFoundException(InvalidRequestException):
    pass


class TagResourceResponse(DeleteApplicationResponse):
    pass


class UntagResourceResponse(DeleteApplicationResponse):
    pass


class TagKey(BaseModel):
    __root__: Annotated[
        str,
        Field(
            max_length=128, min_length=1, regex='^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-@]*)$'
        ),
    ]


class UpdateApplicationResponse(DeleteApplicationResponse):
    pass


class ConflictException(InvalidRequestException):
    pass


class ApplicationState(Enum):
    CREATING = 'CREATING'
    DELETING = 'DELETING'
    ACTIVE = 'ACTIVE'
    CREATE_FAILED = 'CREATE_FAILED'
    DELETE_FAILED = 'DELETE_FAILED'


class Id(BaseModel):
    __root__: Annotated[
        str,
        Field(
            max_length=36,
            min_length=36,
            regex='^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$',
        ),
    ]


class Name(BaseModel):
    __root__: Annotated[str, Field(max_length=100, min_length=1, regex='^[ -~]*$')]


class Description(BaseModel):
    __root__: Annotated[str, Field(max_length=2048, min_length=1, regex='^[ -~]*$')]


class Url(BaseModel):
    __root__: Annotated[
        str, Field(max_length=256, min_length=1, regex='^https\\://\\S+$')
    ]


class Timestamp(BaseModel):
    __root__: int


class Arn(BaseModel):
    __root__: Annotated[str, Field(max_length=1600, min_length=1, regex='^arn:[!-~]+$')]


class ClientRequestToken(BaseModel):
    __root__: Annotated[
        str, Field(max_length=64, min_length=1, regex='^[a-zA-Z0-9-_]+$')
    ]


class TagMap(BaseModel):
    pass

    class Config:
        extra = Extra.allow


class CreateApplicationRequest(BaseModel):
    applicationName: Name
    applicationDescription: Optional[Description] = None
    clientToken: Optional[ClientRequestToken] = None
    roleArn: Arn
    tags: Optional[TagMap] = None


class DeleteApplicationRequest(BaseModel):
    pass


class DescribeApplicationRequest(BaseModel):
    pass


class SsoClientId(BaseModel):
    __root__: str


class ErrorMessage(SsoClientId):
    pass


class NextToken(BaseModel):
    __root__: Annotated[
        str, Field(max_length=2048, min_length=1, regex='^[A-Za-z0-9+/=]+$')
    ]


class ListApplicationsRequest(BaseModel):
    pass


class ResourceArn(SsoClientId):
    pass


class ListTagsForResourceRequest(BaseModel):
    pass


class TagKeyList(BaseModel):
    __root__: List[TagKey]


class TagResourceRequest(BaseModel):
    tags: TagMap


class UntagResourceRequest(BaseModel):
    pass


class UpdateApplicationRequest(BaseModel):
    applicationName: Optional[Name] = None
    applicationDescription: Optional[Description] = None
    clientToken: Optional[ClientRequestToken] = None


class CreateApplicationResponse(BaseModel):
    applicationId: Id
    applicationArn: Arn


class DescribeApplicationResponse(BaseModel):
    applicationId: Id
    applicationArn: Arn
    applicationName: Name
    applicationDescription: Optional[Description] = None
    applicationUrl: Url
    applicationState: ApplicationState
    applicationCreationDate: Timestamp
    applicationLastUpdateDate: Timestamp
    roleArn: Arn
    ssoClientId: Optional[SsoClientId] = None
    errorMessage: Optional[ErrorMessage] = None
    tags: Optional[TagMap] = None


class ListTagsForResourceResponse(BaseModel):
    tags: Optional[TagMap] = None


class ApplicationSummary(BaseModel):
    """
    <p>A summary of information about a AWS IoT Device Management web application.</p> <note> <p>Fleet Hub for AWS IoT Device Management is in public preview and is subject to change.</p> </note>
    """

    applicationId: Id
    applicationName: Name
    applicationDescription: Optional[Description] = None
    applicationUrl: Url
    applicationCreationDate: Optional[Timestamp] = None
    applicationLastUpdateDate: Optional[Timestamp] = None
    applicationState: Optional[ApplicationState] = None


class ApplicationSummaries(BaseModel):
    __root__: List[ApplicationSummary]


class ListApplicationsResponse(BaseModel):
    applicationSummaries: Optional[ApplicationSummaries] = None
    nextToken: Optional[NextToken] = None
