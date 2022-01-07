# generated by datamodel-codegen:
#   filename:  openapi.yaml
#   timestamp: 2021-12-31T02:45:32+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Annotated, Any, List, Optional

from pydantic import BaseModel, Extra, Field


class BackupPlanName(BaseModel):
    __root__: str


class TagValue(BackupPlanName):
    pass


class LimitExceededException(BaseModel):
    __root__: Any


class AlreadyExistsException(LimitExceededException):
    pass


class InvalidParameterValueException(LimitExceededException):
    pass


class MissingParameterValueException(LimitExceededException):
    pass


class ServiceUnavailableException(LimitExceededException):
    pass


class BackupSelectionName(BaseModel):
    __root__: Annotated[str, Field(regex='^[a-zA-Z0-9\\-\\_\\.]{1,50}$')]


class IAMRoleArn(BackupPlanName):
    pass


class String(BackupPlanName):
    pass


class FormatList(BaseModel):
    __root__: List[String]


class ResourceNotFoundException(LimitExceededException):
    pass


class InvalidRequestException(LimitExceededException):
    pass


class ConflictException(LimitExceededException):
    pass


class InvalidResourceStateException(LimitExceededException):
    pass


class DependencyFailureException(LimitExceededException):
    pass


class ExportBackupPlanTemplateOutput(BaseModel):
    BackupPlanTemplateJson: Optional[String] = None


class BackupVaultEvent(Enum):
    BACKUP_JOB_STARTED = 'BACKUP_JOB_STARTED'
    BACKUP_JOB_COMPLETED = 'BACKUP_JOB_COMPLETED'
    BACKUP_JOB_SUCCESSFUL = 'BACKUP_JOB_SUCCESSFUL'
    BACKUP_JOB_FAILED = 'BACKUP_JOB_FAILED'
    BACKUP_JOB_EXPIRED = 'BACKUP_JOB_EXPIRED'
    RESTORE_JOB_STARTED = 'RESTORE_JOB_STARTED'
    RESTORE_JOB_COMPLETED = 'RESTORE_JOB_COMPLETED'
    RESTORE_JOB_SUCCESSFUL = 'RESTORE_JOB_SUCCESSFUL'
    RESTORE_JOB_FAILED = 'RESTORE_JOB_FAILED'
    COPY_JOB_STARTED = 'COPY_JOB_STARTED'
    COPY_JOB_SUCCESSFUL = 'COPY_JOB_SUCCESSFUL'
    COPY_JOB_FAILED = 'COPY_JOB_FAILED'
    RECOVERY_POINT_MODIFIED = 'RECOVERY_POINT_MODIFIED'
    BACKUP_PLAN_CREATED = 'BACKUP_PLAN_CREATED'
    BACKUP_PLAN_MODIFIED = 'BACKUP_PLAN_MODIFIED'


class Long(BaseModel):
    __root__: int


class BackupOptionValue(BackupSelectionName):
    pass


class MetadataValue(BackupPlanName):
    pass


class GlobalSettingsValue(BackupPlanName):
    pass


class IsEnabled(BaseModel):
    __root__: bool


class ARN(BackupPlanName):
    pass


class AccountId(BaseModel):
    __root__: Annotated[str, Field(regex='^[0-9]{12}$')]


class ResourceType(BackupSelectionName):
    pass


class BackupOptions(BaseModel):
    pass

    class Config:
        extra = Extra.allow


class AdvancedBackupSetting(BaseModel):
    """
    A list of backup options for each resource type.
    """

    ResourceType: Optional[ResourceType] = None
    BackupOptions: Optional[BackupOptions] = None


class BackupVaultName(BaseModel):
    __root__: Annotated[str, Field(regex='^[a-zA-Z0-9\\-\\_]{2,50}$')]


class Timestamp(BaseModel):
    __root__: datetime


class BackupJobState(Enum):
    CREATED = 'CREATED'
    PENDING = 'PENDING'
    RUNNING = 'RUNNING'
    ABORTING = 'ABORTING'
    ABORTED = 'ABORTED'
    COMPLETED = 'COMPLETED'
    FAILED = 'FAILED'
    EXPIRED = 'EXPIRED'


class RecoveryPointCreator(BaseModel):
    """
    Contains information about the backup plan and rule that Backup used to initiate the recovery point backup.
    """

    BackupPlanId: Optional[String] = None
    BackupPlanArn: Optional[ARN] = None
    BackupPlanVersion: Optional[String] = None
    BackupRuleId: Optional[String] = None


class BackupJob(BaseModel):
    """
    Contains detailed information about a backup job.
    """

    AccountId: Optional[AccountId] = None
    BackupJobId: Optional[String] = None
    BackupVaultName: Optional[BackupVaultName] = None
    BackupVaultArn: Optional[ARN] = None
    RecoveryPointArn: Optional[ARN] = None
    ResourceArn: Optional[ARN] = None
    CreationDate: Optional[Timestamp] = None
    CompletionDate: Optional[Timestamp] = None
    State: Optional[BackupJobState] = None
    StatusMessage: Optional[String] = None
    PercentDone: Optional[String] = None
    BackupSizeInBytes: Optional[Long] = None
    IamRoleArn: Optional[IAMRoleArn] = None
    CreatedBy: Optional[RecoveryPointCreator] = None
    ExpectedCompletionDate: Optional[Timestamp] = None
    StartBy: Optional[Timestamp] = None
    ResourceType: Optional[ResourceType] = None
    BytesTransferred: Optional[Long] = None
    BackupOptions: Optional[BackupOptions] = None
    BackupType: Optional[String] = None


class BackupJobsList(BaseModel):
    __root__: List[BackupJob]


class BackupOptionKey(BackupSelectionName):
    pass


class BackupPlanTemplatesListMember(BaseModel):
    """
    An object specifying metadata associated with a backup plan template.
    """

    BackupPlanTemplateId: Optional[String] = None
    BackupPlanTemplateName: Optional[String] = None


class BackupPlanTemplatesList(BaseModel):
    __root__: List[BackupPlanTemplatesListMember]


class BackupRuleName(BackupSelectionName):
    pass


class CronExpression(BackupPlanName):
    pass


class WindowMinutes(Long):
    pass


class Lifecycle(BaseModel):
    """
    <p>Contains an array of <code>Transition</code> objects specifying how long in days before a recovery point transitions to cold storage or is deleted.</p> <p>Backups transitioned to cold storage must be stored in cold storage for a minimum of 90 days. Therefore, on the console, the “expire after days” setting must be 90 days greater than the “transition to cold after days” setting. The “transition to cold after days” setting cannot be changed after a backup has been transitioned to cold.</p> <p>Only Amazon EFS file system backups can be transitioned to cold storage.</p>
    """

    MoveToColdStorageAfterDays: Optional[Long] = None
    DeleteAfterDays: Optional[Long] = None


class Tags(BaseModel):
    pass

    class Config:
        extra = Extra.allow


class Boolean1(IsEnabled):
    pass


class BackupSelectionsListMember(BaseModel):
    """
    Contains metadata about a <code>BackupSelection</code> object.
    """

    SelectionId: Optional[String] = None
    SelectionName: Optional[BackupSelectionName] = None
    BackupPlanId: Optional[String] = None
    CreationDate: Optional[Timestamp] = None
    CreatorRequestId: Optional[String] = None
    IamRoleArn: Optional[IAMRoleArn] = None


class BackupSelectionsList(BaseModel):
    __root__: List[BackupSelectionsListMember]


class BackupVaultEvents(BaseModel):
    __root__: List[BackupVaultEvent]


class LongModel(Long):
    pass


class CalculatedLifecycle(BaseModel):
    """
    <p>Contains <code>DeleteAt</code> and <code>MoveToColdStorageAt</code> timestamps, which are used to specify a lifecycle for a recovery point.</p> <p>The lifecycle defines when a protected resource is transitioned to cold storage and when it expires. Backup transitions and expires backups automatically according to the lifecycle that you define.</p> <p>Backups transitioned to cold storage must be stored in cold storage for a minimum of 90 days. Therefore, the “expire after days” setting must be 90 days greater than the “transition to cold after days” setting. The “transition to cold after days” setting cannot be changed after a backup has been transitioned to cold.</p> <p>Only Amazon EFS file system backups can be transitioned to cold storage.</p>
    """

    MoveToColdStorageAt: Optional[Timestamp] = None
    DeleteAt: Optional[Timestamp] = None


class ComplianceResourceIdList(BaseModel):
    __root__: Annotated[List[String], Field(max_items=100, min_items=1)]


class ConditionType(Enum):
    STRINGEQUALS = 'STRINGEQUALS'


class ConditionKey(BackupPlanName):
    pass


class ConditionValue(BackupPlanName):
    pass


class Condition(BaseModel):
    """
    Contains an array of triplets made up of a condition type (such as <code>StringEquals</code>), a key, and a value. Conditions are used to filter resources in a selection that is assigned to a backup plan.
    """

    ConditionType: ConditionType
    ConditionKey: ConditionKey
    ConditionValue: ConditionValue


class ParameterName(BackupPlanName):
    pass


class ParameterValue(BackupPlanName):
    pass


class ControlInputParameter(BaseModel):
    """
    A list of parameters for a control. A control can have zero, one, or more than one parameter. An example of a control with two parameters is: "backup plan frequency is at least <code>daily</code> and the retention period is at least <code>1 year</code>". The first parameter is <code>daily</code>. The second parameter is <code>1 year</code>.
    """

    ParameterName: Optional[ParameterName] = None
    ParameterValue: Optional[ParameterValue] = None


class ControlInputParameters(BaseModel):
    __root__: List[ControlInputParameter]


class ControlName(BackupPlanName):
    pass


class ResourceTypeList(BaseModel):
    __root__: List[ARN]


class StringMap(BaseModel):
    pass

    class Config:
        extra = Extra.allow


class ControlScope(BaseModel):
    """
    <p>A framework consists of one or more controls. Each control has its own control scope. The control scope defines what the control will evaluate. Three examples of control scopes are: a specific backup plan, all backup plans with a specific tag, or all backup plans.</p> <note> <p>To set a control scope that includes all of a particular resource, leave the <code>ControlScope</code> empty or do not pass it when calling <code>CreateFramework</code>.</p> </note>
    """

    ComplianceResourceIds: Optional[ComplianceResourceIdList] = None
    ComplianceResourceTypes: Optional[ResourceTypeList] = None
    Tags: Optional[StringMap] = None


class CopyAction(BaseModel):
    """
    The details of the copy operation.
    """

    Lifecycle: Optional[Lifecycle] = None
    DestinationBackupVaultArn: ARN


class CopyJobState(Enum):
    CREATED = 'CREATED'
    RUNNING = 'RUNNING'
    COMPLETED = 'COMPLETED'
    FAILED = 'FAILED'


class CopyJob(BaseModel):
    """
    Contains detailed information about a copy job.
    """

    AccountId: Optional[AccountId] = None
    CopyJobId: Optional[String] = None
    SourceBackupVaultArn: Optional[ARN] = None
    SourceRecoveryPointArn: Optional[ARN] = None
    DestinationBackupVaultArn: Optional[ARN] = None
    DestinationRecoveryPointArn: Optional[ARN] = None
    ResourceArn: Optional[ARN] = None
    CreationDate: Optional[Timestamp] = None
    CompletionDate: Optional[Timestamp] = None
    State: Optional[CopyJobState] = None
    StatusMessage: Optional[String] = None
    BackupSizeInBytes: Optional[Long] = None
    IamRoleArn: Optional[IAMRoleArn] = None
    CreatedBy: Optional[RecoveryPointCreator] = None
    ResourceType: Optional[ResourceType] = None


class CopyJobsList(BaseModel):
    __root__: List[CopyJob]


class CreateBackupVaultInput(BaseModel):
    BackupVaultTags: Optional[Tags] = None
    EncryptionKeyArn: Optional[ARN] = None
    CreatorRequestId: Optional[String] = None


class FrameworkName(BaseModel):
    __root__: Annotated[
        str, Field(max_length=256, min_length=1, regex='[a-zA-Z][_a-zA-Z0-9]*')
    ]


class FrameworkDescription(BaseModel):
    __root__: Annotated[str, Field(max_length=1024, min_length=0, regex='.*\\S.*')]


class ReportPlanName(FrameworkName):
    pass


class ReportPlanDescription(FrameworkDescription):
    pass


class ReportDeliveryChannel(BaseModel):
    """
    Contains information from your report plan about where to deliver your reports, specifically your Amazon S3 bucket name, S3 key prefix, and the formats of your reports.
    """

    S3BucketName: String
    S3KeyPrefix: Optional[String] = None
    Formats: Optional[FormatList] = None


class ReportSetting(BaseModel):
    """
    Contains detailed information about a report setting.
    """

    ReportTemplate: String


class CreateReportPlanInput(BaseModel):
    ReportPlanName: ReportPlanName
    ReportPlanDescription: Optional[ReportPlanDescription] = None
    ReportDeliveryChannel: ReportDeliveryChannel
    ReportSetting: ReportSetting
    ReportPlanTags: Optional[StringMap] = None
    IdempotencyToken: Optional[String] = None


class DeleteBackupPlanInput(BaseModel):
    pass


class DeleteBackupSelectionInput(BaseModel):
    pass


class DeleteBackupVaultAccessPolicyInput(BaseModel):
    pass


class DeleteBackupVaultInput(BaseModel):
    pass


class DeleteBackupVaultNotificationsInput(BaseModel):
    pass


class DeleteFrameworkInput(BaseModel):
    pass


class DeleteRecoveryPointInput(BaseModel):
    pass


class DeleteReportPlanInput(BaseModel):
    pass


class DescribeBackupJobInput(BaseModel):
    pass


class DescribeBackupVaultInput(BaseModel):
    pass


class DescribeCopyJobInput(BaseModel):
    pass


class DescribeFrameworkInput(BaseModel):
    pass


class DescribeGlobalSettingsInput(BaseModel):
    pass


class GlobalSettings(BaseModel):
    pass

    class Config:
        extra = Extra.allow


class DescribeProtectedResourceInput(BaseModel):
    pass


class DescribeRecoveryPointInput(BaseModel):
    pass


class RecoveryPointStatus(Enum):
    COMPLETED = 'COMPLETED'
    PARTIAL = 'PARTIAL'
    DELETING = 'DELETING'
    EXPIRED = 'EXPIRED'


class Boolean(IsEnabled):
    pass


class StorageClass(Enum):
    WARM = 'WARM'
    COLD = 'COLD'
    DELETED = 'DELETED'


class DescribeRegionSettingsInput(BaseModel):
    pass


class ResourceTypeOptInPreference(BaseModel):
    pass

    class Config:
        extra = Extra.allow


class ReportJobId(BackupPlanName):
    pass


class DescribeReportJobInput(BaseModel):
    pass


class DescribeReportPlanInput(BaseModel):
    pass


class ReportPlan(BaseModel):
    """
    Contains detailed information about a report plan.
    """

    ReportPlanArn: Optional[ARN] = None
    ReportPlanName: Optional[ReportPlanName] = None
    ReportPlanDescription: Optional[ReportPlanDescription] = None
    ReportSetting: Optional[ReportSetting] = None
    ReportDeliveryChannel: Optional[ReportDeliveryChannel] = None
    DeploymentStatus: Optional[String] = None
    CreationTime: Optional[Timestamp] = None
    LastAttemptedExecutionTime: Optional[Timestamp] = None
    LastSuccessfulExecutionTime: Optional[Timestamp] = None


class RestoreJobId(BackupPlanName):
    pass


class DescribeRestoreJobInput(BaseModel):
    pass


class RestoreJobStatus(Enum):
    PENDING = 'PENDING'
    RUNNING = 'RUNNING'
    COMPLETED = 'COMPLETED'
    ABORTED = 'ABORTED'
    FAILED = 'FAILED'


class DisassociateRecoveryPointInput(BaseModel):
    pass


class ExportBackupPlanTemplateInput(BaseModel):
    pass


class Integer(Long):
    pass


class Framework(BaseModel):
    """
    Contains detailed information about a framework. Frameworks contain controls, which evaluate and report on your backup events and resources. Frameworks generate daily compliance results.
    """

    FrameworkName: Optional[FrameworkName] = None
    FrameworkArn: Optional[ARN] = None
    FrameworkDescription: Optional[FrameworkDescription] = None
    NumberOfControls: Optional[Integer] = None
    CreationTime: Optional[Timestamp] = None
    DeploymentStatus: Optional[String] = None


class FrameworkList(BaseModel):
    __root__: List[Framework]


class GetBackupPlanFromJSONInput(BaseModel):
    BackupPlanTemplateJson: String


class GetBackupPlanFromTemplateInput(BaseModel):
    pass


class GetBackupPlanInput(BaseModel):
    pass


class GetBackupSelectionInput(BaseModel):
    pass


class GetBackupVaultAccessPolicyInput(BaseModel):
    pass


class IAMPolicy(BackupPlanName):
    pass


class GetBackupVaultNotificationsInput(BaseModel):
    pass


class GetRecoveryPointRestoreMetadataInput(BaseModel):
    pass


class Metadata(BaseModel):
    pass

    class Config:
        extra = Extra.allow


class ResourceTypes(BaseModel):
    __root__: List[ResourceType]


class GlobalSettingsName(BackupPlanName):
    pass


class MaxResults(BaseModel):
    __root__: Annotated[int, Field(ge=1.0, le=1000.0)]


class ListBackupJobsInput(BaseModel):
    pass


class ListBackupPlanTemplatesInput(BaseModel):
    pass


class ListBackupPlanVersionsInput(BaseModel):
    pass


class ListBackupPlansInput(BaseModel):
    pass


class ListBackupSelectionsInput(BaseModel):
    pass


class ListBackupVaultsInput(BaseModel):
    pass


class ListCopyJobsInput(BaseModel):
    pass


class MaxFrameworkInputs(MaxResults):
    pass


class ListFrameworksInput(BaseModel):
    pass


class ListProtectedResourcesInput(BaseModel):
    pass


class ListRecoveryPointsByBackupVaultInput(BaseModel):
    pass


class ListRecoveryPointsByResourceInput(BaseModel):
    pass


class ListReportJobsInput(BaseModel):
    pass


class ListReportPlansInput(BaseModel):
    pass


class ReportPlanList(BaseModel):
    __root__: List[ReportPlan]


class ListRestoreJobsInput(BaseModel):
    pass


class ListTagsInput(BaseModel):
    pass


class MetadataKey(BackupPlanName):
    pass


class ProtectedResource(BaseModel):
    """
    A structure that contains information about a backed-up resource.
    """

    ResourceArn: Optional[ARN] = None
    ResourceType: Optional[ResourceType] = None
    LastBackupTime: Optional[Timestamp] = None


class PutBackupVaultAccessPolicyInput(BaseModel):
    Policy: Optional[IAMPolicy] = None


class PutBackupVaultNotificationsInput(BaseModel):
    SNSTopicArn: ARN
    BackupVaultEvents: BackupVaultEvents


class RecoveryPointByBackupVault(BaseModel):
    """
    Contains detailed information about the recovery points stored in a backup vault.
    """

    RecoveryPointArn: Optional[ARN] = None
    BackupVaultName: Optional[BackupVaultName] = None
    BackupVaultArn: Optional[ARN] = None
    SourceBackupVaultArn: Optional[ARN] = None
    ResourceArn: Optional[ARN] = None
    ResourceType: Optional[ResourceType] = None
    CreatedBy: Optional[RecoveryPointCreator] = None
    IamRoleArn: Optional[IAMRoleArn] = None
    Status: Optional[RecoveryPointStatus] = None
    StatusMessage: Optional[String] = None
    CreationDate: Optional[Timestamp] = None
    CompletionDate: Optional[Timestamp] = None
    BackupSizeInBytes: Optional[Long] = None
    CalculatedLifecycle: Optional[CalculatedLifecycle] = None
    Lifecycle: Optional[Lifecycle] = None
    EncryptionKeyArn: Optional[ARN] = None
    IsEncrypted: Optional[Boolean] = None
    LastRestoreTime: Optional[Timestamp] = None


class RecoveryPointByResource(BaseModel):
    """
    Contains detailed information about a saved recovery point.
    """

    RecoveryPointArn: Optional[ARN] = None
    CreationDate: Optional[Timestamp] = None
    Status: Optional[RecoveryPointStatus] = None
    StatusMessage: Optional[String] = None
    EncryptionKeyArn: Optional[ARN] = None
    BackupSizeBytes: Optional[Long] = None
    BackupVaultName: Optional[BackupVaultName] = None


class StringList(FormatList):
    pass


class ReportDestination(BaseModel):
    """
    Contains information from your report job about your report destination.
    """

    S3BucketName: Optional[String] = None
    S3Keys: Optional[StringList] = None


class RestoreJobsListMember(BaseModel):
    """
    Contains metadata about a restore job.
    """

    AccountId: Optional[AccountId] = None
    RestoreJobId: Optional[String] = None
    RecoveryPointArn: Optional[ARN] = None
    CreationDate: Optional[Timestamp] = None
    CompletionDate: Optional[Timestamp] = None
    Status: Optional[RestoreJobStatus] = None
    StatusMessage: Optional[String] = None
    PercentDone: Optional[String] = None
    BackupSizeInBytes: Optional[Long] = None
    IamRoleArn: Optional[IAMRoleArn] = None
    ExpectedCompletionTimeMinutes: Optional[Long] = None
    CreatedResourceArn: Optional[ARN] = None
    ResourceType: Optional[ResourceType] = None


class StartBackupJobInput(BaseModel):
    BackupVaultName: BackupVaultName
    ResourceArn: ARN
    IamRoleArn: IAMRoleArn
    IdempotencyToken: Optional[String] = None
    StartWindowMinutes: Optional[WindowMinutes] = None
    CompleteWindowMinutes: Optional[WindowMinutes] = None
    Lifecycle: Optional[Lifecycle] = None
    RecoveryPointTags: Optional[Tags] = None
    BackupOptions: Optional[BackupOptions] = None


class StartCopyJobInput(BaseModel):
    RecoveryPointArn: ARN
    SourceBackupVaultName: BackupVaultName
    DestinationBackupVaultArn: ARN
    IamRoleArn: IAMRoleArn
    IdempotencyToken: Optional[String] = None
    Lifecycle: Optional[Lifecycle] = None


class StartReportJobInput(BaseModel):
    IdempotencyToken: Optional[String] = None


class StartRestoreJobInput(BaseModel):
    RecoveryPointArn: ARN
    Metadata: Metadata
    IamRoleArn: IAMRoleArn
    IdempotencyToken: Optional[String] = None
    ResourceType: Optional[ResourceType] = None


class StopBackupJobInput(BaseModel):
    pass


class TagKey(BackupPlanName):
    pass


class TagKeyList(FormatList):
    pass


class TagResourceInput(BaseModel):
    Tags: Tags


class UntagResourceInput(BaseModel):
    TagKeyList: TagKeyList


class UpdateGlobalSettingsInput(BaseModel):
    GlobalSettings: Optional[GlobalSettings] = None


class UpdateRecoveryPointLifecycleInput(BaseModel):
    Lifecycle: Optional[Lifecycle] = None


class UpdateRegionSettingsInput(BaseModel):
    ResourceTypeOptInPreference: Optional[ResourceTypeOptInPreference] = None


class UpdateReportPlanInput(BaseModel):
    ReportPlanDescription: Optional[ReportPlanDescription] = None
    ReportDeliveryChannel: Optional[ReportDeliveryChannel] = None
    ReportSetting: Optional[ReportSetting] = None
    IdempotencyToken: Optional[String] = None


class AdvancedBackupSettings(BaseModel):
    __root__: List[AdvancedBackupSetting]


class CreateBackupSelectionOutput(BaseModel):
    SelectionId: Optional[String] = None
    BackupPlanId: Optional[String] = None
    CreationDate: Optional[Timestamp] = None


class ResourceArns(ResourceTypeList):
    pass


class ListOfTags(BaseModel):
    __root__: List[Condition]


class CreateBackupVaultOutput(BaseModel):
    BackupVaultName: Optional[BackupVaultName] = None
    BackupVaultArn: Optional[ARN] = None
    CreationDate: Optional[Timestamp] = None


class CreateFrameworkOutput(BaseModel):
    FrameworkName: Optional[FrameworkName] = None
    FrameworkArn: Optional[ARN] = None


class FrameworkControl(BaseModel):
    """
    Contains detailed information about all of the controls of a framework. Each framework must contain at least one control.
    """

    ControlName: ControlName
    ControlInputParameters: Optional[ControlInputParameters] = None
    ControlScope: Optional[ControlScope] = None


class CreateReportPlanOutput(BaseModel):
    ReportPlanName: Optional[ReportPlanName] = None
    ReportPlanArn: Optional[ARN] = None


class DeleteBackupPlanOutput(BaseModel):
    BackupPlanId: Optional[String] = None
    BackupPlanArn: Optional[ARN] = None
    DeletionDate: Optional[Timestamp] = None
    VersionId: Optional[String] = None


class DescribeBackupJobOutput(BaseModel):
    AccountId: Optional[AccountId] = None
    BackupJobId: Optional[String] = None
    BackupVaultName: Optional[BackupVaultName] = None
    BackupVaultArn: Optional[ARN] = None
    RecoveryPointArn: Optional[ARN] = None
    ResourceArn: Optional[ARN] = None
    CreationDate: Optional[Timestamp] = None
    CompletionDate: Optional[Timestamp] = None
    State: Optional[BackupJobState] = None
    StatusMessage: Optional[String] = None
    PercentDone: Optional[String] = None
    BackupSizeInBytes: Optional[Long] = None
    IamRoleArn: Optional[IAMRoleArn] = None
    CreatedBy: Optional[RecoveryPointCreator] = None
    ResourceType: Optional[ResourceType] = None
    BytesTransferred: Optional[Long] = None
    ExpectedCompletionDate: Optional[Timestamp] = None
    StartBy: Optional[Timestamp] = None
    BackupOptions: Optional[BackupOptions] = None
    BackupType: Optional[String] = None


class DescribeBackupVaultOutput(BaseModel):
    BackupVaultName: Optional[String] = None
    BackupVaultArn: Optional[ARN] = None
    EncryptionKeyArn: Optional[ARN] = None
    CreationDate: Optional[Timestamp] = None
    CreatorRequestId: Optional[String] = None
    NumberOfRecoveryPoints: Optional[LongModel] = None


class DescribeCopyJobOutput(BaseModel):
    CopyJob: Optional[CopyJob] = None


class DescribeGlobalSettingsOutput(BaseModel):
    GlobalSettings: Optional[GlobalSettings] = None
    LastUpdateTime: Optional[Timestamp] = None


class DescribeProtectedResourceOutput(ProtectedResource):
    pass


class DescribeRecoveryPointOutput(BaseModel):
    RecoveryPointArn: Optional[ARN] = None
    BackupVaultName: Optional[BackupVaultName] = None
    BackupVaultArn: Optional[ARN] = None
    SourceBackupVaultArn: Optional[ARN] = None
    ResourceArn: Optional[ARN] = None
    ResourceType: Optional[ResourceType] = None
    CreatedBy: Optional[RecoveryPointCreator] = None
    IamRoleArn: Optional[IAMRoleArn] = None
    Status: Optional[RecoveryPointStatus] = None
    StatusMessage: Optional[String] = None
    CreationDate: Optional[Timestamp] = None
    CompletionDate: Optional[Timestamp] = None
    BackupSizeInBytes: Optional[Long] = None
    CalculatedLifecycle: Optional[CalculatedLifecycle] = None
    Lifecycle: Optional[Lifecycle] = None
    EncryptionKeyArn: Optional[ARN] = None
    IsEncrypted: Optional[Boolean] = None
    StorageClass: Optional[StorageClass] = None
    LastRestoreTime: Optional[Timestamp] = None


class DescribeRegionSettingsOutput(BaseModel):
    ResourceTypeOptInPreference: Optional[ResourceTypeOptInPreference] = None


class DescribeReportPlanOutput(BaseModel):
    ReportPlan: Optional[ReportPlan] = None


class DescribeRestoreJobOutput(RestoreJobsListMember):
    pass


class GetBackupVaultAccessPolicyOutput(BaseModel):
    BackupVaultName: Optional[BackupVaultName] = None
    BackupVaultArn: Optional[ARN] = None
    Policy: Optional[IAMPolicy] = None


class GetBackupVaultNotificationsOutput(BaseModel):
    BackupVaultName: Optional[BackupVaultName] = None
    BackupVaultArn: Optional[ARN] = None
    SNSTopicArn: Optional[ARN] = None
    BackupVaultEvents: Optional[BackupVaultEvents] = None


class GetRecoveryPointRestoreMetadataOutput(BaseModel):
    BackupVaultArn: Optional[ARN] = None
    RecoveryPointArn: Optional[ARN] = None
    RestoreMetadata: Optional[Metadata] = None


class GetSupportedResourceTypesOutput(BaseModel):
    ResourceTypes: Optional[ResourceTypes] = None


class ListBackupJobsOutput(BaseModel):
    BackupJobs: Optional[BackupJobsList] = None
    NextToken: Optional[String] = None


class ListBackupPlanTemplatesOutput(BaseModel):
    NextToken: Optional[String] = None
    BackupPlanTemplatesList: Optional[BackupPlanTemplatesList] = None


class ListBackupSelectionsOutput(BaseModel):
    NextToken: Optional[String] = None
    BackupSelectionsList: Optional[BackupSelectionsList] = None


class ListCopyJobsOutput(BaseModel):
    CopyJobs: Optional[CopyJobsList] = None
    NextToken: Optional[String] = None


class ListFrameworksOutput(BaseModel):
    Frameworks: Optional[FrameworkList] = None
    NextToken: Optional[String] = None


class ListReportPlansOutput(BaseModel):
    ReportPlans: Optional[ReportPlanList] = None
    NextToken: Optional[String] = None


class ListTagsOutput(BaseModel):
    NextToken: Optional[String] = None
    Tags: Optional[Tags] = None


class StartBackupJobOutput(BaseModel):
    BackupJobId: Optional[String] = None
    RecoveryPointArn: Optional[ARN] = None
    CreationDate: Optional[Timestamp] = None


class StartCopyJobOutput(BaseModel):
    CopyJobId: Optional[String] = None
    CreationDate: Optional[Timestamp] = None


class StartReportJobOutput(BaseModel):
    ReportJobId: Optional[ReportJobId] = None


class StartRestoreJobOutput(BaseModel):
    RestoreJobId: Optional[RestoreJobId] = None


class UpdateBackupPlanOutput(BaseModel):
    BackupPlanId: Optional[String] = None
    BackupPlanArn: Optional[ARN] = None
    CreationDate: Optional[Timestamp] = None
    VersionId: Optional[String] = None
    AdvancedBackupSettings: Optional[AdvancedBackupSettings] = None


class UpdateFrameworkOutput(BaseModel):
    FrameworkName: Optional[FrameworkName] = None
    FrameworkArn: Optional[ARN] = None
    CreationTime: Optional[Timestamp] = None


class UpdateRecoveryPointLifecycleOutput(BaseModel):
    BackupVaultArn: Optional[ARN] = None
    RecoveryPointArn: Optional[ARN] = None
    Lifecycle: Optional[Lifecycle] = None
    CalculatedLifecycle: Optional[CalculatedLifecycle] = None


class UpdateReportPlanOutput(BaseModel):
    ReportPlanName: Optional[ReportPlanName] = None
    ReportPlanArn: Optional[ARN] = None
    CreationTime: Optional[Timestamp] = None


class BackupPlansListMember(BaseModel):
    """
    Contains metadata about a backup plan.
    """

    BackupPlanArn: Optional[ARN] = None
    BackupPlanId: Optional[String] = None
    CreationDate: Optional[Timestamp] = None
    DeletionDate: Optional[Timestamp] = None
    VersionId: Optional[String] = None
    BackupPlanName: Optional[BackupPlanName] = None
    CreatorRequestId: Optional[String] = None
    LastExecutionDate: Optional[Timestamp] = None
    AdvancedBackupSettings: Optional[AdvancedBackupSettings] = None


class BackupPlanVersionsList(BaseModel):
    __root__: List[BackupPlansListMember]


class BackupPlansList(BackupPlanVersionsList):
    pass


class CopyActions(BaseModel):
    __root__: List[CopyAction]


class BackupRule(BaseModel):
    """
    Specifies a scheduled task used to back up a selection of resources.
    """

    RuleName: BackupRuleName
    TargetBackupVaultName: BackupVaultName
    ScheduleExpression: Optional[CronExpression] = None
    StartWindowMinutes: Optional[WindowMinutes] = None
    CompletionWindowMinutes: Optional[WindowMinutes] = None
    Lifecycle: Optional[Lifecycle] = None
    RecoveryPointTags: Optional[Tags] = None
    RuleId: Optional[String] = None
    CopyActions: Optional[CopyActions] = None
    EnableContinuousBackup: Optional[Boolean1] = None


class BackupRuleInput(BaseModel):
    """
    Specifies a scheduled task used to back up a selection of resources.
    """

    RuleName: BackupRuleName
    TargetBackupVaultName: BackupVaultName
    ScheduleExpression: Optional[CronExpression] = None
    StartWindowMinutes: Optional[WindowMinutes] = None
    CompletionWindowMinutes: Optional[WindowMinutes] = None
    Lifecycle: Optional[Lifecycle] = None
    RecoveryPointTags: Optional[Tags] = None
    CopyActions: Optional[CopyActions] = None
    EnableContinuousBackup: Optional[Boolean1] = None


class BackupSelection(BaseModel):
    """
    Used to specify a set of resources to a backup plan.
    """

    SelectionName: BackupSelectionName
    IamRoleArn: IAMRoleArn
    Resources: Optional[ResourceArns] = None
    ListOfTags: Optional[ListOfTags] = None


class BackupVaultListMember(BaseModel):
    """
    Contains metadata about a backup vault.
    """

    BackupVaultName: Optional[BackupVaultName] = None
    BackupVaultArn: Optional[ARN] = None
    CreationDate: Optional[Timestamp] = None
    EncryptionKeyArn: Optional[ARN] = None
    CreatorRequestId: Optional[String] = None
    NumberOfRecoveryPoints: Optional[LongModel] = None


class BackupVaultList(BaseModel):
    __root__: List[BackupVaultListMember]


class CreateBackupSelectionInput(BaseModel):
    BackupSelection: BackupSelection
    CreatorRequestId: Optional[String] = None


class FrameworkControls(BaseModel):
    __root__: List[FrameworkControl]


class CreateFrameworkInput(BaseModel):
    FrameworkName: FrameworkName
    FrameworkDescription: Optional[FrameworkDescription] = None
    FrameworkControls: FrameworkControls
    IdempotencyToken: Optional[String] = None
    FrameworkTags: Optional[StringMap] = None


class ReportJob(BaseModel):
    """
    Contains detailed information about a report job. A report job compiles a report based on a report plan and publishes it to Amazon S3.
    """

    ReportJobId: Optional[ReportJobId] = None
    ReportPlanArn: Optional[ARN] = None
    ReportTemplate: Optional[String] = None
    CreationTime: Optional[Timestamp] = None
    CompletionTime: Optional[Timestamp] = None
    Status: Optional[String] = None
    StatusMessage: Optional[String] = None
    ReportDestination: Optional[ReportDestination] = None


class ProtectedResourcesList(BaseModel):
    __root__: List[ProtectedResource]


class RecoveryPointByBackupVaultList(BaseModel):
    __root__: List[RecoveryPointByBackupVault]


class RecoveryPointByResourceList(BaseModel):
    __root__: List[RecoveryPointByResource]


class ReportJobList(BaseModel):
    __root__: List[ReportJob]


class RestoreJobsList(BaseModel):
    __root__: List[RestoreJobsListMember]


class UpdateFrameworkInput(BaseModel):
    FrameworkDescription: Optional[FrameworkDescription] = None
    FrameworkControls: Optional[FrameworkControls] = None
    IdempotencyToken: Optional[String] = None


class CreateBackupPlanOutput(UpdateBackupPlanOutput):
    pass


class BackupRulesInput(BaseModel):
    __root__: List[BackupRuleInput]


class DescribeFrameworkOutput(BaseModel):
    FrameworkName: Optional[FrameworkName] = None
    FrameworkArn: Optional[ARN] = None
    FrameworkDescription: Optional[FrameworkDescription] = None
    FrameworkControls: Optional[FrameworkControls] = None
    CreationTime: Optional[Timestamp] = None
    DeploymentStatus: Optional[String] = None
    FrameworkStatus: Optional[String] = None
    IdempotencyToken: Optional[String] = None


class DescribeReportJobOutput(BaseModel):
    ReportJob: Optional[ReportJob] = None


class GetBackupSelectionOutput(BaseModel):
    BackupSelection: Optional[BackupSelection] = None
    SelectionId: Optional[String] = None
    BackupPlanId: Optional[String] = None
    CreationDate: Optional[Timestamp] = None
    CreatorRequestId: Optional[String] = None


class ListBackupPlanVersionsOutput(BaseModel):
    NextToken: Optional[String] = None
    BackupPlanVersionsList: Optional[BackupPlanVersionsList] = None


class ListBackupPlansOutput(BaseModel):
    NextToken: Optional[String] = None
    BackupPlansList: Optional[BackupPlansList] = None


class ListBackupVaultsOutput(BaseModel):
    BackupVaultList: Optional[BackupVaultList] = None
    NextToken: Optional[String] = None


class ListProtectedResourcesOutput(BaseModel):
    Results: Optional[ProtectedResourcesList] = None
    NextToken: Optional[String] = None


class ListRecoveryPointsByBackupVaultOutput(BaseModel):
    NextToken: Optional[String] = None
    RecoveryPoints: Optional[RecoveryPointByBackupVaultList] = None


class ListRecoveryPointsByResourceOutput(BaseModel):
    NextToken: Optional[String] = None
    RecoveryPoints: Optional[RecoveryPointByResourceList] = None


class ListReportJobsOutput(BaseModel):
    ReportJobs: Optional[ReportJobList] = None
    NextToken: Optional[String] = None


class ListRestoreJobsOutput(BaseModel):
    RestoreJobs: Optional[RestoreJobsList] = None
    NextToken: Optional[String] = None


class BackupRules(BaseModel):
    __root__: List[BackupRule]


class BackupPlan(BaseModel):
    """
    Contains an optional backup plan display name and an array of <code>BackupRule</code> objects, each of which specifies a backup rule. Each rule in a backup plan is a separate scheduled task and can back up a different selection of Amazon Web Services resources.
    """

    BackupPlanName: BackupPlanName
    Rules: BackupRules
    AdvancedBackupSettings: Optional[AdvancedBackupSettings] = None


class BackupPlanInput(BaseModel):
    """
    Contains an optional backup plan display name and an array of <code>BackupRule</code> objects, each of which specifies a backup rule. Each rule in a backup plan is a separate scheduled task and can back up a different selection of Amazon Web Services resources.
    """

    BackupPlanName: BackupPlanName
    Rules: BackupRulesInput
    AdvancedBackupSettings: Optional[AdvancedBackupSettings] = None


class CreateBackupPlanInput(BaseModel):
    BackupPlan: BackupPlanInput
    BackupPlanTags: Optional[Tags] = None
    CreatorRequestId: Optional[String] = None


class UpdateBackupPlanInput(BaseModel):
    BackupPlan: BackupPlanInput


class GetBackupPlanOutput(BaseModel):
    BackupPlan: Optional[BackupPlan] = None
    BackupPlanId: Optional[String] = None
    BackupPlanArn: Optional[ARN] = None
    VersionId: Optional[String] = None
    CreatorRequestId: Optional[String] = None
    CreationDate: Optional[Timestamp] = None
    DeletionDate: Optional[Timestamp] = None
    LastExecutionDate: Optional[Timestamp] = None
    AdvancedBackupSettings: Optional[AdvancedBackupSettings] = None


class GetBackupPlanFromJSONOutput(BaseModel):
    BackupPlan: Optional[BackupPlan] = None


class GetBackupPlanFromTemplateOutput(BaseModel):
    BackupPlanDocument: Optional[BackupPlan] = None
