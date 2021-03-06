# generated by datamodel-codegen:
#   filename:  openapi.yaml
#   timestamp: 2021-12-31T02:50:52+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Annotated, Any, List, Optional

from pydantic import BaseModel, Extra, Field


class SuiteDefinitionName(BaseModel):
    __root__: Annotated[str, Field(max_length=256, min_length=1)]


class IntendedForQualificationBoolean(BaseModel):
    __root__: bool


class RootGroup(BaseModel):
    __root__: Annotated[str, Field(max_length=2048, min_length=1)]


class AmazonResourceName(BaseModel):
    __root__: Annotated[str, Field(max_length=2048, min_length=20)]


class String256(SuiteDefinitionName):
    pass


class ValidationException(BaseModel):
    __root__: Any


class InternalServerException(ValidationException):
    pass


class DeleteSuiteDefinitionResponse(BaseModel):
    pass


class ResourceNotFoundException(ValidationException):
    pass


class DeviceUnderTest(BaseModel):
    """
    Lists all the devices under test
    """

    thingArn: Optional[AmazonResourceName] = None
    certificateArn: Optional[AmazonResourceName] = None


class ConflictException(ValidationException):
    pass


class StopSuiteRunResponse(DeleteSuiteDefinitionResponse):
    pass


class TagResourceResponse(DeleteSuiteDefinitionResponse):
    pass


class UntagResourceResponse(DeleteSuiteDefinitionResponse):
    pass


class String128(BaseModel):
    __root__: Annotated[str, Field(max_length=128, min_length=1)]


class TagMap(BaseModel):
    pass

    class Config:
        extra = Extra.allow


class UUID(BaseModel):
    __root__: Annotated[str, Field(max_length=36, min_length=12)]


class Timestamp(BaseModel):
    __root__: datetime


class DeleteSuiteDefinitionRequest(BaseModel):
    pass


class ErrorReason(BaseModel):
    __root__: str


class Failure(ErrorReason):
    pass


class SuiteDefinitionVersion(BaseModel):
    __root__: Annotated[str, Field(max_length=255, min_length=2)]


class GetSuiteDefinitionRequest(BaseModel):
    pass


class GetSuiteRunReportRequest(BaseModel):
    pass


class QualificationReportDownloadUrl(ErrorReason):
    pass


class GetSuiteRunRequest(BaseModel):
    pass


class SuiteRunStatus(Enum):
    PASS = 'PASS'
    FAIL = 'FAIL'
    CANCELED = 'CANCELED'
    PENDING = 'PENDING'
    RUNNING = 'RUNNING'
    STOPPING = 'STOPPING'
    STOPPED = 'STOPPED'
    PASS_WITH_WARNINGS = 'PASS_WITH_WARNINGS'
    ERROR = 'ERROR'


class GroupName(ErrorReason):
    pass


class MaxResults(BaseModel):
    __root__: Annotated[int, Field(ge=1.0, le=50.0)]


class Token(BaseModel):
    __root__: Annotated[str, Field(max_length=2000)]


class ListSuiteDefinitionsRequest(BaseModel):
    pass


class ListSuiteRunsRequest(BaseModel):
    pass


class ListTagsForResourceRequest(BaseModel):
    pass


class LogUrl(ErrorReason):
    pass


class StopSuiteRunRequest(BaseModel):
    pass


class SuiteRunResultCount(BaseModel):
    __root__: Annotated[int, Field(ge=0.0, le=500.0)]


class SuiteRunInformation(BaseModel):
    """
    Information about the suite run.
    """

    suiteDefinitionId: Optional[UUID] = None
    suiteDefinitionVersion: Optional[SuiteDefinitionVersion] = None
    suiteDefinitionName: Optional[SuiteDefinitionName] = None
    suiteRunId: Optional[UUID] = None
    createdAt: Optional[Timestamp] = None
    startedAt: Optional[Timestamp] = None
    endAt: Optional[Timestamp] = None
    status: Optional[SuiteRunStatus] = None
    passed: Optional[SuiteRunResultCount] = None
    failed: Optional[SuiteRunResultCount] = None


class TagKeyList(BaseModel):
    __root__: Annotated[List[String128], Field(max_items=50, min_items=0)]


class TagResourceRequest(BaseModel):
    tags: TagMap


class TestCaseDefinitionName(ErrorReason):
    pass


class Warnings(ErrorReason):
    pass


class TestCaseRun(BaseModel):
    """
    Provides test case run.
    """

    testCaseRunId: Optional[UUID] = None
    testCaseDefinitionId: Optional[UUID] = None
    testCaseDefinitionName: Optional[TestCaseDefinitionName] = None
    status: Optional[SuiteRunStatus] = None
    startTime: Optional[Timestamp] = None
    endTime: Optional[Timestamp] = None
    logUrl: Optional[LogUrl] = None
    warnings: Optional[Warnings] = None
    failure: Optional[Failure] = None


class UntagResourceRequest(BaseModel):
    pass


class CreateSuiteDefinitionResponse(BaseModel):
    suiteDefinitionId: Optional[UUID] = None
    suiteDefinitionArn: Optional[AmazonResourceName] = None
    suiteDefinitionName: Optional[SuiteDefinitionName] = None
    createdAt: Optional[Timestamp] = None


class DeviceUnderTestList(BaseModel):
    __root__: Annotated[List[DeviceUnderTest], Field(max_items=2, min_items=0)]


class GetSuiteRunReportResponse(BaseModel):
    qualificationReportDownloadUrl: Optional[QualificationReportDownloadUrl] = None


class ListTagsForResourceResponse(BaseModel):
    tags: Optional[TagMap] = None


class StartSuiteRunResponse(BaseModel):
    suiteRunId: Optional[UUID] = None
    suiteRunArn: Optional[AmazonResourceName] = None
    createdAt: Optional[Timestamp] = None


class SelectedTestList(BaseModel):
    __root__: Annotated[List[UUID], Field(max_items=100, min_items=0)]


class UpdateSuiteDefinitionResponse(BaseModel):
    suiteDefinitionId: Optional[UUID] = None
    suiteDefinitionArn: Optional[AmazonResourceName] = None
    suiteDefinitionName: Optional[SuiteDefinitionName] = None
    suiteDefinitionVersion: Optional[SuiteDefinitionVersion] = None
    createdAt: Optional[Timestamp] = None
    lastUpdatedAt: Optional[Timestamp] = None


class SuiteDefinitionConfiguration(BaseModel):
    """
    Gets Suite Definition Configuration.
    """

    suiteDefinitionName: Optional[SuiteDefinitionName] = None
    devices: Optional[DeviceUnderTestList] = None
    intendedForQualification: Optional[IntendedForQualificationBoolean] = None
    rootGroup: Optional[RootGroup] = None
    devicePermissionRoleArn: Optional[AmazonResourceName] = None


class CreateSuiteDefinitionRequest(BaseModel):
    suiteDefinitionConfiguration: Optional[SuiteDefinitionConfiguration] = None
    tags: Optional[TagMap] = None


class SuiteRunConfiguration(BaseModel):
    """
    Gets suite run configuration.
    """

    primaryDevice: Optional[DeviceUnderTest] = None
    selectedTestList: Optional[SelectedTestList] = None


class TestCaseRuns(BaseModel):
    """
    Tests under each group result.
    """

    __root__: Annotated[
        List[TestCaseRun], Field(description='Tests under each group result.')
    ]


class GroupResult(BaseModel):
    """
    Show Group Result.
    """

    groupId: Optional[UUID] = None
    groupName: Optional[GroupName] = None
    tests: Optional[TestCaseRuns] = None


class GroupResultList(BaseModel):
    """
    Group Result list.
    """

    __root__: Annotated[List[GroupResult], Field(description='Group Result list.')]


class SuiteRunsList(BaseModel):
    __root__: List[SuiteRunInformation]


class StartSuiteRunRequest(BaseModel):
    suiteDefinitionVersion: Optional[SuiteDefinitionVersion] = None
    suiteRunConfiguration: Optional[SuiteRunConfiguration] = None
    tags: Optional[TagMap] = None


class SuiteDefinitionInformation(BaseModel):
    """
    Information about the suite definition.
    """

    suiteDefinitionId: Optional[UUID] = None
    suiteDefinitionName: Optional[SuiteDefinitionName] = None
    defaultDevices: Optional[DeviceUnderTestList] = None
    intendedForQualification: Optional[IntendedForQualificationBoolean] = None
    createdAt: Optional[Timestamp] = None


class UpdateSuiteDefinitionRequest(BaseModel):
    suiteDefinitionConfiguration: Optional[SuiteDefinitionConfiguration] = None


class GetSuiteDefinitionResponse(BaseModel):
    suiteDefinitionId: Optional[UUID] = None
    suiteDefinitionArn: Optional[AmazonResourceName] = None
    suiteDefinitionVersion: Optional[SuiteDefinitionVersion] = None
    latestVersion: Optional[SuiteDefinitionVersion] = None
    suiteDefinitionConfiguration: Optional[SuiteDefinitionConfiguration] = None
    createdAt: Optional[Timestamp] = None
    lastModifiedAt: Optional[Timestamp] = None
    tags: Optional[TagMap] = None


class ListSuiteRunsResponse(BaseModel):
    suiteRunsList: Optional[SuiteRunsList] = None
    nextToken: Optional[Token] = None


class TestResult(BaseModel):
    """
    Show each group result.
    """

    groups: Optional[GroupResultList] = None


class SuiteDefinitionInformationList(BaseModel):
    __root__: List[SuiteDefinitionInformation]


class GetSuiteRunResponse(BaseModel):
    suiteDefinitionId: Optional[UUID] = None
    suiteDefinitionVersion: Optional[SuiteDefinitionVersion] = None
    suiteRunId: Optional[UUID] = None
    suiteRunArn: Optional[AmazonResourceName] = None
    suiteRunConfiguration: Optional[SuiteRunConfiguration] = None
    testResult: Optional[TestResult] = None
    startTime: Optional[Timestamp] = None
    endTime: Optional[Timestamp] = None
    status: Optional[SuiteRunStatus] = None
    errorReason: Optional[ErrorReason] = None
    tags: Optional[TagMap] = None


class ListSuiteDefinitionsResponse(BaseModel):
    suiteDefinitionInformationList: Optional[SuiteDefinitionInformationList] = None
    nextToken: Optional[Token] = None
