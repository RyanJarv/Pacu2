# generated by datamodel-codegen:
#   filename:  openapi.yaml
#   timestamp: 2021-12-31T02:54:05+00:00

from __future__ import annotations

from enum import Enum
from typing import Annotated, Any, List, Optional

from pydantic import BaseModel, Field


class InternalErrorException(BaseModel):
    __root__: Any


class InvalidParameterException(InternalErrorException):
    pass


class NotFoundException(InternalErrorException):
    pass


class InvalidNextTokenException(InternalErrorException):
    pass


class ExpiredNextTokenException(InternalErrorException):
    pass


class String(BaseModel):
    __root__: str


class AttributeNameList(BaseModel):
    __root__: List[String]


class AttributeValue(BaseModel):
    """
    The values of a given attribute, such as <code>Throughput Optimized HDD</code> or <code>Provisioned IOPS</code> for the <code>Amazon EC2</code> <code>volumeType</code> attribute.
    """

    Value: Optional[String] = None


class AttributeValueList(BaseModel):
    __root__: List[AttributeValue]


class BoxedInteger(BaseModel):
    __root__: Annotated[int, Field(ge=1.0, le=100.0)]


class FilterType(Enum):
    TERM_MATCH = 'TERM_MATCH'


class Filter(BaseModel):
    """
    The constraints that you want all returned products to match.
    """

    Type: FilterType
    Field: String
    Value: String


class Filters(BaseModel):
    __root__: List[Filter]


class PriceListItemJSON(String):
    pass


class Service(BaseModel):
    """
    The metadata for a service, such as the service code and available attribute names.
    """

    ServiceCode: Optional[String] = None
    AttributeNames: Optional[AttributeNameList] = None


class DescribeServicesRequest(BaseModel):
    ServiceCode: Optional[String] = None
    FormatVersion: Optional[String] = None
    NextToken: Optional[String] = None
    MaxResults: Optional[BoxedInteger] = None


class GetAttributeValuesResponse(BaseModel):
    AttributeValues: Optional[AttributeValueList] = None
    NextToken: Optional[String] = None


class GetAttributeValuesRequest(BaseModel):
    ServiceCode: String
    AttributeName: String
    NextToken: Optional[String] = None
    MaxResults: Optional[BoxedInteger] = None


class GetProductsRequest(BaseModel):
    ServiceCode: Optional[String] = None
    Filters: Optional[Filters] = None
    FormatVersion: Optional[String] = None
    NextToken: Optional[String] = None
    MaxResults: Optional[BoxedInteger] = None


class ServiceList(BaseModel):
    __root__: List[Service]


class PriceList(BaseModel):
    __root__: List[PriceListItemJSON]


class DescribeServicesResponse(BaseModel):
    Services: Optional[ServiceList] = None
    FormatVersion: Optional[String] = None
    NextToken: Optional[String] = None


class GetProductsResponse(BaseModel):
    FormatVersion: Optional[String] = None
    PriceList: Optional[PriceList] = None
    NextToken: Optional[String] = None