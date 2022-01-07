# generated by datamodel-codegen:
#   filename:  openapi.yaml
#   timestamp: 2021-12-31T02:58:17+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Annotated, Any, List, Optional

from pydantic import BaseModel, Extra, Field


class ResourceNotFoundException(BaseModel):
    __root__: Any


class ValidationException(ResourceNotFoundException):
    pass


class InternalServerException(ResourceNotFoundException):
    pass


class ServiceQuotaExceededException(ResourceNotFoundException):
    pass


class ConflictException(ResourceNotFoundException):
    pass


class TagValue(BaseModel):
    __root__: Annotated[
        str, Field(max_length=256, regex='[\\p{L}\\p{Z}\\p{N}_.:/=+\\-@]*')
    ]


class TagResourceResponse(BaseModel):
    pass


class UntagResourceResponse(TagResourceResponse):
    pass


class TagKey(BaseModel):
    __root__: Annotated[
        str, Field(max_length=128, min_length=1, regex='(?!aws:)[a-zA-Z+-=._:/]+')
    ]


class ApplicationId(BaseModel):
    __root__: Annotated[str, Field(max_length=26, min_length=26, regex='[a-z0-9]+')]


class ApplicationArn(BaseModel):
    __root__: Annotated[
        str,
        Field(
            regex='arn:aws[-a-z]*:servicecatalog:[a-z]{2}(-gov)?-[a-z]+-\\d:\\d{12}:/applications/[a-z0-9]+'
        ),
    ]


class Name(BaseModel):
    __root__: Annotated[str, Field(max_length=256, min_length=1, regex='[-.\\w]+')]


class Description(BaseModel):
    __root__: Annotated[str, Field(max_length=1024)]


class Timestamp(BaseModel):
    __root__: datetime


class Tags(BaseModel):
    pass

    class Config:
        extra = Extra.allow


class Application(BaseModel):
    """
    Represents a Amazon Web Services Service Catalog AppRegistry application that is the top-level node in a hierarchy of related cloud resource abstractions.
    """

    id: Optional[ApplicationId] = None
    arn: Optional[ApplicationArn] = None
    name: Optional[Name] = None
    description: Optional[Description] = None
    creationTime: Optional[Timestamp] = None
    lastUpdateTime: Optional[Timestamp] = None
    tags: Optional[Tags] = None


class ApplicationSpecifier(Name):
    pass


class ApplicationSummary(BaseModel):
    """
    Summary of a Amazon Web Services Service Catalog AppRegistry application.
    """

    id: Optional[ApplicationId] = None
    arn: Optional[ApplicationArn] = None
    name: Optional[Name] = None
    description: Optional[Description] = None
    creationTime: Optional[Timestamp] = None
    lastUpdateTime: Optional[Timestamp] = None


class ApplicationSummaries(BaseModel):
    __root__: List[ApplicationSummary]


class Arn(BaseModel):
    __root__: Annotated[
        str,
        Field(
            max_length=1600,
            min_length=1,
            regex='arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\\-])+:([a-z]{2}(-gov)?-[a-z]+-\\d{1})?:(\\d{12})?:(.*)',
        ),
    ]


class AttributeGroupSpecifier(Name):
    pass


class AssociateAttributeGroupRequest(BaseModel):
    pass


class AttributeGroupArn(BaseModel):
    __root__: Annotated[
        str,
        Field(
            regex='arn:aws[-a-z]*:servicecatalog:[a-z]{2}(-gov)?-[a-z]+-\\d:\\d{12}:/attribute-groups/[a-z0-9]+'
        ),
    ]


class ResourceType(Enum):
    CFN_STACK = 'CFN_STACK'


class ResourceSpecifier(BaseModel):
    __root__: Annotated[str, Field(max_length=256, min_length=1, regex='\\S+')]


class AssociateResourceRequest(BaseModel):
    pass


class AssociationCount(BaseModel):
    __root__: Annotated[int, Field(ge=0.0)]


class AttributeGroupId(ApplicationId):
    pass


class AttributeGroup(BaseModel):
    """
    Represents a Amazon Web Services Service Catalog AppRegistry attribute group that is rich metadata which describes an application and its components.
    """

    id: Optional[AttributeGroupId] = None
    arn: Optional[AttributeGroupArn] = None
    name: Optional[Name] = None
    description: Optional[Description] = None
    creationTime: Optional[Timestamp] = None
    lastUpdateTime: Optional[Timestamp] = None
    tags: Optional[Tags] = None


class AttributeGroupIds(BaseModel):
    __root__: List[AttributeGroupId]


class AttributeGroupSummary(BaseModel):
    """
    Summary of a Amazon Web Services Service Catalog AppRegistry attribute group.
    """

    id: Optional[AttributeGroupId] = None
    arn: Optional[AttributeGroupArn] = None
    name: Optional[Name] = None
    description: Optional[Description] = None
    creationTime: Optional[Timestamp] = None
    lastUpdateTime: Optional[Timestamp] = None


class AttributeGroupSummaries(BaseModel):
    __root__: List[AttributeGroupSummary]


class Attributes(BaseModel):
    __root__: Annotated[
        str,
        Field(
            max_length=8000,
            min_length=1,
            regex='[\\u0009\\u000A\\u000D\\u0020-\\u00FF]+',
        ),
    ]


class ClientToken(BaseModel):
    __root__: Annotated[
        str, Field(max_length=128, min_length=1, regex='[a-zA-Z0-9][a-zA-Z0-9_-]*')
    ]


class CreateApplicationRequest(BaseModel):
    name: Name
    description: Optional[Description] = None
    tags: Optional[Tags] = None
    clientToken: ClientToken


class CreateAttributeGroupRequest(BaseModel):
    name: Name
    description: Optional[Description] = None
    attributes: Attributes
    tags: Optional[Tags] = None
    clientToken: ClientToken


class DeleteApplicationRequest(BaseModel):
    pass


class DeleteAttributeGroupRequest(BaseModel):
    pass


class DisassociateAttributeGroupRequest(BaseModel):
    pass


class DisassociateResourceRequest(BaseModel):
    pass


class GetApplicationRequest(BaseModel):
    pass


class GetAssociatedResourceRequest(BaseModel):
    pass


class GetAttributeGroupRequest(BaseModel):
    pass


class NextToken(BaseModel):
    __root__: Annotated[
        str, Field(max_length=2024, min_length=1, regex='[A-Za-z0-9+/=]+')
    ]


class MaxResults(BaseModel):
    __root__: Annotated[int, Field(ge=1.0, le=25.0)]


class ListApplicationsRequest(BaseModel):
    pass


class ListAssociatedAttributeGroupsRequest(BaseModel):
    pass


class ListAssociatedResourcesRequest(BaseModel):
    pass


class ListAttributeGroupsRequest(BaseModel):
    pass


class ListTagsForResourceRequest(BaseModel):
    pass


class StackArn(BaseModel):
    __root__: Annotated[
        str,
        Field(
            regex='arn:aws[-a-z]*:cloudformation:[a-z]{2}(-gov)?-[a-z]+-\\d:\\d{12}:stack/[a-zA-Z][-A-Za-z0-9]{0,127}/[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}'
        ),
    ]


class ResourceGroupState(Enum):
    CREATING = 'CREATING'
    CREATE_COMPLETE = 'CREATE_COMPLETE'
    CREATE_FAILED = 'CREATE_FAILED'
    UPDATING = 'UPDATING'
    UPDATE_COMPLETE = 'UPDATE_COMPLETE'
    UPDATE_FAILED = 'UPDATE_FAILED'


class String(BaseModel):
    __root__: str


class ResourceInfo(BaseModel):
    """
    The information about the resource.
    """

    name: Optional[ResourceSpecifier] = None
    arn: Optional[StackArn] = None


class SyncAction(Enum):
    START_SYNC = 'START_SYNC'
    NO_ACTION = 'NO_ACTION'


class SyncResourceRequest(BaseModel):
    pass


class TagKeys(BaseModel):
    __root__: Annotated[List[TagKey], Field(max_items=50, min_items=0)]


class TagResourceRequest(BaseModel):
    tags: Tags


class UntagResourceRequest(BaseModel):
    pass


class UpdateApplicationRequest(BaseModel):
    name: Optional[Name] = None
    description: Optional[Description] = None


class UpdateAttributeGroupRequest(BaseModel):
    name: Optional[Name] = None
    description: Optional[Description] = None
    attributes: Optional[Attributes] = None


class AssociateAttributeGroupResponse(BaseModel):
    applicationArn: Optional[ApplicationArn] = None
    attributeGroupArn: Optional[AttributeGroupArn] = None


class AssociateResourceResponse(BaseModel):
    applicationArn: Optional[ApplicationArn] = None
    resourceArn: Optional[Arn] = None


class CreateApplicationResponse(BaseModel):
    application: Optional[Application] = None


class CreateAttributeGroupResponse(BaseModel):
    attributeGroup: Optional[AttributeGroup] = None


class DeleteApplicationResponse(BaseModel):
    application: Optional[ApplicationSummary] = None


class DeleteAttributeGroupResponse(BaseModel):
    attributeGroup: Optional[AttributeGroupSummary] = None


class DisassociateAttributeGroupResponse(AssociateAttributeGroupResponse):
    pass


class DisassociateResourceResponse(AssociateResourceResponse):
    pass


class GetAttributeGroupResponse(BaseModel):
    id: Optional[AttributeGroupId] = None
    arn: Optional[AttributeGroupArn] = None
    name: Optional[Name] = None
    description: Optional[Description] = None
    attributes: Optional[Attributes] = None
    creationTime: Optional[Timestamp] = None
    lastUpdateTime: Optional[Timestamp] = None
    tags: Optional[Tags] = None


class ListApplicationsResponse(BaseModel):
    applications: Optional[ApplicationSummaries] = None
    nextToken: Optional[NextToken] = None


class ListAssociatedAttributeGroupsResponse(BaseModel):
    attributeGroups: Optional[AttributeGroupIds] = None
    nextToken: Optional[NextToken] = None


class ListAttributeGroupsResponse(BaseModel):
    attributeGroups: Optional[AttributeGroupSummaries] = None
    nextToken: Optional[NextToken] = None


class ListTagsForResourceResponse(BaseModel):
    tags: Optional[Tags] = None


class SyncResourceResponse(BaseModel):
    applicationArn: Optional[ApplicationArn] = None
    resourceArn: Optional[Arn] = None
    actionTaken: Optional[SyncAction] = None


class UpdateApplicationResponse(CreateApplicationResponse):
    pass


class UpdateAttributeGroupResponse(CreateAttributeGroupResponse):
    pass


class ResourceGroup(BaseModel):
    """
    The information about the resource group integration.
    """

    state: Optional[ResourceGroupState] = None
    arn: Optional[Arn] = None
    errorMessage: Optional[String] = None


class Resources(BaseModel):
    __root__: List[ResourceInfo]


class ResourceIntegrations(BaseModel):
    """
    The service integration information about the resource.
    """

    resourceGroup: Optional[ResourceGroup] = None


class ListAssociatedResourcesResponse(BaseModel):
    resources: Optional[Resources] = None
    nextToken: Optional[NextToken] = None


class Integrations(ResourceIntegrations):
    """
    The information about the service integration.
    """

    pass


class Resource(BaseModel):
    """
    The information about the resource.
    """

    name: Optional[ResourceSpecifier] = None
    arn: Optional[StackArn] = None
    associationTime: Optional[Timestamp] = None
    integrations: Optional[ResourceIntegrations] = None


class GetApplicationResponse(BaseModel):
    id: Optional[ApplicationId] = None
    arn: Optional[ApplicationArn] = None
    name: Optional[Name] = None
    description: Optional[Description] = None
    creationTime: Optional[Timestamp] = None
    lastUpdateTime: Optional[Timestamp] = None
    associatedResourceCount: Optional[AssociationCount] = None
    tags: Optional[Tags] = None
    integrations: Optional[Integrations] = None


class GetAssociatedResourceResponse(BaseModel):
    resource: Optional[Resource] = None