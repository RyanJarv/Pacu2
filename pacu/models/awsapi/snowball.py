# generated by datamodel-codegen:
#   filename:  openapi.yaml
#   timestamp: 2021-12-31T02:58:32+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Annotated, Any, List, Optional

from pydantic import BaseModel, Field


class CancelClusterResult(BaseModel):
    pass


class KMSRequestFailedException(BaseModel):
    __root__: Any


class InvalidJobStateException(KMSRequestFailedException):
    pass


class InvalidResourceException(KMSRequestFailedException):
    pass


class CancelJobResult(CancelClusterResult):
    pass


class InvalidAddressException(KMSRequestFailedException):
    pass


class UnsupportedAddressException(KMSRequestFailedException):
    pass


class InvalidInputCombinationException(KMSRequestFailedException):
    pass


class Ec2RequestFailedException(KMSRequestFailedException):
    pass


class ClusterLimitExceededException(KMSRequestFailedException):
    pass


class ConflictException(KMSRequestFailedException):
    pass


class ReturnShippingLabelAlreadyExistsException(KMSRequestFailedException):
    pass


class InvalidNextTokenException(KMSRequestFailedException):
    pass


class GetSnowballUsageRequest(BaseModel):
    pass


class UpdateClusterResult(CancelClusterResult):
    pass


class UpdateJobResult(CancelClusterResult):
    pass


class UpdateJobShipmentStateResult(CancelClusterResult):
    pass


class UpdateLongTermPricingResult(CancelClusterResult):
    pass


class AddressId(BaseModel):
    __root__: Annotated[
        str,
        Field(
            max_length=40,
            min_length=40,
            regex='ADID[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}',
        ),
    ]


class String(BaseModel):
    __root__: Annotated[str, Field(max_length=1024, min_length=1)]


class Boolean(BaseModel):
    __root__: bool


class Address(BaseModel):
    """
    The address that you want the Snow device(s) associated with a specific job to be shipped to. Addresses are validated at the time of creation. The address you provide must be located within the serviceable area of your region. Although no individual elements of the <code>Address</code> are required, if the address is invalid or unsupported, then an exception is thrown.
    """

    AddressId: Optional[AddressId] = None
    Name: Optional[String] = None
    Company: Optional[String] = None
    Street1: Optional[String] = None
    Street2: Optional[String] = None
    Street3: Optional[String] = None
    City: Optional[String] = None
    StateOrProvince: Optional[String] = None
    PrefectureOrDistrict: Optional[String] = None
    Landmark: Optional[String] = None
    Country: Optional[String] = None
    PostalCode: Optional[String] = None
    PhoneNumber: Optional[String] = None
    IsRestricted: Optional[Boolean] = None


class AddressList(BaseModel):
    __root__: List[Address]


class AmiId(BaseModel):
    __root__: Annotated[
        str,
        Field(
            max_length=21, min_length=12, regex='(ami-[0-9a-f]{8})|(ami-[0-9a-f]{17})'
        ),
    ]


class ClusterId(BaseModel):
    __root__: Annotated[
        str,
        Field(
            max_length=39,
            min_length=39,
            regex='CID[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}',
        ),
    ]


class JobId(BaseModel):
    __root__: Annotated[
        str,
        Field(
            max_length=39,
            min_length=39,
            regex='(M|J)ID[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}',
        ),
    ]


class ClusterState(Enum):
    AwaitingQuorum = 'AwaitingQuorum'
    Pending = 'Pending'
    InUse = 'InUse'
    Complete = 'Complete'
    Cancelled = 'Cancelled'


class Timestamp(BaseModel):
    __root__: datetime


class ClusterListEntry(BaseModel):
    """
    Contains a cluster's state, a cluster's ID, and other important information.
    """

    ClusterId: Optional[String] = None
    ClusterState: Optional[ClusterState] = None
    CreationDate: Optional[Timestamp] = None
    Description: Optional[String] = None


class ClusterListEntryList(BaseModel):
    __root__: List[ClusterListEntry]


class KmsKeyARN(BaseModel):
    __root__: Annotated[
        str, Field(max_length=255, regex='arn:aws.*:kms:.*:[0-9]{12}:key/.*')
    ]


class RoleARN(BaseModel):
    __root__: Annotated[
        str, Field(max_length=255, regex='arn:aws.*:iam::[0-9]{12}:role/.*')
    ]


class JobType(Enum):
    IMPORT = 'IMPORT'
    EXPORT = 'EXPORT'
    LOCAL_USE = 'LOCAL_USE'


class SnowballType(Enum):
    STANDARD = 'STANDARD'
    EDGE = 'EDGE'
    EDGE_C = 'EDGE_C'
    EDGE_CG = 'EDGE_CG'
    EDGE_S = 'EDGE_S'
    SNC1_HDD = 'SNC1_HDD'
    SNC1_SSD = 'SNC1_SSD'


class ShippingOption(Enum):
    SECOND_DAY = 'SECOND_DAY'
    NEXT_DAY = 'NEXT_DAY'
    EXPRESS = 'EXPRESS'
    STANDARD = 'STANDARD'


class CompatibleImage(BaseModel):
    """
    A JSON-formatted object that describes a compatible Amazon Machine Image (AMI), including the ID and name for a Snow device AMI. This AMI is compatible with the device's physical hardware requirements, and it should be able to be run in an SBE1 instance on the device.
    """

    AmiId: Optional[String] = None
    Name: Optional[String] = None


class CompatibleImageList(BaseModel):
    __root__: List[CompatibleImage]


class RemoteManagement(Enum):
    INSTALLED_ONLY = 'INSTALLED_ONLY'
    INSTALLED_AUTOSTART = 'INSTALLED_AUTOSTART'


class SnowballCapacity(Enum):
    T50 = 'T50'
    T80 = 'T80'
    T100 = 'T100'
    T42 = 'T42'
    T98 = 'T98'
    T8 = 'T8'
    T14 = 'T14'
    NoPreference = 'NoPreference'


class LongTermPricingId(BaseModel):
    __root__: Annotated[
        str,
        Field(
            max_length=41,
            min_length=41,
            regex='LTPID[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}',
        ),
    ]


class LongTermPricingType(Enum):
    OneYear = 'OneYear'
    ThreeYear = 'ThreeYear'


class JavaBoolean(Boolean):
    pass


class ShippingLabelStatus(Enum):
    InProgress = 'InProgress'
    TimedOut = 'TimedOut'
    Succeeded = 'Succeeded'
    Failed = 'Failed'


class Long(BaseModel):
    __root__: int


class DataTransfer(BaseModel):
    """
    Defines the real-time status of a Snow device's data transfer while the device is at AWS. This data is only available while a job has a <code>JobState</code> value of <code>InProgress</code>, for both import and export jobs.
    """

    BytesTransferred: Optional[Long] = None
    ObjectsTransferred: Optional[Long] = None
    TotalBytes: Optional[Long] = None
    TotalObjects: Optional[Long] = None


class ListLimit(BaseModel):
    __root__: Annotated[int, Field(ge=0.0, le=100.0)]


class DeviceServiceName(Enum):
    NFS_ON_DEVICE_SERVICE = 'NFS_ON_DEVICE_SERVICE'
    S3_ON_DEVICE_SERVICE = 'S3_ON_DEVICE_SERVICE'


class Ec2AmiResource(BaseModel):
    """
    A JSON-formatted object that contains the IDs for an Amazon Machine Image (AMI), including the Amazon EC2 AMI ID and the Snow device AMI ID. Each AMI has these two IDs to simplify identifying the AMI in both the AWS Cloud and on the device.
    """

    AmiId: AmiId
    SnowballAmiId: Optional[String] = None


class Ec2AmiResourceList(BaseModel):
    __root__: List[Ec2AmiResource]


class ResourceARN(BaseModel):
    __root__: Annotated[str, Field(max_length=255, regex='arn:aws.*:*')]


class EventTriggerDefinition(BaseModel):
    """
    The container for the <a>EventTriggerDefinition$EventResourceARN</a>.
    """

    EventResourceARN: Optional[ResourceARN] = None


class EventTriggerDefinitionList(BaseModel):
    __root__: List[EventTriggerDefinition]


class GSTIN(BaseModel):
    __root__: Annotated[
        str, Field(regex='\\d{2}[A-Z]{5}\\d{4}[A-Z]{1}[A-Z\\d]{1}[Z]{1}[A-Z\\d]{1}')
    ]


class Integer(Long):
    pass


class INDTaxDocuments(BaseModel):
    """
    The tax documents required in AWS Regions in India.
    """

    GSTIN: Optional[GSTIN] = None


class JobState(Enum):
    New = 'New'
    PreparingAppliance = 'PreparingAppliance'
    PreparingShipment = 'PreparingShipment'
    InTransitToCustomer = 'InTransitToCustomer'
    WithCustomer = 'WithCustomer'
    InTransitToAWS = 'InTransitToAWS'
    WithAWSSortingFacility = 'WithAWSSortingFacility'
    WithAWS = 'WithAWS'
    InProgress = 'InProgress'
    Complete = 'Complete'
    Cancelled = 'Cancelled'
    Listing = 'Listing'
    Pending = 'Pending'


class JobListEntry(BaseModel):
    """
    Each <code>JobListEntry</code> object contains a job's state, a job's ID, and a value that indicates whether the job is a job part, in the case of an export job.
    """

    JobId: Optional[String] = None
    JobState: Optional[JobState] = None
    IsMaster: Optional[Boolean] = None
    JobType: Optional[JobType] = None
    SnowballType: Optional[SnowballType] = None
    CreationDate: Optional[Timestamp] = None
    Description: Optional[String] = None


class JobListEntryList(BaseModel):
    __root__: List[JobListEntry]


class JobLogs(BaseModel):
    """
    <p>Contains job logs. Whenever a Snow device is used to import data into or export data out of Amazon S3, you'll have the option of downloading a PDF job report. Job logs are returned as a part of the response syntax of the <code>DescribeJob</code> action in the <code>JobMetadata</code> data type. The job logs can be accessed for up to 60 minutes after this request has been made. To access any of the job logs after 60 minutes have passed, you'll have to make another call to the <code>DescribeJob</code> action.</p> <p>For import jobs, the PDF job report becomes available at the end of the import process. For export jobs, your job report typically becomes available while the Snow device for your job part is being delivered to you.</p> <p>The job report provides you insight into the state of your Amazon S3 data transfer. The report includes details about your job or job part for your records.</p> <p>For deeper visibility into the status of your transferred objects, you can look at the two associated logs: a success log and a failure log. The logs are saved in comma-separated value (CSV) format, and the name of each log includes the ID of the job or job part that the log describes.</p>
    """

    JobCompletionReportURI: Optional[String] = None
    JobSuccessLogURI: Optional[String] = None
    JobFailureLogURI: Optional[String] = None


class JobStateList(BaseModel):
    __root__: List[JobState]


class KeyRange(BaseModel):
    """
    Contains a key range. For export jobs, a <code>S3Resource</code> object can have an optional <code>KeyRange</code> value. The length of the range is defined at job creation, and has either an inclusive <code>BeginMarker</code>, an inclusive <code>EndMarker</code>, or both. Ranges are UTF-8 binary sorted.
    """

    BeginMarker: Optional[String] = None
    EndMarker: Optional[String] = None


class LambdaResource(BaseModel):
    """
    Identifies
    """

    LambdaArn: Optional[ResourceARN] = None
    EventTriggers: Optional[EventTriggerDefinitionList] = None


class LongTermPricingAssociatedJobIdList(BaseModel):
    __root__: List[JobId]


class LongTermPricingListEntry(BaseModel):
    """
    Each <code>LongTermPricingListEntry</code> object contains information about a long-term pricing type.
    """

    LongTermPricingId: Optional[LongTermPricingId] = None
    LongTermPricingEndDate: Optional[Timestamp] = None
    LongTermPricingStartDate: Optional[Timestamp] = None
    LongTermPricingType: Optional[LongTermPricingType] = None
    CurrentActiveJob: Optional[JobId] = None
    ReplacementJob: Optional[JobId] = None
    IsLongTermPricingAutoRenew: Optional[JavaBoolean] = None
    LongTermPricingStatus: Optional[String] = None
    SnowballType: Optional[SnowballType] = None
    JobIds: Optional[LongTermPricingAssociatedJobIdList] = None


class StorageLimit(BaseModel):
    __root__: Annotated[int, Field(ge=0.0)]


class StorageUnit(Enum):
    TB = 'TB'


class NFSOnDeviceServiceConfiguration(BaseModel):
    """
    An object that represents metadata and configuration settings for NFS service on an AWS Snow Family device.
    """

    StorageLimit: Optional[StorageLimit] = None
    StorageUnit: Optional[StorageUnit] = None


class SnsTopicARN(BaseModel):
    __root__: Annotated[
        str, Field(max_length=255, regex='arn:aws.*:sns:.*:[0-9]{12}:.*')
    ]


class Shipment(BaseModel):
    """
    The <code>Status</code> and <code>TrackingNumber</code> information for an inbound or outbound shipment.
    """

    Status: Optional[String] = None
    TrackingNumber: Optional[String] = None


class ShipmentState(Enum):
    RECEIVED = 'RECEIVED'
    RETURNED = 'RETURNED'


class WirelessConnection(BaseModel):
    """
    Configures the wireless connection on an AWS Snowcone device.
    """

    IsWifiEnabled: Optional[Boolean] = None


class TargetOnDeviceService(BaseModel):
    """
    An object that represents the service or services on the Snow Family device that your transferred data will be exported from or imported into. AWS Snow Family supports Amazon S3 and NFS (Network File System).
    """

    ServiceName: Optional[DeviceServiceName] = None
    TransferOption: Optional[JobType] = None


class CancelClusterRequest(BaseModel):
    ClusterId: ClusterId


class CancelJobRequest(BaseModel):
    JobId: JobId


class CreateAddressResult(BaseModel):
    AddressId: Optional[String] = None


class CreateAddressRequest(BaseModel):
    Address: Address


class CreateClusterResult(BaseModel):
    ClusterId: Optional[ClusterId] = None


class CreateJobResult(BaseModel):
    JobId: Optional[JobId] = None


class CreateLongTermPricingResult(BaseModel):
    LongTermPricingId: Optional[LongTermPricingId] = None


class CreateLongTermPricingRequest(BaseModel):
    LongTermPricingType: LongTermPricingType
    IsLongTermPricingAutoRenew: Optional[JavaBoolean] = None
    SnowballType: Optional[SnowballType] = None


class CreateReturnShippingLabelResult(BaseModel):
    Status: Optional[ShippingLabelStatus] = None


class CreateReturnShippingLabelRequest(BaseModel):
    JobId: JobId
    ShippingOption: Optional[ShippingOption] = None


class DescribeAddressResult(BaseModel):
    Address: Optional[Address] = None


class DescribeAddressRequest(BaseModel):
    AddressId: AddressId


class DescribeAddressesResult(BaseModel):
    Addresses: Optional[AddressList] = None
    NextToken: Optional[String] = None


class DescribeAddressesRequest(BaseModel):
    MaxResults: Optional[ListLimit] = None
    NextToken: Optional[String] = None


class DescribeClusterRequest(BaseModel):
    ClusterId: ClusterId


class DescribeJobRequest(BaseModel):
    JobId: JobId


class DescribeReturnShippingLabelResult(BaseModel):
    Status: Optional[ShippingLabelStatus] = None
    ExpirationDate: Optional[Timestamp] = None


class DescribeReturnShippingLabelRequest(BaseModel):
    JobId: JobId


class GetJobManifestResult(BaseModel):
    ManifestURI: Optional[String] = None


class GetJobManifestRequest(BaseModel):
    JobId: JobId


class GetJobUnlockCodeResult(BaseModel):
    UnlockCode: Optional[String] = None


class GetJobUnlockCodeRequest(BaseModel):
    JobId: JobId


class GetSnowballUsageResult(BaseModel):
    SnowballLimit: Optional[Integer] = None
    SnowballsInUse: Optional[Integer] = None


class GetSoftwareUpdatesResult(BaseModel):
    UpdatesURI: Optional[String] = None


class GetSoftwareUpdatesRequest(BaseModel):
    JobId: JobId


class ListClusterJobsResult(BaseModel):
    JobListEntries: Optional[JobListEntryList] = None
    NextToken: Optional[String] = None


class ListClusterJobsRequest(BaseModel):
    ClusterId: ClusterId
    MaxResults: Optional[ListLimit] = None
    NextToken: Optional[String] = None


class ListClustersResult(BaseModel):
    ClusterListEntries: Optional[ClusterListEntryList] = None
    NextToken: Optional[String] = None


class ListClustersRequest(BaseModel):
    MaxResults: Optional[ListLimit] = None
    NextToken: Optional[String] = None


class ListCompatibleImagesResult(BaseModel):
    CompatibleImages: Optional[CompatibleImageList] = None
    NextToken: Optional[String] = None


class ListCompatibleImagesRequest(BaseModel):
    MaxResults: Optional[ListLimit] = None
    NextToken: Optional[String] = None


class ListJobsResult(ListClusterJobsResult):
    pass


class ListJobsRequest(BaseModel):
    MaxResults: Optional[ListLimit] = None
    NextToken: Optional[String] = None


class ListLongTermPricingRequest(BaseModel):
    MaxResults: Optional[ListLimit] = None
    NextToken: Optional[String] = None


class UpdateJobShipmentStateRequest(BaseModel):
    JobId: JobId
    ShipmentState: ShipmentState


class UpdateLongTermPricingRequest(BaseModel):
    LongTermPricingId: LongTermPricingId
    ReplacementJob: Optional[JobId] = None
    IsLongTermPricingAutoRenew: Optional[JavaBoolean] = None


class Notification(BaseModel):
    """
    <p>The Amazon Simple Notification Service (Amazon SNS) notification settings associated with a specific job. The <code>Notification</code> object is returned as a part of the response syntax of the <code>DescribeJob</code> action in the <code>JobMetadata</code> data type.</p> <p>When the notification settings are defined during job creation, you can choose to notify based on a specific set of job states using the <code>JobStatesToNotify</code> array of strings, or you can specify that you want to have Amazon SNS notifications sent out for all job states with <code>NotifyAll</code> set to true.</p>
    """

    SnsTopicARN: Optional[SnsTopicARN] = None
    JobStatesToNotify: Optional[JobStateList] = None
    NotifyAll: Optional[Boolean] = None


class TaxDocuments(BaseModel):
    """
    The tax documents required in your AWS Region.
    """

    IND: Optional[INDTaxDocuments] = None


class OnDeviceServiceConfiguration(BaseModel):
    """
    An object that represents metadata and configuration settings for services on an AWS Snow Family device.
    """

    NFSOnDeviceService: Optional[NFSOnDeviceServiceConfiguration] = None


class SnowconeDeviceConfiguration(BaseModel):
    """
    Specifies the device configuration for an AWS Snowcone job.
    """

    WirelessConnection: Optional[WirelessConnection] = None


class ShippingDetails(BaseModel):
    """
    A job's shipping information, including inbound and outbound tracking numbers and shipping speed options.
    """

    ShippingOption: Optional[ShippingOption] = None
    InboundShipment: Optional[Shipment] = None
    OutboundShipment: Optional[Shipment] = None


class LambdaResourceList(BaseModel):
    __root__: List[LambdaResource]


class LongTermPricingEntryList(BaseModel):
    __root__: List[LongTermPricingListEntry]


class TargetOnDeviceServiceList(BaseModel):
    __root__: List[TargetOnDeviceService]


class S3Resource(BaseModel):
    """
    Each <code>S3Resource</code> object represents an Amazon S3 bucket that your transferred data will be exported from or imported into. For export jobs, this object can have an optional <code>KeyRange</code> value. The length of the range is defined at job creation, and has either an inclusive <code>BeginMarker</code>, an inclusive <code>EndMarker</code>, or both. Ranges are UTF-8 binary sorted.
    """

    BucketArn: Optional[ResourceARN] = None
    KeyRange: Optional[KeyRange] = None
    TargetOnDeviceServices: Optional[TargetOnDeviceServiceList] = None


class ListLongTermPricingResult(BaseModel):
    LongTermPricingEntries: Optional[LongTermPricingEntryList] = None
    NextToken: Optional[String] = None


class DeviceConfiguration(BaseModel):
    """
    The container for <code>SnowconeDeviceConfiguration</code>.
    """

    SnowconeDeviceConfiguration: Optional[SnowconeDeviceConfiguration] = None


class S3ResourceList(BaseModel):
    __root__: List[S3Resource]


class JobResource(BaseModel):
    """
    Contains an array of AWS resource objects. Each object represents an Amazon S3 bucket, an AWS Lambda function, or an Amazon Machine Image (AMI) based on Amazon EC2 that is associated with a particular job.
    """

    S3Resources: Optional[S3ResourceList] = None
    LambdaResources: Optional[LambdaResourceList] = None
    Ec2AmiResources: Optional[Ec2AmiResourceList] = None


class ClusterMetadata(BaseModel):
    """
    Contains metadata about a specific cluster.
    """

    ClusterId: Optional[String] = None
    Description: Optional[String] = None
    KmsKeyARN: Optional[KmsKeyARN] = None
    RoleARN: Optional[RoleARN] = None
    ClusterState: Optional[ClusterState] = None
    JobType: Optional[JobType] = None
    SnowballType: Optional[SnowballType] = None
    CreationDate: Optional[Timestamp] = None
    Resources: Optional[JobResource] = None
    AddressId: Optional[AddressId] = None
    ShippingOption: Optional[ShippingOption] = None
    Notification: Optional[Notification] = None
    ForwardingAddressId: Optional[AddressId] = None
    TaxDocuments: Optional[TaxDocuments] = None
    OnDeviceServiceConfiguration: Optional[OnDeviceServiceConfiguration] = None


class JobMetadata(BaseModel):
    """
    Contains information about a specific job including shipping information, job status, and other important metadata. This information is returned as a part of the response syntax of the <code>DescribeJob</code> action.
    """

    JobId: Optional[String] = None
    JobState: Optional[JobState] = None
    JobType: Optional[JobType] = None
    SnowballType: Optional[SnowballType] = None
    CreationDate: Optional[Timestamp] = None
    Resources: Optional[JobResource] = None
    Description: Optional[String] = None
    KmsKeyARN: Optional[KmsKeyARN] = None
    RoleARN: Optional[RoleARN] = None
    AddressId: Optional[AddressId] = None
    ShippingDetails: Optional[ShippingDetails] = None
    SnowballCapacityPreference: Optional[SnowballCapacity] = None
    Notification: Optional[Notification] = None
    DataTransferProgress: Optional[DataTransfer] = None
    JobLogInfo: Optional[JobLogs] = None
    ClusterId: Optional[String] = None
    ForwardingAddressId: Optional[AddressId] = None
    TaxDocuments: Optional[TaxDocuments] = None
    DeviceConfiguration: Optional[DeviceConfiguration] = None
    RemoteManagement: Optional[RemoteManagement] = None
    LongTermPricingId: Optional[LongTermPricingId] = None
    OnDeviceServiceConfiguration: Optional[OnDeviceServiceConfiguration] = None


class JobMetadataList(BaseModel):
    __root__: List[JobMetadata]


class CreateClusterRequest(BaseModel):
    JobType: JobType
    Resources: JobResource
    OnDeviceServiceConfiguration: Optional[OnDeviceServiceConfiguration] = None
    Description: Optional[String] = None
    AddressId: AddressId
    KmsKeyARN: Optional[KmsKeyARN] = None
    RoleARN: RoleARN
    SnowballType: SnowballType
    ShippingOption: ShippingOption
    Notification: Optional[Notification] = None
    ForwardingAddressId: Optional[AddressId] = None
    TaxDocuments: Optional[TaxDocuments] = None
    RemoteManagement: Optional[RemoteManagement] = None


class CreateJobRequest(BaseModel):
    JobType: Optional[JobType] = None
    Resources: Optional[JobResource] = None
    OnDeviceServiceConfiguration: Optional[OnDeviceServiceConfiguration] = None
    Description: Optional[String] = None
    AddressId: Optional[AddressId] = None
    KmsKeyARN: Optional[KmsKeyARN] = None
    RoleARN: Optional[RoleARN] = None
    SnowballCapacityPreference: Optional[SnowballCapacity] = None
    ShippingOption: Optional[ShippingOption] = None
    Notification: Optional[Notification] = None
    ClusterId: Optional[ClusterId] = None
    SnowballType: Optional[SnowballType] = None
    ForwardingAddressId: Optional[AddressId] = None
    TaxDocuments: Optional[TaxDocuments] = None
    DeviceConfiguration: Optional[DeviceConfiguration] = None
    RemoteManagement: Optional[RemoteManagement] = None
    LongTermPricingId: Optional[LongTermPricingId] = None


class DescribeClusterResult(BaseModel):
    ClusterMetadata: Optional[ClusterMetadata] = None


class DescribeJobResult(BaseModel):
    JobMetadata: Optional[JobMetadata] = None
    SubJobMetadata: Optional[JobMetadataList] = None


class UpdateClusterRequest(BaseModel):
    ClusterId: ClusterId
    RoleARN: Optional[RoleARN] = None
    Description: Optional[String] = None
    Resources: Optional[JobResource] = None
    OnDeviceServiceConfiguration: Optional[OnDeviceServiceConfiguration] = None
    AddressId: Optional[AddressId] = None
    ShippingOption: Optional[ShippingOption] = None
    Notification: Optional[Notification] = None
    ForwardingAddressId: Optional[AddressId] = None


class UpdateJobRequest(BaseModel):
    JobId: JobId
    RoleARN: Optional[RoleARN] = None
    Notification: Optional[Notification] = None
    Resources: Optional[JobResource] = None
    OnDeviceServiceConfiguration: Optional[OnDeviceServiceConfiguration] = None
    AddressId: Optional[AddressId] = None
    ShippingOption: Optional[ShippingOption] = None
    Description: Optional[String] = None
    SnowballCapacityPreference: Optional[SnowballCapacity] = None
    ForwardingAddressId: Optional[AddressId] = None