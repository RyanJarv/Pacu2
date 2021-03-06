# generated by datamodel-codegen:
#   filename:  openapi.yaml
#   timestamp: 2021-12-31T02:53:48+00:00

from __future__ import annotations

from typing import Annotated, Any, List, Optional

from pydantic import BaseModel, Extra, Field, SecretStr


class ItemID(BaseModel):
    __root__: Annotated[str, Field(max_length=256)]


class AttributeValue(BaseModel):
    __root__: Annotated[SecretStr, Field(max_length=1000)]


class FilterAttributeValue(AttributeValue):
    pass


class InvalidInputException(BaseModel):
    __root__: Any


class ResourceNotFoundException(InvalidInputException):
    pass


class Arn(BaseModel):
    __root__: Annotated[
        str, Field(max_length=256, regex='arn:([a-z\\d-]+):personalize:.*:.*:.+')
    ]


class AttributeName(BaseModel):
    __root__: Annotated[str, Field(max_length=150, regex='[A-Za-z\\d_]+')]


class Context(BaseModel):
    pass

    class Config:
        extra = Extra.allow


class FilterAttributeName(BaseModel):
    __root__: Annotated[str, Field(max_length=50, regex='[A-Za-z0-9_]+')]


class FilterValues(BaseModel):
    pass

    class Config:
        extra = Extra.allow


class InputList(BaseModel):
    __root__: List[ItemID]


class UserID(ItemID):
    pass


class GetPersonalizedRankingRequest(BaseModel):
    campaignArn: Arn
    inputList: InputList
    userId: UserID
    context: Optional[Context] = None
    filterArn: Optional[Arn] = None
    filterValues: Optional[FilterValues] = None


class RecommendationID(BaseModel):
    __root__: str


class NumResults(BaseModel):
    __root__: Annotated[int, Field(ge=0.0)]


class GetRecommendationsRequest(BaseModel):
    campaignArn: Arn
    itemId: Optional[ItemID] = None
    userId: Optional[UserID] = None
    numResults: Optional[NumResults] = None
    context: Optional[Context] = None
    filterArn: Optional[Arn] = None
    filterValues: Optional[FilterValues] = None


class Score(BaseModel):
    __root__: float


class PredictedItem(BaseModel):
    """
    <p>An object that identifies an item.</p> <p>The and APIs return a list of <code>PredictedItem</code>s.</p>
    """

    itemId: Optional[ItemID] = None
    score: Optional[Score] = None


class ItemList(BaseModel):
    __root__: List[PredictedItem]


class GetPersonalizedRankingResponse(BaseModel):
    personalizedRanking: Optional[ItemList] = None
    recommendationId: Optional[RecommendationID] = None


class GetRecommendationsResponse(BaseModel):
    itemList: Optional[ItemList] = None
    recommendationId: Optional[RecommendationID] = None
