# generated by datamodel-codegen:
#   filename:  openapi.yaml
#   timestamp: 2021-12-31T02:53:04+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Annotated, Any, List, Optional

from pydantic import BaseModel, Field


class InternalServerError(BaseModel):
    __root__: Any


class ServiceUnavailableException(InternalServerError):
    pass


class AccessDeniedException(InternalServerError):
    pass


class ThrottlingException(InternalServerError):
    pass


class DryRunOperation(InternalServerError):
    pass


class InvalidInputException(InternalServerError):
    pass


class GetHomeRegionRequest(BaseModel):
    pass


class ControlId(BaseModel):
    __root__: Annotated[
        str, Field(max_length=50, min_length=1, regex='^hrc-[a-z0-9]{12}$')
    ]


class HomeRegion(BaseModel):
    __root__: Annotated[
        str, Field(max_length=50, min_length=1, regex='^([a-z]+)-([a-z]+)-([0-9]+)$')
    ]


class DryRun(BaseModel):
    __root__: bool


class DescribeHomeRegionControlsMaxResults(BaseModel):
    __root__: Annotated[int, Field(ge=1.0, le=100.0)]


class Token(BaseModel):
    __root__: Annotated[
        str,
        Field(max_length=2048, min_length=0, regex='^[a-zA-Z0-9\\/\\+\\=]{0,2048}$'),
    ]


class RequestedTime(BaseModel):
    __root__: datetime


class TargetType(Enum):
    ACCOUNT = 'ACCOUNT'


class TargetId(BaseModel):
    __root__: Annotated[str, Field(max_length=12, min_length=12, regex='^\\d{12}$')]


class GetHomeRegionResult(BaseModel):
    HomeRegion: Optional[HomeRegion] = None


class Target(BaseModel):
    """
    The target parameter specifies the identifier to which the home region is applied, which is always an <code>ACCOUNT</code>. It applies the home region to the current <code>ACCOUNT</code>.
    """

    Type: TargetType
    Id: Optional[TargetId] = None


class HomeRegionControl(BaseModel):
    """
    A home region control is an object that specifies the home region for an account, with some additional information. It contains a target (always of type <code>ACCOUNT</code>), an ID, and a time at which the home region was set.
    """

    ControlId: Optional[ControlId] = None
    HomeRegion: Optional[HomeRegion] = None
    Target: Optional[Target] = None
    RequestedTime: Optional[RequestedTime] = None


class HomeRegionControls(BaseModel):
    __root__: Annotated[List[HomeRegionControl], Field(max_items=100)]


class CreateHomeRegionControlResult(BaseModel):
    HomeRegionControl: Optional[HomeRegionControl] = None


class CreateHomeRegionControlRequest(BaseModel):
    HomeRegion: HomeRegion
    Target: Target
    DryRun: Optional[DryRun] = None


class DescribeHomeRegionControlsResult(BaseModel):
    HomeRegionControls: Optional[HomeRegionControls] = None
    NextToken: Optional[Token] = None


class DescribeHomeRegionControlsRequest(BaseModel):
    ControlId: Optional[ControlId] = None
    HomeRegion: Optional[HomeRegion] = None
    Target: Optional[Target] = None
    MaxResults: Optional[DescribeHomeRegionControlsMaxResults] = None
    NextToken: Optional[Token] = None
