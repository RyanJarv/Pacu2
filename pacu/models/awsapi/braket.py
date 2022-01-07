# generated by datamodel-codegen:
#   filename:  openapi.yaml
#   timestamp: 2021-12-31T02:45:36+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Annotated, Any, List, Optional

from pydantic import BaseModel, Extra, Field


class ResourceNotFoundException(BaseModel):
    __root__: Any


class AccessDeniedException(ResourceNotFoundException):
    pass


class ConflictException(ResourceNotFoundException):
    pass


class ThrottlingException(ResourceNotFoundException):
    pass


class InternalServiceException(ResourceNotFoundException):
    pass


class ValidationException(ResourceNotFoundException):
    pass


class String(BaseModel):
    __root__: str


class DeviceOfflineException(ResourceNotFoundException):
    pass


class ServiceQuotaExceededException(ResourceNotFoundException):
    pass


class DeviceRetiredException(ResourceNotFoundException):
    pass


class TagResourceResponse(BaseModel):
    pass


class UntagResourceResponse(TagResourceResponse):
    pass


class String64(BaseModel):
    __root__: Annotated[str, Field(max_length=64, min_length=1)]


class QuantumTaskArn(BaseModel):
    __root__: Annotated[str, Field(max_length=256, min_length=1)]


class CancelQuantumTaskRequest(BaseModel):
    clientToken: String64


class CancellationStatus(Enum):
    CANCELLING = 'CANCELLING'
    CANCELLED = 'CANCELLED'


class JsonValue(String):
    pass


class DeviceArn(QuantumTaskArn):
    pass


class CreateQuantumTaskRequestDeviceParametersString(BaseModel):
    __root__: Annotated[str, Field(max_length=48000, min_length=1)]


class CreateQuantumTaskRequestOutputS3BucketString(BaseModel):
    __root__: Annotated[str, Field(max_length=63, min_length=3)]


class CreateQuantumTaskRequestOutputS3KeyPrefixString(BaseModel):
    __root__: Annotated[str, Field(max_length=1024, min_length=1)]


class CreateQuantumTaskRequestShotsLong(BaseModel):
    __root__: Annotated[int, Field(ge=0.0)]


class TagsMap(BaseModel):
    pass

    class Config:
        extra = Extra.allow


class CreateQuantumTaskRequest(BaseModel):
    action: JsonValue
    clientToken: String64
    deviceArn: DeviceArn
    deviceParameters: Optional[CreateQuantumTaskRequestDeviceParametersString] = None
    outputS3Bucket: CreateQuantumTaskRequestOutputS3BucketString
    outputS3KeyPrefix: CreateQuantumTaskRequestOutputS3KeyPrefixString
    shots: CreateQuantumTaskRequestShotsLong
    tags: Optional[TagsMap] = None


class DeviceStatus(Enum):
    ONLINE = 'ONLINE'
    OFFLINE = 'OFFLINE'
    RETIRED = 'RETIRED'


class DeviceType(Enum):
    QPU = 'QPU'
    SIMULATOR = 'SIMULATOR'


class DeviceSummary(BaseModel):
    """
    Includes information about the device.
    """

    deviceArn: DeviceArn
    deviceName: String
    deviceStatus: DeviceStatus
    deviceType: DeviceType
    providerName: String


class DeviceSummaryList(BaseModel):
    __root__: List[DeviceSummary]


class GetDeviceRequest(BaseModel):
    pass


class GetQuantumTaskRequest(BaseModel):
    pass


class SyntheticTimestampDateTime(BaseModel):
    __root__: datetime


class Long(BaseModel):
    __root__: int


class QuantumTaskStatus(Enum):
    CREATED = 'CREATED'
    QUEUED = 'QUEUED'
    RUNNING = 'RUNNING'
    COMPLETED = 'COMPLETED'
    FAILED = 'FAILED'
    CANCELLING = 'CANCELLING'
    CANCELLED = 'CANCELLED'


class ListTagsForResourceRequest(BaseModel):
    pass


class QuantumTaskSummary(BaseModel):
    """
    Includes information about a quantum task.
    """

    createdAt: SyntheticTimestampDateTime
    deviceArn: DeviceArn
    endedAt: Optional[SyntheticTimestampDateTime] = None
    outputS3Bucket: String
    outputS3Directory: String
    quantumTaskArn: QuantumTaskArn
    shots: Long
    status: QuantumTaskStatus
    tags: Optional[TagsMap] = None


class QuantumTaskSummaryList(BaseModel):
    __root__: List[QuantumTaskSummary]


class SearchDevicesFilterNameString(String64):
    pass


class String256(QuantumTaskArn):
    pass


class SearchDevicesRequestMaxResultsInteger(BaseModel):
    __root__: Annotated[int, Field(ge=1.0, le=100.0)]


class SearchQuantumTasksFilterOperator(Enum):
    LT = 'LT'
    LTE = 'LTE'
    EQUAL = 'EQUAL'
    GT = 'GT'
    GTE = 'GTE'
    BETWEEN = 'BETWEEN'


class SearchQuantumTasksFilterValuesList(BaseModel):
    __root__: Annotated[List[String256], Field(max_items=10, min_items=1)]


class SearchQuantumTasksRequestMaxResultsInteger(SearchDevicesRequestMaxResultsInteger):
    pass


class TagKeys(BaseModel):
    __root__: List[String]


class TagResourceRequest(BaseModel):
    tags: TagsMap


class UntagResourceRequest(BaseModel):
    pass


class CancelQuantumTaskResponse(BaseModel):
    cancellationStatus: CancellationStatus
    quantumTaskArn: QuantumTaskArn


class CreateQuantumTaskResponse(BaseModel):
    quantumTaskArn: QuantumTaskArn


class GetDeviceResponse(BaseModel):
    deviceArn: DeviceArn
    deviceCapabilities: JsonValue
    deviceName: String
    deviceStatus: DeviceStatus
    deviceType: DeviceType
    providerName: String


class GetQuantumTaskResponse(BaseModel):
    createdAt: SyntheticTimestampDateTime
    deviceArn: DeviceArn
    deviceParameters: JsonValue
    endedAt: Optional[SyntheticTimestampDateTime] = None
    failureReason: Optional[String] = None
    outputS3Bucket: String
    outputS3Directory: String
    quantumTaskArn: QuantumTaskArn
    shots: Long
    status: QuantumTaskStatus
    tags: Optional[TagsMap] = None


class ListTagsForResourceResponse(BaseModel):
    tags: Optional[TagsMap] = None


class SearchDevicesResponse(BaseModel):
    devices: DeviceSummaryList
    nextToken: Optional[String] = None


class SearchQuantumTasksResponse(BaseModel):
    nextToken: Optional[String] = None
    quantumTasks: QuantumTaskSummaryList


class SearchQuantumTasksFilter(BaseModel):
    """
    A filter to use to search for tasks.
    """

    name: String64
    operator: SearchQuantumTasksFilterOperator
    values: SearchQuantumTasksFilterValuesList


class SearchDevicesFilterValuesList(SearchQuantumTasksFilterValuesList):
    pass


class SearchQuantumTasksRequestFiltersList(BaseModel):
    __root__: Annotated[
        List[SearchQuantumTasksFilter], Field(max_items=10, min_items=0)
    ]


class SearchQuantumTasksRequest(BaseModel):
    filters: SearchQuantumTasksRequestFiltersList
    maxResults: Optional[SearchQuantumTasksRequestMaxResultsInteger] = None
    nextToken: Optional[String] = None


class SearchDevicesFilter(BaseModel):
    """
    The filter to use for searching devices.
    """

    name: SearchDevicesFilterNameString
    values: SearchDevicesFilterValuesList


class SearchDevicesRequestFiltersList(BaseModel):
    __root__: Annotated[List[SearchDevicesFilter], Field(max_items=10, min_items=0)]


class SearchDevicesRequest(BaseModel):
    filters: SearchDevicesRequestFiltersList
    maxResults: Optional[SearchDevicesRequestMaxResultsInteger] = None
    nextToken: Optional[String] = None