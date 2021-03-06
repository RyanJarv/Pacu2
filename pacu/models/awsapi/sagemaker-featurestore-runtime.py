# generated by datamodel-codegen:
#   filename:  openapi.yaml
#   timestamp: 2021-12-31T02:57:48+00:00

from __future__ import annotations

from typing import Annotated, Any, List, Optional

from pydantic import BaseModel, Field


class ValidationError(BaseModel):
    __root__: Any


class InternalFailure(ValidationError):
    pass


class ServiceUnavailable(ValidationError):
    pass


class AccessForbidden(ValidationError):
    pass


class FeatureName(BaseModel):
    __root__: Annotated[
        str, Field(max_length=64, min_length=1, regex='^[a-zA-Z0-9]([-_]*[a-zA-Z0-9])*')
    ]


class ResourceNotFound(ValidationError):
    pass


class ValueAsString(BaseModel):
    __root__: Annotated[str, Field(max_length=358400, regex='.*')]


class Message(BaseModel):
    __root__: Annotated[str, Field(max_length=2048)]


class BatchGetRecordError(BaseModel):
    """
    The error that has occurred when attempting to retrieve a batch of Records.
    """

    FeatureGroupName: ValueAsString
    RecordIdentifierValueAsString: ValueAsString
    ErrorCode: ValueAsString
    ErrorMessage: Message


class BatchGetRecordErrors(BaseModel):
    __root__: Annotated[List[BatchGetRecordError], Field(min_items=0)]


class FeatureGroupName(BaseModel):
    __root__: Annotated[
        str, Field(max_length=64, min_length=1, regex='^[a-zA-Z0-9](-*[a-zA-Z0-9])*')
    ]


class RecordIdentifiers(BaseModel):
    __root__: Annotated[List[ValueAsString], Field(max_items=100, min_items=1)]


class FeatureNames(BaseModel):
    __root__: Annotated[List[FeatureName], Field(min_items=1)]


class DeleteRecordRequest(BaseModel):
    pass


class GetRecordRequest(BaseModel):
    pass


class BatchGetRecordIdentifier(BaseModel):
    """
    The identifier that identifies the batch of Records you are retrieving in a batch.
    """

    FeatureGroupName: FeatureGroupName
    RecordIdentifiersValueAsString: RecordIdentifiers
    FeatureNames: Optional[FeatureNames] = None


class FeatureValue(BaseModel):
    """
    The value associated with a feature.
    """

    FeatureName: FeatureName
    ValueAsString: ValueAsString


class BatchGetRecordIdentifiers(BaseModel):
    __root__: Annotated[
        List[BatchGetRecordIdentifier], Field(max_items=10, min_items=1)
    ]


class BatchGetRecordRequest(BaseModel):
    Identifiers: BatchGetRecordIdentifiers


class UnprocessedIdentifiers(BaseModel):
    __root__: Annotated[List[BatchGetRecordIdentifier], Field(min_items=0)]


class Record(BaseModel):
    __root__: Annotated[List[FeatureValue], Field(min_items=1)]


class BatchGetRecordResultDetail(BaseModel):
    """
    The output of Records that have been retrieved in a batch.
    """

    FeatureGroupName: ValueAsString
    RecordIdentifierValueAsString: ValueAsString
    Record: Record


class PutRecordRequest(BaseModel):
    Record: Record


class GetRecordResponse(BaseModel):
    Record: Optional[Record] = None


class BatchGetRecordResultDetails(BaseModel):
    __root__: Annotated[List[BatchGetRecordResultDetail], Field(min_items=0)]


class BatchGetRecordResponse(BaseModel):
    Records: BatchGetRecordResultDetails
    Errors: BatchGetRecordErrors
    UnprocessedIdentifiers: UnprocessedIdentifiers
