# generated by datamodel-codegen:
#   filename:  openapi.yaml
#   timestamp: 2021-12-31T02:52:10+00:00

from __future__ import annotations

from enum import Enum
from typing import Annotated, Any, List, Optional

from pydantic import BaseModel, Field


class InternalServiceException(BaseModel):
    __root__: Any


class AccessDeniedException(InternalServiceException):
    pass


class ValidationException(InternalServiceException):
    pass


class ResourceNotFoundException(InternalServiceException):
    pass


class ResourceInUseException(InternalServiceException):
    pass


class ThrottlingException(InternalServiceException):
    pass


class ResourceNotSupportedException(InternalServiceException):
    pass


class SortBy(BaseModel):
    __root__: Annotated[str, Field(max_length=255, min_length=1, regex='^[a-zA-Z]+$')]


class SortOrder(Enum):
    ASCENDING = 'ASCENDING'
    DESCENDING = 'DESCENDING'


class ServiceQuotaExceededException(InternalServiceException):
    pass


class ARN(BaseModel):
    __root__: Annotated[
        str, Field(max_length=2048, min_length=1, regex='^[a-zA-Z0-9:*/-]+$')
    ]


class Catalog(BaseModel):
    __root__: Annotated[str, Field(max_length=64, min_length=1, regex='^[a-zA-Z]+$')]


class ResourceId(BaseModel):
    __root__: Annotated[str, Field(max_length=255, min_length=1, regex='^[\\w\\-]+$')]


class CancelChangeSetRequest(BaseModel):
    pass


class ChangeType(BaseModel):
    __root__: Annotated[str, Field(max_length=255, min_length=1, regex='^[A-Z][\\w]*$')]


class Json(BaseModel):
    __root__: Annotated[
        str,
        Field(max_length=16384, min_length=2, regex='^[\\s]*\\{[\\s\\S]*\\}[\\s]*$'),
    ]


class ChangeName(BaseModel):
    __root__: Annotated[str, Field(max_length=72, min_length=1, regex='^[a-zA-Z]$')]


class ChangeSetName(BaseModel):
    __root__: Annotated[
        str, Field(max_length=100, min_length=1, regex='^[\\w\\s+=.:@-]+$')
    ]


class DateTimeISO8601(BaseModel):
    __root__: Annotated[
        str,
        Field(
            max_length=20,
            min_length=20,
            regex='^([\\d]{4})\\-(1[0-2]|0[1-9])\\-(3[01]|0[1-9]|[12][\\d])T(2[0-3]|[01][\\d]):([0-5][\\d]):([0-5][\\d])Z$',
        ),
    ]


class ChangeStatus(Enum):
    PREPARING = 'PREPARING'
    APPLYING = 'APPLYING'
    SUCCEEDED = 'SUCCEEDED'
    CANCELLED = 'CANCELLED'
    FAILED = 'FAILED'


class ResourceIdList(BaseModel):
    __root__: List[ResourceId]


class FailureCode(Enum):
    CLIENT_ERROR = 'CLIENT_ERROR'
    SERVER_FAULT = 'SERVER_FAULT'


class ClientRequestToken(BaseModel):
    __root__: Annotated[str, Field(max_length=36, min_length=1, regex='^[\\w\\-]+$')]


class DescribeChangeSetRequest(BaseModel):
    pass


class ExceptionMessageContent(BaseModel):
    __root__: Annotated[str, Field(max_length=2048, min_length=1, regex='^(.)+$')]


class DescribeEntityRequest(BaseModel):
    pass


class EntityType(SortBy):
    pass


class Identifier(BaseModel):
    __root__: Annotated[str, Field(max_length=255, min_length=1, regex='^[\\w\\-@]+$')]


class EntityNameString(BaseModel):
    __root__: Annotated[
        str, Field(max_length=255, min_length=1, regex='^\\\\S+[\\\\S\\\\s]*')
    ]


class VisibilityValue(Catalog):
    pass


class EntitySummary(BaseModel):
    """
    This object is a container for common summary information about the entity. The summary doesn't contain the whole entity structure, but it does contain information common across all entities.
    """

    Name: Optional[EntityNameString] = None
    EntityType: Optional[EntityType] = None
    EntityId: Optional[ResourceId] = None
    EntityArn: Optional[ARN] = None
    LastModifiedDate: Optional[DateTimeISO8601] = None
    Visibility: Optional[VisibilityValue] = None


class EntitySummaryList(BaseModel):
    __root__: List[EntitySummary]


class ErrorCodeString(BaseModel):
    __root__: Annotated[str, Field(max_length=72, min_length=1, regex='^[a-zA-Z_]+$')]


class ErrorDetail(BaseModel):
    """
    Details about the error.
    """

    ErrorCode: Optional[ErrorCodeString] = None
    ErrorMessage: Optional[ExceptionMessageContent] = None


class FilterName(SortBy):
    pass


class FilterValueContent(BaseModel):
    __root__: Annotated[str, Field(max_length=255, min_length=1, regex='^(.)+$')]


class Sort(BaseModel):
    """
    An object that contains two attributes, <code>SortBy</code> and <code>SortOrder</code>.
    """

    SortBy: Optional[SortBy] = None
    SortOrder: Optional[SortOrder] = None


class MaxResultInteger(BaseModel):
    __root__: Annotated[int, Field(ge=1.0, le=20.0)]


class NextToken(BaseModel):
    __root__: Annotated[
        str, Field(max_length=2048, min_length=1, regex='^[\\w+=.:@\\-\\/]$')
    ]


class CancelChangeSetResponse(BaseModel):
    ChangeSetId: Optional[ResourceId] = None
    ChangeSetArn: Optional[ARN] = None


class DescribeEntityResponse(BaseModel):
    EntityType: Optional[EntityType] = None
    EntityIdentifier: Optional[Identifier] = None
    EntityArn: Optional[ARN] = None
    LastModifiedDate: Optional[DateTimeISO8601] = None
    Details: Optional[Json] = None


class ListEntitiesResponse(BaseModel):
    EntitySummaryList: Optional[EntitySummaryList] = None
    NextToken: Optional[NextToken] = None


class StartChangeSetResponse(CancelChangeSetResponse):
    pass


class Entity(BaseModel):
    """
    An entity contains data that describes your product, its supported features, and how it can be used or launched by your customer.
    """

    Type: EntityType
    Identifier: Optional[Identifier] = None


class ChangeSetSummaryListItem(BaseModel):
    """
    A summary of a change set returned in a list of change sets when the <code>ListChangeSets</code> action is called.
    """

    ChangeSetId: Optional[ResourceId] = None
    ChangeSetArn: Optional[ARN] = None
    ChangeSetName: Optional[ChangeSetName] = None
    StartTime: Optional[DateTimeISO8601] = None
    EndTime: Optional[DateTimeISO8601] = None
    Status: Optional[ChangeStatus] = None
    EntityIdList: Optional[ResourceIdList] = None
    FailureCode: Optional[FailureCode] = None


class ChangeSetSummaryList(BaseModel):
    __root__: List[ChangeSetSummaryListItem]


class ErrorDetailList(BaseModel):
    __root__: List[ErrorDetail]


class ValueList(BaseModel):
    __root__: Annotated[List[FilterValueContent], Field(max_items=10, min_items=1)]


class ListChangeSetsResponse(BaseModel):
    ChangeSetSummaryList: Optional[ChangeSetSummaryList] = None
    NextToken: Optional[NextToken] = None


class Filter(BaseModel):
    """
    A filter object, used to optionally filter results from calls to the <code>ListEntities</code> and <code>ListChangeSets</code> actions.
    """

    Name: Optional[FilterName] = None
    ValueList: Optional[ValueList] = None


class Change(BaseModel):
    """
    An object that contains the <code>ChangeType</code>, <code>Details</code>, and <code>Entity</code>.
    """

    ChangeType: ChangeType
    Entity: Entity
    Details: Json
    ChangeName: Optional[ChangeName] = None


class ChangeSummary(BaseModel):
    """
    This object is a container for common summary information about the change. The summary doesn't contain the whole change structure.
    """

    ChangeType: Optional[ChangeType] = None
    Entity: Optional[Entity] = None
    Details: Optional[Json] = None
    ErrorDetailList: Optional[ErrorDetailList] = None
    ChangeName: Optional[ChangeName] = None


class ChangeSetDescription(BaseModel):
    __root__: List[ChangeSummary]


class FilterList(BaseModel):
    __root__: Annotated[List[Filter], Field(max_items=8, min_items=1)]


class ListChangeSetsRequest(BaseModel):
    Catalog: Catalog
    FilterList: Optional[FilterList] = None
    Sort: Optional[Sort] = None
    MaxResults: Optional[MaxResultInteger] = None
    NextToken: Optional[NextToken] = None


class ListEntitiesRequest(BaseModel):
    Catalog: Catalog
    EntityType: EntityType
    FilterList: Optional[FilterList] = None
    Sort: Optional[Sort] = None
    NextToken: Optional[NextToken] = None
    MaxResults: Optional[MaxResultInteger] = None


class RequestedChangeList(BaseModel):
    __root__: Annotated[List[Change], Field(max_items=20, min_items=1)]


class StartChangeSetRequest(BaseModel):
    Catalog: Catalog
    ChangeSet: RequestedChangeList
    ChangeSetName: Optional[ChangeSetName] = None
    ClientRequestToken: Optional[ClientRequestToken] = None


class DescribeChangeSetResponse(BaseModel):
    ChangeSetId: Optional[ResourceId] = None
    ChangeSetArn: Optional[ARN] = None
    ChangeSetName: Optional[ChangeSetName] = None
    StartTime: Optional[DateTimeISO8601] = None
    EndTime: Optional[DateTimeISO8601] = None
    Status: Optional[ChangeStatus] = None
    FailureCode: Optional[FailureCode] = None
    FailureDescription: Optional[ExceptionMessageContent] = None
    ChangeSet: Optional[ChangeSetDescription] = None
