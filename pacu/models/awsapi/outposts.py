# generated by datamodel-codegen:
#   filename:  openapi.yaml
#   timestamp: 2021-12-31T02:53:43+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Annotated, Any, List, Optional

from pydantic import BaseModel, Extra, Field


class ValidationException(BaseModel):
    __root__: Any


class ConflictException(ValidationException):
    pass


class AccessDeniedException(ValidationException):
    pass


class NotFoundException(ValidationException):
    pass


class InternalServerException(ValidationException):
    pass


class ServiceQuotaExceededException(ValidationException):
    pass


class TagValue(BaseModel):
    __root__: Annotated[str, Field(max_length=256, regex='^[\\S \\n]+$')]


class DeleteOutpostOutput(BaseModel):
    pass


class DeleteSiteOutput(DeleteOutpostOutput):
    pass


class LifeCycleStatus(BaseModel):
    __root__: Annotated[
        str,
        Field(
            description='The life cycle status.',
            max_length=20,
            min_length=1,
            regex='^[ A-Za-z]+$',
        ),
    ]


class AvailabilityZone(BaseModel):
    __root__: Annotated[
        str,
        Field(
            description='The Availability Zone.',
            max_length=1000,
            min_length=1,
            regex='^([a-zA-Z]+-){1,3}([a-zA-Z]+)?(\\d+[a-zA-Z]?)?$',
        ),
    ]


class AvailabilityZoneId(BaseModel):
    __root__: Annotated[
        str,
        Field(
            description='The ID of the Availability Zone.',
            max_length=255,
            min_length=1,
            regex='^[a-zA-Z]+\\d-[a-zA-Z]+\\d$',
        ),
    ]


class TagResourceResponse(DeleteOutpostOutput):
    pass


class UntagResourceResponse(DeleteOutpostOutput):
    pass


class TagKey(BaseModel):
    __root__: Annotated[
        str, Field(max_length=128, min_length=1, regex='^(?!aws:)[a-zA-Z+-=._:/]+$')
    ]


class AccountId(BaseModel):
    __root__: Annotated[
        str,
        Field(
            description='The ID of the AWS account.',
            max_length=12,
            min_length=12,
            regex='\\d{12}',
        ),
    ]


class Arn(BaseModel):
    __root__: Annotated[
        str,
        Field(
            max_length=1011,
            regex='^(arn:aws([a-z-]+)?:outposts:[a-z\\d-]+:\\d{12}:([a-z\\d-]+)/)[a-z]{2,8}-[a-f0-9]{17}$',
        ),
    ]


class AvailabilityZoneIdList(BaseModel):
    __root__: Annotated[List[AvailabilityZoneId], Field(max_items=5, min_items=1)]


class AvailabilityZoneList(BaseModel):
    __root__: Annotated[List[AvailabilityZone], Field(max_items=5, min_items=1)]


class OutpostIdentifier(BaseModel):
    __root__: Annotated[
        str,
        Field(
            max_length=180,
            min_length=1,
            regex='^(arn:aws([a-z-]+)?:outposts:[a-z\\d-]+:\\d{12}:outpost/)?op-[a-f0-9]{17}$',
        ),
    ]


class PaymentOption(Enum):
    ALL_UPFRONT = 'ALL_UPFRONT'
    NO_UPFRONT = 'NO_UPFRONT'
    PARTIAL_UPFRONT = 'PARTIAL_UPFRONT'


class PaymentTerm(Enum):
    THREE_YEARS = 'THREE_YEARS'


class OutpostName(BaseModel):
    __root__: Annotated[
        str,
        Field(
            description='The name of the Outpost.',
            max_length=255,
            min_length=1,
            regex='^[\\S ]+$',
        ),
    ]


class OutpostDescription(BaseModel):
    __root__: Annotated[
        str,
        Field(
            description='The description of the Outpost.',
            max_length=1000,
            min_length=0,
            regex='^[\\S ]*$',
        ),
    ]


class SiteId(BaseModel):
    __root__: Annotated[
        str,
        Field(
            description='The ID of the site.',
            max_length=255,
            min_length=1,
            regex='^(arn:aws([a-z-]+)?:outposts:[a-z\\d-]+:\\d{12}:site/)?(os-[a-f0-9]{17})$',
        ),
    ]


class TagMap(BaseModel):
    pass

    class Config:
        extra = Extra.allow


class CreateOutpostInput(BaseModel):
    Name: OutpostName
    Description: Optional[OutpostDescription] = None
    SiteId: SiteId
    AvailabilityZone: Optional[AvailabilityZone] = None
    AvailabilityZoneId: Optional[AvailabilityZoneId] = None
    Tags: Optional[TagMap] = None


class OutpostId(OutpostIdentifier):
    pass


class DeleteOutpostInput(BaseModel):
    pass


class DeleteSiteInput(BaseModel):
    pass


class GetOutpostInput(BaseModel):
    pass


class Token(BaseModel):
    __root__: Annotated[
        str,
        Field(
            description='The pagination token.',
            max_length=1005,
            min_length=1,
            regex='^(\\d+)##(\\S+)$',
        ),
    ]


class MaxResults1000(BaseModel):
    __root__: Annotated[
        int, Field(description='The maximum page size.', ge=1.0, le=1000.0)
    ]


class GetOutpostInstanceTypesInput(BaseModel):
    pass


class OutpostArn(BaseModel):
    __root__: Annotated[
        str,
        Field(
            description='The Amazon Resource Name (ARN) of the Outpost.',
            max_length=255,
            min_length=1,
            regex='^arn:aws([a-z-]+)?:outposts:[a-z\\d-]+:\\d{12}:outpost/op-[a-f0-9]{17}$',
        ),
    ]


class ISO8601Timestamp(BaseModel):
    __root__: datetime


class InstanceType(BaseModel):
    __root__: Annotated[str, Field(description='The instance type.')]


class InstanceTypeItem(BaseModel):
    """
    Information about an instance type.
    """

    InstanceType: Optional[InstanceType] = None


class LifeCycleStatusList(BaseModel):
    __root__: Annotated[List[LifeCycleStatus], Field(max_items=5, min_items=1)]


class SkuCode(BaseModel):
    __root__: Annotated[str, Field(max_length=10, min_length=1, regex='OR-[A-Z0-9]{7}')]


class LineItemId(BaseModel):
    __root__: Annotated[str, Field(regex='ooi-[a-f0-9]{17}')]


class LineItemQuantity(BaseModel):
    __root__: Annotated[int, Field(ge=1.0, le=20.0)]


class Status1(BaseModel):
    __root__: Annotated[str, Field(max_length=1000, min_length=1, regex='^[\\S ]+$')]


class LineItem(BaseModel):
    """
    Information about a line item.
    """

    CatalogItemId: Optional[SkuCode] = None
    LineItemId: Optional[LineItemId] = None
    Quantity: Optional[LineItemQuantity] = None
    Status: Optional[Status1] = None


class LineItemListDefinition(BaseModel):
    __root__: List[LineItem]


class ListOutpostsInput(BaseModel):
    pass


class ListSitesInput(BaseModel):
    pass


class ListTagsForResourceRequest(BaseModel):
    pass


class OutpostIdOnly(BaseModel):
    __root__: Annotated[
        str, Field(max_length=20, min_length=1, regex='^op-[a-f0-9]{17}$')
    ]


class OrderId(BaseModel):
    __root__: Annotated[
        str, Field(max_length=20, min_length=1, regex='oo-[a-f0-9]{17}$')
    ]


class OrderStatus(Enum):
    RECEIVED = 'RECEIVED'
    PENDING = 'PENDING'
    PROCESSING = 'PROCESSING'
    INSTALLING = 'INSTALLING'
    FULFILLED = 'FULFILLED'
    CANCELLED = 'CANCELLED'


class OwnerId(BaseModel):
    __root__: Annotated[
        str,
        Field(
            description='The AWS account ID of the Outpost owner.',
            max_length=12,
            min_length=12,
            regex='\\d{12}',
        ),
    ]


class SiteArn(BaseModel):
    __root__: Annotated[
        str,
        Field(
            description='The Amazon Resource Name (ARN) of the site.',
            max_length=255,
            min_length=1,
            regex='^arn:aws([a-z-]+)?:outposts:[a-z\\d-]+:\\d{12}:site/(os-[a-f0-9]{17})$',
        ),
    ]


class SiteName(BaseModel):
    __root__: Annotated[
        str,
        Field(
            description='The name of the site.',
            max_length=1000,
            min_length=1,
            regex='^[\\S ]+$',
        ),
    ]


class SiteDescription(BaseModel):
    __root__: Annotated[
        str,
        Field(
            description='The description of the site.',
            max_length=1001,
            min_length=1,
            regex='^[\\S ]+$',
        ),
    ]


class Site(BaseModel):
    """
    Information about a site.
    """

    SiteId: Optional[SiteId] = None
    AccountId: Optional[AccountId] = None
    Name: Optional[SiteName] = None
    Description: Optional[SiteDescription] = None
    Tags: Optional[TagMap] = None
    SiteArn: Optional[SiteArn] = None


class TagKeyList(BaseModel):
    __root__: Annotated[List[TagKey], Field(max_items=50, min_items=1)]


class TagResourceRequest(BaseModel):
    Tags: TagMap


class UntagResourceRequest(BaseModel):
    pass


class LineItemRequest(BaseModel):
    """
    Information about a line item request.
    """

    CatalogItemId: Optional[SkuCode] = None
    Quantity: Optional[LineItemQuantity] = None


class ListTagsForResourceResponse(BaseModel):
    Tags: Optional[TagMap] = None


class LineItemRequestListDefinition(BaseModel):
    __root__: Annotated[List[LineItemRequest], Field(max_items=20, min_items=1)]


class CreateOrderInput(BaseModel):
    OutpostIdentifier: OutpostIdentifier
    LineItems: LineItemRequestListDefinition
    PaymentOption: PaymentOption
    PaymentTerm: Optional[PaymentTerm] = None


class Order(BaseModel):
    """
    Information about an order.
    """

    OutpostId: Optional[OutpostIdOnly] = None
    OrderId: Optional[OrderId] = None
    Status: Optional[OrderStatus] = None
    LineItems: Optional[LineItemListDefinition] = None
    PaymentOption: Optional[PaymentOption] = None
    OrderSubmissionDate: Optional[ISO8601Timestamp] = None
    OrderFulfilledDate: Optional[ISO8601Timestamp] = None


class Outpost(BaseModel):
    """
    Information about an Outpost.
    """

    OutpostId: Optional[OutpostId] = None
    OwnerId: Optional[OwnerId] = None
    OutpostArn: Optional[OutpostArn] = None
    SiteId: Optional[SiteId] = None
    Name: Optional[OutpostName] = None
    Description: Optional[OutpostDescription] = None
    LifeCycleStatus: Optional[LifeCycleStatus] = None
    AvailabilityZone: Optional[AvailabilityZone] = None
    AvailabilityZoneId: Optional[AvailabilityZoneId] = None
    Tags: Optional[TagMap] = None
    SiteArn: Optional[SiteArn] = None


class InstanceTypeListDefinition(BaseModel):
    """
    Information about the instance types.
    """

    __root__: Annotated[
        List[InstanceTypeItem],
        Field(description='Information about the instance types.'),
    ]


class OutpostListDefinition(BaseModel):
    """
    Information about the Outposts.
    """

    __root__: Annotated[
        List[Outpost], Field(description='Information about the Outposts.')
    ]


class SiteListDefinition(BaseModel):
    """
    Information about the sites.
    """

    __root__: Annotated[List[Site], Field(description='Information about the sites.')]


class CreateOrderOutput(BaseModel):
    Order: Optional[Order] = None


class CreateOutpostOutput(BaseModel):
    Outpost: Optional[Outpost] = None


class GetOutpostOutput(CreateOutpostOutput):
    pass


class GetOutpostInstanceTypesOutput(BaseModel):
    InstanceTypes: Optional[InstanceTypeListDefinition] = None
    NextToken: Optional[Token] = None
    OutpostId: Optional[OutpostId] = None
    OutpostArn: Optional[OutpostArn] = None


class ListOutpostsOutput(BaseModel):
    Outposts: Optional[OutpostListDefinition] = None
    NextToken: Optional[Token] = None


class ListSitesOutput(BaseModel):
    Sites: Optional[SiteListDefinition] = None
    NextToken: Optional[Token] = None
