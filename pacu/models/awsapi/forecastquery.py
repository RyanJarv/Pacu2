# generated by datamodel-codegen:
#   filename:  openapi.yaml
#   timestamp: 2021-12-31T02:49:40+00:00

from __future__ import annotations

from typing import Annotated, Any, List, Optional

from pydantic import BaseModel, Extra, Field


class ResourceNotFoundException(BaseModel):
    __root__: Any


class ResourceInUseException(ResourceNotFoundException):
    pass


class InvalidInputException(ResourceNotFoundException):
    pass


class LimitExceededException(ResourceNotFoundException):
    pass


class InvalidNextTokenException(ResourceNotFoundException):
    pass


class Arn(BaseModel):
    __root__: Annotated[
        str, Field(max_length=256, regex='arn:([a-z\\d-]+):forecast:.*:.*:.+')
    ]


class AttributeName(BaseModel):
    __root__: Annotated[str, Field(max_length=256, regex='^[a-zA-Z0-9\\_\\-]+$')]


class AttributeValue(BaseModel):
    __root__: Annotated[str, Field(max_length=256)]


class Timestamp(BaseModel):
    __root__: str


class Double(BaseModel):
    __root__: float


class DataPoint(BaseModel):
    """
    The forecast value for a specific date. Part of the <a>Forecast</a> object.
    """

    Timestamp: Optional[Timestamp] = None
    Value: Optional[Double] = None


class DateTime(Timestamp):
    pass


class Filters(BaseModel):
    pass

    class Config:
        extra = Extra.allow


class Predictions(BaseModel):
    pass

    class Config:
        extra = Extra.allow


class Forecast(BaseModel):
    """
    Provides information about a forecast. Returned as part of the <a>QueryForecast</a> response.
    """

    Predictions: Optional[Predictions] = None


class NextToken(BaseModel):
    __root__: Annotated[str, Field(max_length=3000, min_length=1)]


class TimeSeries(BaseModel):
    __root__: List[DataPoint]


class Statistic(BaseModel):
    __root__: Annotated[str, Field(max_length=4)]


class QueryForecastResponse(BaseModel):
    Forecast: Optional[Forecast] = None


class QueryForecastRequest(BaseModel):
    ForecastArn: Arn
    StartDate: Optional[DateTime] = None
    EndDate: Optional[DateTime] = None
    Filters: Filters
    NextToken: Optional[NextToken] = None