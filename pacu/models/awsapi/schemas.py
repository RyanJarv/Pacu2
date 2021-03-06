# generated by datamodel-codegen:
#   filename:  openapi.yaml
#   timestamp: 2021-12-31T02:57:51+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Annotated, Any, List, Optional

from pydantic import BaseModel, Extra, Field


class _String(BaseModel):
    __root__: str


class BadRequestException(BaseModel):
    __root__: Any


class InternalServerErrorException(BadRequestException):
    pass


class UnauthorizedException(BadRequestException):
    pass


class ForbiddenException(BadRequestException):
    pass


class ServiceUnavailableException(BadRequestException):
    pass


class ConflictException(BadRequestException):
    pass


class NotFoundException(BadRequestException):
    pass


class TooManyRequestsException(BadRequestException):
    pass


class ExportSchemaResponse(BaseModel):
    Content: Optional[_String] = None
    SchemaArn: Optional[_String] = None
    SchemaName: Optional[_String] = None
    SchemaVersion: Optional[_String] = None
    Type: Optional[_String] = None


class GetDiscoveredSchemaResponse(BaseModel):
    Content: Optional[_String] = None


class GetDiscoveredSchemaVersionItemInput(BaseModel):
    __root__: Annotated[str, Field(max_length=100000, min_length=1)]


class GetResourcePolicyResponse(BaseModel):
    Policy: Optional[_String] = None
    RevisionId: Optional[_String] = None


class GoneException(BadRequestException):
    pass


class PutResourcePolicyResponse(GetResourcePolicyResponse):
    pass


class PreconditionFailedException(BadRequestException):
    pass


class CodeGenerationStatus(Enum):
    CREATE_IN_PROGRESS = 'CREATE_IN_PROGRESS'
    CREATE_COMPLETE = 'CREATE_COMPLETE'
    CREATE_FAILED = 'CREATE_FAILED'


class _StringMin0Max256(BaseModel):
    __root__: Annotated[str, Field(max_length=256, min_length=0)]


class _StringMin20Max1600(BaseModel):
    __root__: Annotated[str, Field(max_length=1600, min_length=20)]


class _Boolean(BaseModel):
    __root__: bool


class Tags(BaseModel):
    """
    Key-value pairs associated with a resource.
    """

    pass

    class Config:
        extra = Extra.allow


class CreateDiscovererRequest(BaseModel):
    Description: Optional[_StringMin0Max256] = None
    SourceArn: _StringMin20Max1600
    CrossAccount: Optional[_Boolean] = None
    Tags: Optional[Tags] = None


class DiscovererState(Enum):
    STARTED = 'STARTED'
    STOPPED = 'STOPPED'


class CreateRegistryRequest(BaseModel):
    Description: Optional[_StringMin0Max256] = None
    Tags: Optional[Tags] = None


class _StringMin1Max100000(GetDiscoveredSchemaVersionItemInput):
    pass


class Type3(Enum):
    OpenApi3 = 'OpenApi3'
    JSONSchemaDraft4 = 'JSONSchemaDraft4'


class CreateSchemaRequest(BaseModel):
    Content: _StringMin1Max100000
    Description: Optional[_StringMin0Max256] = None
    Tags: Optional[Tags] = None
    Type: Type3


class _TimestampIso8601(BaseModel):
    __root__: datetime


class DeleteDiscovererRequest(BaseModel):
    pass


class DeleteRegistryRequest(BaseModel):
    pass


class DeleteResourcePolicyRequest(BaseModel):
    pass


class DeleteSchemaRequest(BaseModel):
    pass


class DeleteSchemaVersionRequest(BaseModel):
    pass


class DescribeCodeBindingRequest(BaseModel):
    pass


class DescribeDiscovererRequest(BaseModel):
    pass


class DescribeRegistryRequest(BaseModel):
    pass


class DescribeSchemaRequest(BaseModel):
    pass


class DiscovererSummary(BaseModel):
    DiscovererArn: Optional[_String] = None
    DiscovererId: Optional[_String] = None
    SourceArn: Optional[_String] = None
    State: Optional[DiscovererState] = None
    CrossAccount: Optional[_Boolean] = None
    Tags: Optional[Tags] = None


class ExportSchemaRequest(BaseModel):
    pass


class GetCodeBindingSourceRequest(BaseModel):
    pass


class Body(_String):
    pass


class _ListOfGetDiscoveredSchemaVersionItemInput(BaseModel):
    __root__: Annotated[
        List[GetDiscoveredSchemaVersionItemInput], Field(max_items=10, min_items=1)
    ]


class GetDiscoveredSchemaRequest(BaseModel):
    Events: _ListOfGetDiscoveredSchemaVersionItemInput
    Type: Type3


class GetResourcePolicyRequest(BaseModel):
    pass


class _Integer(BaseModel):
    __root__: int


class ListDiscoverersRequest(BaseModel):
    pass


class _ListOfDiscovererSummary(BaseModel):
    __root__: List[DiscovererSummary]


class ListRegistriesRequest(BaseModel):
    pass


class ListSchemaVersionsRequest(BaseModel):
    pass


class ListSchemasRequest(BaseModel):
    pass


class ListTagsForResourceRequest(BaseModel):
    pass


class PutCodeBindingRequest(BaseModel):
    pass


class PutResourcePolicyRequest(BaseModel):
    """
    The name of the policy.
    """

    Policy: _String
    RevisionId: Optional[_String] = None


class RegistrySummary(BaseModel):
    RegistryArn: Optional[_String] = None
    RegistryName: Optional[_String] = None
    Tags: Optional[Tags] = None


class _Long(_Integer):
    pass


class SchemaSummary(BaseModel):
    """
    A summary of schema details.
    """

    LastModified: Optional[_TimestampIso8601] = None
    SchemaArn: Optional[_String] = None
    SchemaName: Optional[_String] = None
    Tags: Optional[Tags] = None
    VersionCount: Optional[_Long] = None


class SchemaVersionSummary(BaseModel):
    SchemaArn: Optional[_String] = None
    SchemaName: Optional[_String] = None
    SchemaVersion: Optional[_String] = None
    Type: Optional[Type3] = None


class SearchSchemaVersionSummary(BaseModel):
    CreatedDate: Optional[_TimestampIso8601] = None
    SchemaVersion: Optional[_String] = None
    Type: Optional[Type3] = None


class SearchSchemasRequest(BaseModel):
    pass


class StartDiscovererRequest(BaseModel):
    pass


class StopDiscovererRequest(BaseModel):
    pass


class TagResourceRequest(BaseModel):
    Tags: Tags


class _ListOfString(BaseModel):
    __root__: List[_String]


class UntagResourceRequest(BaseModel):
    pass


class UpdateDiscovererRequest(BaseModel):
    Description: Optional[_StringMin0Max256] = None
    CrossAccount: Optional[_Boolean] = None


class UpdateRegistryRequest(BaseModel):
    """
    Updates the registry.
    """

    Description: Optional[_StringMin0Max256] = None


class _StringMin0Max36(BaseModel):
    __root__: Annotated[str, Field(max_length=36, min_length=0)]


class UpdateSchemaRequest(BaseModel):
    ClientTokenId: Optional[_StringMin0Max36] = None
    Content: Optional[_StringMin1Max100000] = None
    Description: Optional[_StringMin0Max256] = None
    Type: Optional[Type3] = None


class CreateDiscovererResponse(BaseModel):
    Description: Optional[_String] = None
    DiscovererArn: Optional[_String] = None
    DiscovererId: Optional[_String] = None
    SourceArn: Optional[_String] = None
    State: Optional[DiscovererState] = None
    CrossAccount: Optional[_Boolean] = None
    Tags: Optional[Tags] = None


class CreateRegistryResponse(BaseModel):
    Description: Optional[_String] = None
    RegistryArn: Optional[_String] = None
    RegistryName: Optional[_String] = None
    Tags: Optional[Tags] = None


class CreateSchemaResponse(BaseModel):
    Description: Optional[_String] = None
    LastModified: Optional[_TimestampIso8601] = None
    SchemaArn: Optional[_String] = None
    SchemaName: Optional[_String] = None
    SchemaVersion: Optional[_String] = None
    Tags: Optional[Tags] = None
    Type: Optional[_String] = None
    VersionCreatedDate: Optional[_TimestampIso8601] = None


class DescribeCodeBindingResponse(BaseModel):
    CreationDate: Optional[_TimestampIso8601] = None
    LastModified: Optional[_TimestampIso8601] = None
    SchemaVersion: Optional[_String] = None
    Status: Optional[CodeGenerationStatus] = None


class DescribeDiscovererResponse(CreateDiscovererResponse):
    pass


class DescribeRegistryResponse(CreateRegistryResponse):
    pass


class DescribeSchemaResponse(BaseModel):
    Content: Optional[_String] = None
    Description: Optional[_String] = None
    LastModified: Optional[_TimestampIso8601] = None
    SchemaArn: Optional[_String] = None
    SchemaName: Optional[_String] = None
    SchemaVersion: Optional[_String] = None
    Tags: Optional[Tags] = None
    Type: Optional[_String] = None
    VersionCreatedDate: Optional[_TimestampIso8601] = None


class GetCodeBindingSourceResponse(BaseModel):
    Body: Optional[Body] = None


class ListDiscoverersResponse(BaseModel):
    Discoverers: Optional[_ListOfDiscovererSummary] = None
    NextToken: Optional[_String] = None


class ListTagsForResourceResponse(BaseModel):
    Tags: Optional[Tags] = None


class PutCodeBindingResponse(DescribeCodeBindingResponse):
    pass


class StartDiscovererResponse(BaseModel):
    DiscovererId: Optional[_String] = None
    State: Optional[DiscovererState] = None


class StopDiscovererResponse(StartDiscovererResponse):
    pass


class UpdateDiscovererResponse(CreateDiscovererResponse):
    pass


class UpdateRegistryResponse(CreateRegistryResponse):
    pass


class UpdateSchemaResponse(CreateSchemaResponse):
    pass


class _ListOfRegistrySummary(BaseModel):
    __root__: List[RegistrySummary]


class _ListOfSchemaVersionSummary(BaseModel):
    __root__: List[SchemaVersionSummary]


class _ListOfSchemaSummary(BaseModel):
    __root__: List[SchemaSummary]


class _ListOfSearchSchemaVersionSummary(BaseModel):
    __root__: List[SearchSchemaVersionSummary]


class SearchSchemaSummary(BaseModel):
    RegistryName: Optional[_String] = None
    SchemaArn: Optional[_String] = None
    SchemaName: Optional[_String] = None
    SchemaVersions: Optional[_ListOfSearchSchemaVersionSummary] = None


class _ListOfSearchSchemaSummary(BaseModel):
    __root__: List[SearchSchemaSummary]


class ListRegistriesResponse(BaseModel):
    NextToken: Optional[_String] = None
    Registries: Optional[_ListOfRegistrySummary] = None


class ListSchemaVersionsResponse(BaseModel):
    NextToken: Optional[_String] = None
    SchemaVersions: Optional[_ListOfSchemaVersionSummary] = None


class ListSchemasResponse(BaseModel):
    NextToken: Optional[_String] = None
    Schemas: Optional[_ListOfSchemaSummary] = None


class SearchSchemasResponse(BaseModel):
    NextToken: Optional[_String] = None
    Schemas: Optional[_ListOfSearchSchemaSummary] = None
