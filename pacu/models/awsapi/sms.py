# generated by datamodel-codegen:
#   filename:  openapi.yaml
#   timestamp: 2021-12-31T02:58:27+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Annotated, Any, List, Optional

from pydantic import BaseModel, Field


class UnauthorizedOperationException(BaseModel):
    __root__: Any


class InvalidParameterException(UnauthorizedOperationException):
    pass


class MissingRequiredParameterException(UnauthorizedOperationException):
    pass


class InternalError(UnauthorizedOperationException):
    pass


class OperationNotPermittedException(UnauthorizedOperationException):
    pass


class ServerCannotBeReplicatedException(UnauthorizedOperationException):
    pass


class ReplicationJobAlreadyExistsException(UnauthorizedOperationException):
    pass


class NoConnectorsAvailableException(UnauthorizedOperationException):
    pass


class TemporarilyUnavailableException(UnauthorizedOperationException):
    pass


class DeleteAppResponse(BaseModel):
    pass


class DeleteAppLaunchConfigurationResponse(DeleteAppResponse):
    pass


class DeleteAppReplicationConfigurationResponse(DeleteAppResponse):
    pass


class DeleteAppValidationConfigurationResponse(DeleteAppResponse):
    pass


class DeleteReplicationJobResponse(DeleteAppResponse):
    pass


class ReplicationJobNotFoundException(UnauthorizedOperationException):
    pass


class DeleteServerCatalogResponse(DeleteAppResponse):
    pass


class DeleteServerCatalogRequest(BaseModel):
    pass


class DisassociateConnectorResponse(DeleteAppResponse):
    pass


class ImportAppCatalogResponse(DeleteAppResponse):
    pass


class ImportServerCatalogResponse(DeleteAppResponse):
    pass


class ImportServerCatalogRequest(BaseModel):
    pass


class LaunchAppResponse(DeleteAppResponse):
    pass


class NotifyAppValidationOutputResponse(DeleteAppResponse):
    pass


class PutAppLaunchConfigurationResponse(DeleteAppResponse):
    pass


class PutAppReplicationConfigurationResponse(DeleteAppResponse):
    pass


class PutAppValidationConfigurationResponse(DeleteAppResponse):
    pass


class StartAppReplicationResponse(DeleteAppResponse):
    pass


class StartOnDemandAppReplicationResponse(DeleteAppResponse):
    pass


class ReplicationRunLimitExceededException(UnauthorizedOperationException):
    pass


class DryRunOperationException(UnauthorizedOperationException):
    pass


class StopAppReplicationResponse(DeleteAppResponse):
    pass


class TerminateAppResponse(DeleteAppResponse):
    pass


class UpdateReplicationJobResponse(DeleteAppResponse):
    pass


class AmiId(BaseModel):
    __root__: str


class AppDescription(AmiId):
    pass


class AppId(AmiId):
    pass


class AppIdWithValidation(BaseModel):
    __root__: Annotated[str, Field(regex='^app-[0-9a-f]{17}$')]


class AppIds(BaseModel):
    __root__: List[AppId]


class AppLaunchConfigurationStatus(Enum):
    NOT_CONFIGURED = 'NOT_CONFIGURED'
    CONFIGURED = 'CONFIGURED'


class AppLaunchStatus(Enum):
    READY_FOR_CONFIGURATION = 'READY_FOR_CONFIGURATION'
    CONFIGURATION_IN_PROGRESS = 'CONFIGURATION_IN_PROGRESS'
    CONFIGURATION_INVALID = 'CONFIGURATION_INVALID'
    READY_FOR_LAUNCH = 'READY_FOR_LAUNCH'
    VALIDATION_IN_PROGRESS = 'VALIDATION_IN_PROGRESS'
    LAUNCH_PENDING = 'LAUNCH_PENDING'
    LAUNCH_IN_PROGRESS = 'LAUNCH_IN_PROGRESS'
    LAUNCHED = 'LAUNCHED'
    PARTIALLY_LAUNCHED = 'PARTIALLY_LAUNCHED'
    DELTA_LAUNCH_IN_PROGRESS = 'DELTA_LAUNCH_IN_PROGRESS'
    DELTA_LAUNCH_FAILED = 'DELTA_LAUNCH_FAILED'
    LAUNCH_FAILED = 'LAUNCH_FAILED'
    TERMINATE_IN_PROGRESS = 'TERMINATE_IN_PROGRESS'
    TERMINATE_FAILED = 'TERMINATE_FAILED'
    TERMINATED = 'TERMINATED'


class AppLaunchStatusMessage(AmiId):
    pass


class AppName(AmiId):
    pass


class AppReplicationStatus(Enum):
    READY_FOR_CONFIGURATION = 'READY_FOR_CONFIGURATION'
    CONFIGURATION_IN_PROGRESS = 'CONFIGURATION_IN_PROGRESS'
    CONFIGURATION_INVALID = 'CONFIGURATION_INVALID'
    READY_FOR_REPLICATION = 'READY_FOR_REPLICATION'
    VALIDATION_IN_PROGRESS = 'VALIDATION_IN_PROGRESS'
    REPLICATION_PENDING = 'REPLICATION_PENDING'
    REPLICATION_IN_PROGRESS = 'REPLICATION_IN_PROGRESS'
    REPLICATED = 'REPLICATED'
    PARTIALLY_REPLICATED = 'PARTIALLY_REPLICATED'
    DELTA_REPLICATION_IN_PROGRESS = 'DELTA_REPLICATION_IN_PROGRESS'
    DELTA_REPLICATED = 'DELTA_REPLICATED'
    DELTA_REPLICATION_FAILED = 'DELTA_REPLICATION_FAILED'
    REPLICATION_FAILED = 'REPLICATION_FAILED'
    REPLICATION_STOPPING = 'REPLICATION_STOPPING'
    REPLICATION_STOP_FAILED = 'REPLICATION_STOP_FAILED'
    REPLICATION_STOPPED = 'REPLICATION_STOPPED'


class AppReplicationStatusMessage(AmiId):
    pass


class AppStatus(Enum):
    CREATING = 'CREATING'
    ACTIVE = 'ACTIVE'
    UPDATING = 'UPDATING'
    DELETING = 'DELETING'
    DELETED = 'DELETED'
    DELETE_FAILED = 'DELETE_FAILED'


class AppStatusMessage(AmiId):
    pass


class ImportedAppId(AmiId):
    pass


class Timestamp(BaseModel):
    __root__: datetime


class RoleName(AmiId):
    pass


class TotalServerGroups(BaseModel):
    __root__: int


class TotalServers(TotalServerGroups):
    pass


class ValidationId(BaseModel):
    __root__: Annotated[str, Field(regex='^val-[0-9a-f]{17}$')]


class NonEmptyStringWithMaxLen255(BaseModel):
    __root__: Annotated[str, Field(max_length=255, min_length=1, regex='^[\\S]+$')]


class AppValidationStrategy(Enum):
    SSM = 'SSM'


class AssociatePublicIpAddress(BaseModel):
    __root__: bool


class AutoLaunch(AssociatePublicIpAddress):
    pass


class BucketName(AmiId):
    pass


class ClientToken(AmiId):
    pass


class Command(BaseModel):
    __root__: Annotated[str, Field(max_length=64000, min_length=1)]


class ConnectorId(AmiId):
    pass


class ConnectorVersion(AmiId):
    pass


class ConnectorStatus(Enum):
    HEALTHY = 'HEALTHY'
    UNHEALTHY = 'UNHEALTHY'


class VmManagerName(AmiId):
    pass


class VmManagerType(Enum):
    VSPHERE = 'VSPHERE'
    SCVMM = 'SCVMM'
    HYPERV_MANAGER = 'HYPERV-MANAGER'


class VmManagerId(AmiId):
    pass


class IpAddress(AmiId):
    pass


class MacAddress(AmiId):
    pass


class ConnectorCapability(Enum):
    VSPHERE = 'VSPHERE'
    SCVMM = 'SCVMM'
    HYPERV_MANAGER = 'HYPERV-MANAGER'
    SNAPSHOT_BATCHING = 'SNAPSHOT_BATCHING'
    SMS_OPTIMIZED = 'SMS_OPTIMIZED'


class ServerId(AmiId):
    pass


class Frequency(TotalServerGroups):
    pass


class RunOnce(AssociatePublicIpAddress):
    pass


class LicenseType(Enum):
    AWS = 'AWS'
    BYOL = 'BYOL'


class Description(AmiId):
    pass


class NumberOfRecentAmisToKeep(TotalServerGroups):
    pass


class Encrypted(AssociatePublicIpAddress):
    pass


class KmsKeyId(AmiId):
    pass


class ReplicationJobId(AmiId):
    pass


class ForceStopAppReplication(AssociatePublicIpAddress):
    pass


class ForceTerminateApp(AssociatePublicIpAddress):
    pass


class EC2KeyName(AmiId):
    pass


class ExecutionTimeoutSeconds(BaseModel):
    __root__: Annotated[int, Field(ge=60.0, le=28800.0)]


class OutputFormat(Enum):
    JSON = 'JSON'
    YAML = 'YAML'


class NextToken(AmiId):
    pass


class MaxResults(TotalServerGroups):
    pass


class ServerCatalogStatus(Enum):
    NOT_IMPORTED = 'NOT_IMPORTED'
    IMPORTING = 'IMPORTING'
    AVAILABLE = 'AVAILABLE'
    DELETED = 'DELETED'
    EXPIRED = 'EXPIRED'


class InstanceId(BaseModel):
    __root__: Annotated[str, Field(regex='(^i-(\\w{8}|\\w{17})$)|(^mi-\\w{17}$)')]


class InstanceType(AmiId):
    pass


class StackName(AmiId):
    pass


class StackId(AmiId):
    pass


class LaunchOrder(TotalServerGroups):
    pass


class LogicalId(AmiId):
    pass


class ValidationStatus(Enum):
    READY_FOR_VALIDATION = 'READY_FOR_VALIDATION'
    PENDING = 'PENDING'
    IN_PROGRESS = 'IN_PROGRESS'
    SUCCEEDED = 'SUCCEEDED'
    FAILED = 'FAILED'


class ValidationStatusMessage(BaseModel):
    __root__: Annotated[str, Field(max_length=2500)]


class NotificationContext(BaseModel):
    """
    Contains the status of validating an application.
    """

    validationId: Optional[ValidationId] = None
    status: Optional[ValidationStatus] = None
    statusMessage: Optional[ValidationStatusMessage] = None


class ServerType(Enum):
    VIRTUAL_MACHINE = 'VIRTUAL_MACHINE'


class ReplicationJobState(Enum):
    PENDING = 'PENDING'
    ACTIVE = 'ACTIVE'
    FAILED = 'FAILED'
    DELETING = 'DELETING'
    DELETED = 'DELETED'
    COMPLETED = 'COMPLETED'
    PAUSED_ON_FAILURE = 'PAUSED_ON_FAILURE'
    FAILING = 'FAILING'


class ReplicationJobStatusMessage(AmiId):
    pass


class ReplicationJobTerminated(AssociatePublicIpAddress):
    pass


class ReplicationRunId(AmiId):
    pass


class ReplicationRunState(Enum):
    PENDING = 'PENDING'
    MISSED = 'MISSED'
    ACTIVE = 'ACTIVE'
    FAILED = 'FAILED'
    COMPLETED = 'COMPLETED'
    DELETING = 'DELETING'
    DELETED = 'DELETED'


class ReplicationRunType(Enum):
    ON_DEMAND = 'ON_DEMAND'
    AUTOMATIC = 'AUTOMATIC'


class ReplicationRunStatusMessage(AmiId):
    pass


class ReplicationRunStage(AmiId):
    pass


class ReplicationRunStageProgress(AmiId):
    pass


class S3BucketName(BaseModel):
    __root__: Annotated[str, Field(max_length=63, min_length=3)]


class S3KeyName(BaseModel):
    __root__: Annotated[str, Field(max_length=1024)]


class ScriptType(Enum):
    SHELL_SCRIPT = 'SHELL_SCRIPT'
    POWERSHELL_SCRIPT = 'POWERSHELL_SCRIPT'


class SecurityGroup(AmiId):
    pass


class ServerGroupId(AmiId):
    pass


class ServerGroupName(AmiId):
    pass


class VPC(AmiId):
    pass


class Subnet(AmiId):
    pass


class ServerReplicationParameters(BaseModel):
    """
    The replication parameters for replicating a server.
    """

    seedTime: Optional[Timestamp] = None
    frequency: Optional[Frequency] = None
    runOnce: Optional[RunOnce] = None
    licenseType: Optional[LicenseType] = None
    numberOfRecentAmisToKeep: Optional[NumberOfRecentAmisToKeep] = None
    encrypted: Optional[Encrypted] = None
    kmsKeyId: Optional[KmsKeyId] = None


class ServerValidationStrategy(Enum):
    USERDATA = 'USERDATA'


class TagKey(AmiId):
    pass


class TagValue(AmiId):
    pass


class Tag(BaseModel):
    """
    Key/value pair that can be assigned to an application.
    """

    key: Optional[TagKey] = None
    value: Optional[TagValue] = None


class VmId(AmiId):
    pass


class VmName(AmiId):
    pass


class VmPath(AmiId):
    pass


class VmServerAddress(BaseModel):
    """
    Represents a VM server location.
    """

    vmManagerId: Optional[VmManagerId] = None
    vmId: Optional[VmId] = None


class CreateReplicationJobResponse(BaseModel):
    replicationJobId: Optional[ReplicationJobId] = None


class CreateReplicationJobRequest(BaseModel):
    serverId: ServerId
    seedReplicationTime: Timestamp
    frequency: Optional[Frequency] = None
    runOnce: Optional[RunOnce] = None
    licenseType: Optional[LicenseType] = None
    roleName: Optional[RoleName] = None
    description: Optional[Description] = None
    numberOfRecentAmisToKeep: Optional[NumberOfRecentAmisToKeep] = None
    encrypted: Optional[Encrypted] = None
    kmsKeyId: Optional[KmsKeyId] = None


class DeleteAppRequest(BaseModel):
    appId: Optional[AppId] = None
    forceStopAppReplication: Optional[ForceStopAppReplication] = None
    forceTerminateApp: Optional[ForceTerminateApp] = None


class DeleteAppLaunchConfigurationRequest(BaseModel):
    appId: Optional[AppId] = None


class DeleteAppReplicationConfigurationRequest(BaseModel):
    appId: Optional[AppId] = None


class DeleteAppValidationConfigurationRequest(BaseModel):
    appId: AppIdWithValidation


class DeleteReplicationJobRequest(BaseModel):
    replicationJobId: ReplicationJobId


class DisassociateConnectorRequest(BaseModel):
    connectorId: ConnectorId


class GenerateChangeSetRequest(BaseModel):
    appId: Optional[AppId] = None
    changesetFormat: Optional[OutputFormat] = None


class GenerateTemplateRequest(BaseModel):
    appId: Optional[AppId] = None
    templateFormat: Optional[OutputFormat] = None


class GetAppRequest(BaseModel):
    appId: Optional[AppId] = None


class GetAppLaunchConfigurationRequest(BaseModel):
    appId: Optional[AppId] = None


class GetAppReplicationConfigurationRequest(BaseModel):
    appId: Optional[AppId] = None


class GetAppValidationConfigurationRequest(BaseModel):
    appId: AppIdWithValidation


class GetAppValidationOutputRequest(BaseModel):
    appId: AppIdWithValidation


class GetConnectorsRequest(BaseModel):
    nextToken: Optional[NextToken] = None
    maxResults: Optional[MaxResults] = None


class GetReplicationJobsRequest(BaseModel):
    replicationJobId: Optional[ReplicationJobId] = None
    nextToken: Optional[NextToken] = None
    maxResults: Optional[MaxResults] = None


class GetReplicationRunsRequest(BaseModel):
    replicationJobId: ReplicationJobId
    nextToken: Optional[NextToken] = None
    maxResults: Optional[MaxResults] = None


class ImportAppCatalogRequest(BaseModel):
    roleName: Optional[RoleName] = None


class LaunchAppRequest(BaseModel):
    appId: Optional[AppId] = None


class ListAppsRequest(BaseModel):
    appIds: Optional[AppIds] = None
    nextToken: Optional[NextToken] = None
    maxResults: Optional[MaxResults] = None


class NotifyAppValidationOutputRequest(BaseModel):
    appId: AppIdWithValidation
    notificationContext: Optional[NotificationContext] = None


class StartAppReplicationRequest(BaseModel):
    appId: Optional[AppId] = None


class StartOnDemandAppReplicationRequest(BaseModel):
    appId: AppId
    description: Optional[Description] = None


class StartOnDemandReplicationRunResponse(BaseModel):
    replicationRunId: Optional[ReplicationRunId] = None


class StartOnDemandReplicationRunRequest(BaseModel):
    replicationJobId: ReplicationJobId
    description: Optional[Description] = None


class StopAppReplicationRequest(BaseModel):
    appId: Optional[AppId] = None


class TerminateAppRequest(BaseModel):
    appId: Optional[AppId] = None


class UpdateReplicationJobRequest(BaseModel):
    replicationJobId: ReplicationJobId
    frequency: Optional[Frequency] = None
    nextReplicationRunStartTime: Optional[Timestamp] = None
    licenseType: Optional[LicenseType] = None
    roleName: Optional[RoleName] = None
    description: Optional[Description] = None
    numberOfRecentAmisToKeep: Optional[NumberOfRecentAmisToKeep] = None
    encrypted: Optional[Encrypted] = None
    kmsKeyId: Optional[KmsKeyId] = None


class LaunchDetails(BaseModel):
    """
    Details about the latest launch of an application.
    """

    latestLaunchTime: Optional[Timestamp] = None
    stackName: Optional[StackName] = None
    stackId: Optional[StackId] = None


class AppSummary(BaseModel):
    """
    Information about the application.
    """

    appId: Optional[AppId] = None
    importedAppId: Optional[ImportedAppId] = None
    name: Optional[AppName] = None
    description: Optional[AppDescription] = None
    status: Optional[AppStatus] = None
    statusMessage: Optional[AppStatusMessage] = None
    replicationConfigurationStatus: Optional[AppLaunchConfigurationStatus] = None
    replicationStatus: Optional[AppReplicationStatus] = None
    replicationStatusMessage: Optional[AppReplicationStatusMessage] = None
    latestReplicationTime: Optional[Timestamp] = None
    launchConfigurationStatus: Optional[AppLaunchConfigurationStatus] = None
    launchStatus: Optional[AppLaunchStatus] = None
    launchStatusMessage: Optional[AppLaunchStatusMessage] = None
    launchDetails: Optional[LaunchDetails] = None
    creationTime: Optional[Timestamp] = None
    lastModified: Optional[Timestamp] = None
    roleName: Optional[RoleName] = None
    totalServerGroups: Optional[TotalServerGroups] = None
    totalServers: Optional[TotalServers] = None


class Apps(BaseModel):
    __root__: List[AppSummary]


class ConnectorCapabilityList(BaseModel):
    __root__: List[ConnectorCapability]


class Connector(BaseModel):
    """
    Represents a connector.
    """

    connectorId: Optional[ConnectorId] = None
    version: Optional[ConnectorVersion] = None
    status: Optional[ConnectorStatus] = None
    capabilityList: Optional[ConnectorCapabilityList] = None
    vmManagerName: Optional[VmManagerName] = None
    vmManagerType: Optional[VmManagerType] = None
    vmManagerId: Optional[VmManagerId] = None
    ipAddress: Optional[IpAddress] = None
    macAddress: Optional[MacAddress] = None
    associatedOn: Optional[Timestamp] = None


class ConnectorList(BaseModel):
    __root__: List[Connector]


class Tags(BaseModel):
    __root__: List[Tag]


class S3Location(BaseModel):
    """
    Location of an Amazon S3 object.
    """

    bucket: Optional[S3BucketName] = None
    key: Optional[S3KeyName] = None


class VmServerAddressList(BaseModel):
    __root__: List[VmServerAddress]


class VmServer(BaseModel):
    """
    Represents a VM server.
    """

    vmServerAddress: Optional[VmServerAddress] = None
    vmName: Optional[VmName] = None
    vmManagerName: Optional[VmManagerName] = None
    vmManagerType: Optional[VmManagerType] = None
    vmPath: Optional[VmPath] = None


class ReplicationRunStageDetails(BaseModel):
    """
    Details of the current stage of a replication run.
    """

    stage: Optional[ReplicationRunStage] = None
    stageProgress: Optional[ReplicationRunStageProgress] = None


class ReplicationRun(BaseModel):
    """
    Represents a replication run.
    """

    replicationRunId: Optional[ReplicationRunId] = None
    state: Optional[ReplicationRunState] = None
    type: Optional[ReplicationRunType] = None
    stageDetails: Optional[ReplicationRunStageDetails] = None
    statusMessage: Optional[ReplicationRunStatusMessage] = None
    amiId: Optional[AmiId] = None
    scheduledStartTime: Optional[Timestamp] = None
    completedTime: Optional[Timestamp] = None
    description: Optional[Description] = None
    encrypted: Optional[Encrypted] = None
    kmsKeyId: Optional[KmsKeyId] = None


class Source(BaseModel):
    """
    Contains the location of a validation script.
    """

    s3Location: Optional[S3Location] = None


class Server(BaseModel):
    """
    Represents a server.
    """

    serverId: Optional[ServerId] = None
    serverType: Optional[ServerType] = None
    vmServer: Optional[VmServer] = None
    replicationJobId: Optional[ReplicationJobId] = None
    replicationJobTerminated: Optional[ReplicationJobTerminated] = None


class UserData(Source):
    """
    A script that runs on first launch of an Amazon EC2 instance. Used for configuring the server during launch.
    """

    pass


class ServerLaunchConfiguration(BaseModel):
    """
    Launch configuration for a server.
    """

    server: Optional[Server] = None
    logicalId: Optional[LogicalId] = None
    vpc: Optional[VPC] = None
    subnet: Optional[Subnet] = None
    securityGroup: Optional[SecurityGroup] = None
    ec2KeyName: Optional[EC2KeyName] = None
    userData: Optional[UserData] = None
    instanceType: Optional[InstanceType] = None
    associatePublicIpAddress: Optional[AssociatePublicIpAddress] = None
    iamInstanceProfileName: Optional[RoleName] = None
    configureScript: Optional[S3Location] = None
    configureScriptType: Optional[ScriptType] = None


class ServerReplicationConfiguration(BaseModel):
    """
    Replication configuration of a server.
    """

    server: Optional[Server] = None
    serverReplicationParameters: Optional[ServerReplicationParameters] = None


class UserDataValidationParameters(BaseModel):
    """
    Contains validation parameters.
    """

    source: Optional[Source] = None
    scriptType: Optional[ScriptType] = None


class ServerValidationConfiguration(BaseModel):
    """
    Configuration for validating an instance.
    """

    server: Optional[Server] = None
    validationId: Optional[ValidationId] = None
    name: Optional[NonEmptyStringWithMaxLen255] = None
    serverValidationStrategy: Optional[ServerValidationStrategy] = None
    userDataValidationParameters: Optional[UserDataValidationParameters] = None


class ServerValidationOutput(BaseModel):
    """
    Contains output from validating an instance.
    """

    server: Optional[Server] = None


class GenerateChangeSetResponse(Source):
    pass


class GenerateTemplateResponse(Source):
    pass


class GetConnectorsResponse(BaseModel):
    connectorList: Optional[ConnectorList] = None
    nextToken: Optional[NextToken] = None


class GetServersRequest(BaseModel):
    nextToken: Optional[NextToken] = None
    maxResults: Optional[MaxResults] = None
    vmServerAddressList: Optional[VmServerAddressList] = None


class ListAppsResponse(BaseModel):
    apps: Optional[Apps] = None
    nextToken: Optional[NextToken] = None


class SSMValidationParameters(BaseModel):
    """
    Contains validation parameters.
    """

    source: Optional[Source] = None
    instanceId: Optional[InstanceId] = None
    scriptType: Optional[ScriptType] = None
    command: Optional[Command] = None
    executionTimeoutSeconds: Optional[ExecutionTimeoutSeconds] = None
    outputS3BucketName: Optional[BucketName] = None


class AppValidationConfiguration(BaseModel):
    """
    Configuration for validating an application.
    """

    validationId: Optional[ValidationId] = None
    name: Optional[NonEmptyStringWithMaxLen255] = None
    appValidationStrategy: Optional[AppValidationStrategy] = None
    ssmValidationParameters: Optional[SSMValidationParameters] = None


class AppValidationConfigurations(BaseModel):
    __root__: List[AppValidationConfiguration]


class SSMOutput(Source):
    """
    Contains the location of validation output.
    """

    pass


class AppValidationOutput(BaseModel):
    """
    Output from validating an application.
    """

    ssmOutput: Optional[SSMOutput] = None


class ReplicationRunList(BaseModel):
    __root__: List[ReplicationRun]


class ServerList(BaseModel):
    __root__: List[Server]


class ServerGroup(BaseModel):
    """
    Logical grouping of servers.
    """

    serverGroupId: Optional[ServerGroupId] = None
    name: Optional[ServerGroupName] = None
    serverList: Optional[ServerList] = None


class ServerLaunchConfigurations(BaseModel):
    __root__: List[ServerLaunchConfiguration]


class ServerGroupLaunchConfiguration(BaseModel):
    """
    Launch configuration for a server group.
    """

    serverGroupId: Optional[ServerGroupId] = None
    launchOrder: Optional[LaunchOrder] = None
    serverLaunchConfigurations: Optional[ServerLaunchConfigurations] = None


class ServerReplicationConfigurations(BaseModel):
    __root__: List[ServerReplicationConfiguration]


class ServerGroupReplicationConfiguration(BaseModel):
    """
    Replication configuration for a server group.
    """

    serverGroupId: Optional[ServerGroupId] = None
    serverReplicationConfigurations: Optional[ServerReplicationConfigurations] = None


class ServerValidationConfigurations(BaseModel):
    __root__: List[ServerValidationConfiguration]


class ServerGroupValidationConfiguration(BaseModel):
    """
    Configuration for validating an instance.
    """

    serverGroupId: Optional[ServerGroupId] = None
    serverValidationConfigurations: Optional[ServerValidationConfigurations] = None


class ValidationOutput(BaseModel):
    """
    Contains validation output.
    """

    validationId: Optional[ValidationId] = None
    name: Optional[NonEmptyStringWithMaxLen255] = None
    status: Optional[ValidationStatus] = None
    statusMessage: Optional[ValidationStatusMessage] = None
    latestValidationTime: Optional[Timestamp] = None
    appValidationOutput: Optional[AppValidationOutput] = None
    serverValidationOutput: Optional[ServerValidationOutput] = None


class GetServersResponse(BaseModel):
    lastModifiedOn: Optional[Timestamp] = None
    serverCatalogStatus: Optional[ServerCatalogStatus] = None
    serverList: Optional[ServerList] = None
    nextToken: Optional[NextToken] = None


class ServerGroups(BaseModel):
    __root__: List[ServerGroup]


class ServerGroupLaunchConfigurations(BaseModel):
    __root__: List[ServerGroupLaunchConfiguration]


class ServerGroupReplicationConfigurations(BaseModel):
    __root__: List[ServerGroupReplicationConfiguration]


class ServerGroupValidationConfigurations(BaseModel):
    __root__: List[ServerGroupValidationConfiguration]


class ValidationOutputList(BaseModel):
    __root__: List[ValidationOutput]


class ReplicationJob(BaseModel):
    """
    Represents a replication job.
    """

    replicationJobId: Optional[ReplicationJobId] = None
    serverId: Optional[ServerId] = None
    serverType: Optional[ServerType] = None
    vmServer: Optional[VmServer] = None
    seedReplicationTime: Optional[Timestamp] = None
    frequency: Optional[Frequency] = None
    runOnce: Optional[RunOnce] = None
    nextReplicationRunStartTime: Optional[Timestamp] = None
    licenseType: Optional[LicenseType] = None
    roleName: Optional[RoleName] = None
    latestAmiId: Optional[AmiId] = None
    state: Optional[ReplicationJobState] = None
    statusMessage: Optional[ReplicationJobStatusMessage] = None
    description: Optional[Description] = None
    numberOfRecentAmisToKeep: Optional[NumberOfRecentAmisToKeep] = None
    encrypted: Optional[Encrypted] = None
    kmsKeyId: Optional[KmsKeyId] = None
    replicationRunList: Optional[ReplicationRunList] = None


class CreateAppResponse(BaseModel):
    appSummary: Optional[AppSummary] = None
    serverGroups: Optional[ServerGroups] = None
    tags: Optional[Tags] = None


class CreateAppRequest(BaseModel):
    name: Optional[AppName] = None
    description: Optional[AppDescription] = None
    roleName: Optional[RoleName] = None
    clientToken: Optional[ClientToken] = None
    serverGroups: Optional[ServerGroups] = None
    tags: Optional[Tags] = None


class GetAppResponse(CreateAppResponse):
    pass


class GetAppLaunchConfigurationResponse(BaseModel):
    appId: Optional[AppId] = None
    roleName: Optional[RoleName] = None
    autoLaunch: Optional[AutoLaunch] = None
    serverGroupLaunchConfigurations: Optional[ServerGroupLaunchConfigurations] = None


class GetAppReplicationConfigurationResponse(BaseModel):
    serverGroupReplicationConfigurations: Optional[
        ServerGroupReplicationConfigurations
    ] = None


class GetAppValidationConfigurationResponse(BaseModel):
    appValidationConfigurations: Optional[AppValidationConfigurations] = None
    serverGroupValidationConfigurations: Optional[
        ServerGroupValidationConfigurations
    ] = None


class GetAppValidationOutputResponse(BaseModel):
    validationOutputList: Optional[ValidationOutputList] = None


class GetReplicationRunsResponse(BaseModel):
    replicationJob: Optional[ReplicationJob] = None
    replicationRunList: Optional[ReplicationRunList] = None
    nextToken: Optional[NextToken] = None


class PutAppLaunchConfigurationRequest(BaseModel):
    appId: Optional[AppId] = None
    roleName: Optional[RoleName] = None
    autoLaunch: Optional[AutoLaunch] = None
    serverGroupLaunchConfigurations: Optional[ServerGroupLaunchConfigurations] = None


class PutAppReplicationConfigurationRequest(BaseModel):
    appId: Optional[AppId] = None
    serverGroupReplicationConfigurations: Optional[
        ServerGroupReplicationConfigurations
    ] = None


class PutAppValidationConfigurationRequest(BaseModel):
    appId: AppIdWithValidation
    appValidationConfigurations: Optional[AppValidationConfigurations] = None
    serverGroupValidationConfigurations: Optional[
        ServerGroupValidationConfigurations
    ] = None


class UpdateAppResponse(CreateAppResponse):
    pass


class UpdateAppRequest(BaseModel):
    appId: Optional[AppId] = None
    name: Optional[AppName] = None
    description: Optional[AppDescription] = None
    roleName: Optional[RoleName] = None
    serverGroups: Optional[ServerGroups] = None
    tags: Optional[Tags] = None


class ReplicationJobList(BaseModel):
    __root__: List[ReplicationJob]


class GetReplicationJobsResponse(BaseModel):
    replicationJobList: Optional[ReplicationJobList] = None
    nextToken: Optional[NextToken] = None