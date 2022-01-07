# generated by datamodel-codegen:
#   filename:  openapi.yaml
#   timestamp: 2021-12-31T02:50:31+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Annotated, List, Optional

from pydantic import BaseModel, Field


class GenericString(BaseModel):
    __root__: str


class APIVersion(BaseModel):
    __root__: Annotated[
        str, Field(description='Specifies the version of the client tool.')
    ]


class Description(BaseModel):
    __root__: Annotated[
        str, Field(description='The associated description for this object.')
    ]


class URL(BaseModel):
    __root__: Annotated[str, Field(description='The URL for a given Artifact.')]


class Artifact(BaseModel):
    """
    A discrete item that contains the description and URL of an artifact (such as a PDF).
    """

    Description: Optional[Description] = None
    URL: Optional[URL] = None


class ArtifactList(BaseModel):
    """
    A collection of artifacts.
    """

    __root__: Annotated[List[Artifact], Field(description='A collection of artifacts.')]


class ErrorMessage(BaseModel):
    __root__: Annotated[
        str, Field(description='The human-readable description of a particular error.')
    ]


class JobId(BaseModel):
    __root__: Annotated[
        str, Field(description='A unique identifier which refers to a particular job.')
    ]


class CancelJobInput(BaseModel):
    """
    Input structure for the CancelJob operation.
    """

    JobId: JobId
    APIVersion: Optional[APIVersion] = None


class Success(BaseModel):
    __root__: Annotated[
        bool,
        Field(
            description='Specifies whether (true) or not (false) AWS Import/Export updated your job.'
        ),
    ]


class Carrier(BaseModel):
    __root__: Annotated[
        str,
        Field(
            description='Name of the shipping company. This value is included when the LocationCode is "Returned".'
        ),
    ]


class JobType(Enum):
    """
    Specifies whether the job to initiate is an import or export job.
    """

    Import = 'Import'
    Export = 'Export'


class Manifest(BaseModel):
    __root__: Annotated[
        str, Field(description='The UTF-8 encoded text of the manifest file.')
    ]


class ManifestAddendum(BaseModel):
    __root__: Annotated[str, Field(description='For internal use only.')]


class ValidateOnly(BaseModel):
    __root__: Annotated[
        bool,
        Field(
            description='Validate the manifest and parameter values in the request but do not actually create a job.'
        ),
    ]


class CreateJobInput(BaseModel):
    """
    Input structure for the CreateJob operation.
    """

    JobType: JobType
    Manifest: Manifest
    ManifestAddendum: Optional[ManifestAddendum] = None
    ValidateOnly: ValidateOnly
    APIVersion: Optional[APIVersion] = None


class Signature(BaseModel):
    __root__: Annotated[
        str,
        Field(
            description='An encrypted code used to authenticate the request and response, for example, "DV+TpDfx1/TdSE9ktyK9k/bDTVI=". Only use this value is you want to create the signature file yourself. Generally you should use the SignatureFileContents value.'
        ),
    ]


class SignatureFileContents(BaseModel):
    __root__: Annotated[
        str,
        Field(
            description='The actual text of the SIGNATURE file to be written to disk.'
        ),
    ]


class WarningMessage(BaseModel):
    __root__: Annotated[
        str,
        Field(
            description='An optional message notifying you of non-fatal issues with the job, such as use of an incompatible Amazon S3 bucket name.'
        ),
    ]


class CreationDate(BaseModel):
    __root__: Annotated[
        datetime,
        Field(
            description='Timestamp of the CreateJob request in ISO8601 date format. For example "2010-03-28T20:27:35Z".'
        ),
    ]


class CurrentManifest(BaseModel):
    __root__: Annotated[
        str,
        Field(
            description='The last manifest submitted, which will be used to process the job.'
        ),
    ]


class ErrorCount(BaseModel):
    __root__: Annotated[
        int,
        Field(
            description='Number of errors. We return this value when the ProgressCode is Success or SuccessWithErrors.'
        ),
    ]


class JobIdList(BaseModel):
    __root__: List[GenericString]


class Name(BaseModel):
    __root__: Annotated[
        str,
        Field(
            description='Specifies the name of the person responsible for shipping this package.'
        ),
    ]


class Company(BaseModel):
    __root__: Annotated[
        str,
        Field(
            description='Specifies the name of the company that will ship this package.'
        ),
    ]


class PhoneNumber(BaseModel):
    __root__: Annotated[
        str,
        Field(
            description='Specifies the phone number of the person responsible for shipping this package.'
        ),
    ]


class Country(BaseModel):
    __root__: Annotated[
        str,
        Field(description='Specifies the name of your country for the return address.'),
    ]


class StateOrProvince(BaseModel):
    __root__: Annotated[
        str,
        Field(
            description='Specifies the name of your state or your province for the return address.'
        ),
    ]


class City(BaseModel):
    __root__: Annotated[
        str,
        Field(description='Specifies the name of your city for the return address.'),
    ]


class PostalCode(BaseModel):
    __root__: Annotated[
        str, Field(description='Specifies the postal code for the return address.')
    ]


class Street1(BaseModel):
    __root__: Annotated[
        str,
        Field(
            description='Specifies the first part of the street address for the return address, for example 1234 Main Street.'
        ),
    ]


class Street2(BaseModel):
    __root__: Annotated[
        str,
        Field(
            description='Specifies the optional second part of the street address for the return address, for example Suite 100.'
        ),
    ]


class Street3(BaseModel):
    __root__: Annotated[
        str,
        Field(
            description='Specifies the optional third part of the street address for the return address, for example c/o Jane Doe.'
        ),
    ]


class GetShippingLabelInput(BaseModel):
    jobIds: JobIdList
    name: Optional[Name] = None
    company: Optional[Company] = None
    phoneNumber: Optional[PhoneNumber] = None
    country: Optional[Country] = None
    stateOrProvince: Optional[StateOrProvince] = None
    city: Optional[City] = None
    postalCode: Optional[PostalCode] = None
    street1: Optional[Street1] = None
    street2: Optional[Street2] = None
    street3: Optional[Street3] = None
    APIVersion: Optional[APIVersion] = None


class GetStatusInput(BaseModel):
    """
    Input structure for the GetStatus operation.
    """

    JobId: JobId
    APIVersion: Optional[APIVersion] = None


class LocationCode(BaseModel):
    __root__: Annotated[
        str,
        Field(
            description='A token representing the location of the storage device, such as "AtAWS".'
        ),
    ]


class LocationMessage(BaseModel):
    __root__: Annotated[
        str,
        Field(
            description='A more human readable form of the physical location of the storage device.'
        ),
    ]


class ProgressCode(BaseModel):
    __root__: Annotated[
        str,
        Field(
            description='A token representing the state of the job, such as "Started".'
        ),
    ]


class ProgressMessage(BaseModel):
    __root__: Annotated[
        str, Field(description='A more human readable form of the job status.')
    ]


class TrackingNumber(BaseModel):
    __root__: Annotated[
        str,
        Field(
            description='The shipping tracking number assigned by AWS Import/Export to the storage device when it\'s returned to you. We return this value when the LocationCode is "Returned".'
        ),
    ]


class LogBucket(BaseModel):
    __root__: Annotated[str, Field(description='Amazon S3 bucket for user logs.')]


class LogKey(BaseModel):
    __root__: Annotated[
        str, Field(description='The key where the user logs were stored.')
    ]


class IsCanceled(BaseModel):
    __root__: Annotated[
        bool, Field(description='Indicates whether the job was canceled.')
    ]


class IsTruncated(BaseModel):
    __root__: Annotated[
        bool,
        Field(
            description='Indicates whether the list of jobs was truncated. If true, then call ListJobs again using the last JobId element as the marker.'
        ),
    ]


class Job(BaseModel):
    """
    Representation of a job returned by the ListJobs operation.
    """

    JobId: Optional[JobId] = None
    CreationDate: Optional[CreationDate] = None
    IsCanceled: Optional[IsCanceled] = None
    JobType: Optional[JobType] = None


class JobsList(BaseModel):
    """
    A list container for Jobs returned by the ListJobs operation.
    """

    __root__: Annotated[
        List[Job],
        Field(
            description='A list container for Jobs returned by the ListJobs operation.'
        ),
    ]


class MaxJobs(BaseModel):
    __root__: Annotated[
        int,
        Field(
            description='Sets the maximum number of jobs returned in the response. If there are additional jobs that were not returned because MaxJobs was exceeded, the response contains &lt;IsTruncated&gt;true&lt;/IsTruncated&gt;. To return the additional jobs, see Marker.'
        ),
    ]


class Marker(BaseModel):
    __root__: Annotated[
        str,
        Field(
            description='Specifies the JOBID to start after when listing the jobs created with your account. AWS Import/Export lists your jobs in reverse chronological order. See MaxJobs.'
        ),
    ]


class ListJobsInput(BaseModel):
    """
    Input structure for the ListJobs operation.
    """

    MaxJobs: Optional[MaxJobs] = None
    Marker: Optional[Marker] = None
    APIVersion: Optional[APIVersion] = None


class UpdateJobInput(BaseModel):
    """
    Input structure for the UpateJob operation.
    """

    JobId: JobId
    Manifest: Manifest
    JobType: JobType
    ValidateOnly: ValidateOnly
    APIVersion: Optional[APIVersion] = None


class CancelJobOutput(BaseModel):
    """
    Output structure for the CancelJob operation.
    """

    Success: Optional[Success] = None


class InvalidJobIdException(BaseModel):
    """
    The JOBID was missing, not found, or not associated with the AWS account.
    """

    message: Optional[ErrorMessage] = None


class ExpiredJobIdException(InvalidJobIdException):
    """
    Indicates that the specified job has expired out of the system.
    """

    pass


class CanceledJobIdException(InvalidJobIdException):
    """
    The specified job ID has been canceled and is no longer valid.
    """

    pass


class UnableToCancelJobIdException(InvalidJobIdException):
    """
    AWS Import/Export cannot cancel the job
    """

    pass


class InvalidAccessKeyIdException(InvalidJobIdException):
    """
    The AWS Access Key ID specified in the request did not match the manifest's accessKeyId value. The manifest and the request authentication must use the same AWS Access Key ID.
    """

    pass


class InvalidVersionException(InvalidJobIdException):
    """
    The client tool version is invalid.
    """

    pass


class CreateJobOutput(BaseModel):
    """
    Output structure for the CreateJob operation.
    """

    JobId: Optional[JobId] = None
    JobType: Optional[JobType] = None
    Signature: Optional[Signature] = None
    SignatureFileContents: Optional[SignatureFileContents] = None
    WarningMessage: Optional[WarningMessage] = None
    ArtifactList: Optional[ArtifactList] = None


class MissingParameterException(InvalidJobIdException):
    """
    One or more required parameters was missing from the request.
    """

    pass


class InvalidParameterException(InvalidJobIdException):
    """
    One or more parameters had an invalid value.
    """

    pass


class InvalidAddressException(InvalidJobIdException):
    """
    The address specified in the manifest is invalid.
    """

    pass


class InvalidManifestFieldException(InvalidJobIdException):
    """
    One or more manifest fields was invalid. Please correct and resubmit.
    """

    pass


class MissingManifestFieldException(InvalidJobIdException):
    """
    One or more required fields were missing from the manifest file. Please correct and resubmit.
    """

    pass


class NoSuchBucketException(InvalidJobIdException):
    """
    The specified bucket does not exist. Create the specified bucket or change the manifest's bucket, exportBucket, or logBucket field to a bucket that the account, as specified by the manifest's Access Key ID, has write permissions to.
    """

    pass


class MissingCustomsException(InvalidJobIdException):
    """
    One or more required customs parameters was missing from the manifest.
    """

    pass


class InvalidCustomsException(InvalidJobIdException):
    """
    One or more customs parameters was invalid. Please correct and resubmit.
    """

    pass


class InvalidFileSystemException(InvalidJobIdException):
    """
    File system specified in export manifest is invalid.
    """

    pass


class MultipleRegionsException(InvalidJobIdException):
    """
    Your manifest file contained buckets from multiple regions. A job is restricted to buckets from one region. Please correct and resubmit.
    """

    pass


class BucketPermissionException(InvalidJobIdException):
    """
    The account specified does not have the appropriate bucket permissions.
    """

    pass


class MalformedManifestException(InvalidJobIdException):
    """
    Your manifest is not well-formed.
    """

    pass


class CreateJobQuotaExceededException(InvalidJobIdException):
    """
    Each account can create only a certain number of jobs per day. If you need to create more than this, please contact awsimportexport@amazon.com to explain your particular use case.
    """

    pass


class GetShippingLabelOutput(BaseModel):
    ShippingLabelURL: Optional[GenericString] = None
    Warning: Optional[GenericString] = None


class GetStatusOutput(BaseModel):
    """
    Output structure for the GetStatus operation.
    """

    JobId: Optional[JobId] = None
    JobType: Optional[JobType] = None
    LocationCode: Optional[LocationCode] = None
    LocationMessage: Optional[LocationMessage] = None
    ProgressCode: Optional[ProgressCode] = None
    ProgressMessage: Optional[ProgressMessage] = None
    Carrier: Optional[Carrier] = None
    TrackingNumber: Optional[TrackingNumber] = None
    LogBucket: Optional[LogBucket] = None
    LogKey: Optional[LogKey] = None
    ErrorCount: Optional[ErrorCount] = None
    Signature: Optional[Signature] = None
    SignatureFileContents: Optional[Signature] = None
    CurrentManifest: Optional[CurrentManifest] = None
    CreationDate: Optional[CreationDate] = None
    ArtifactList: Optional[ArtifactList] = None


class ListJobsOutput(BaseModel):
    """
    Output structure for the ListJobs operation.
    """

    Jobs: Optional[JobsList] = None
    IsTruncated: Optional[IsTruncated] = None


class UpdateJobOutput(BaseModel):
    """
    Output structure for the UpateJob operation.
    """

    Success: Optional[Success] = None
    WarningMessage: Optional[WarningMessage] = None
    ArtifactList: Optional[ArtifactList] = None


class UnableToUpdateJobIdException(InvalidJobIdException):
    """
    AWS Import/Export cannot update the job
    """

    pass