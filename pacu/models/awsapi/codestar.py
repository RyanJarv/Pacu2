# generated by datamodel-codegen:
#   filename:  openapi.yaml
#   timestamp: 2021-12-31T02:46:38+00:00

from __future__ import annotations

from datetime import datetime
from typing import Annotated, Any, List, Optional

from pydantic import BaseModel, Extra, Field, SecretStr


class LimitExceededException(BaseModel):
    __root__: Any


class ProjectNotFoundException(LimitExceededException):
    pass


class TeamMemberAlreadyAssociatedException(LimitExceededException):
    pass


class ValidationException(LimitExceededException):
    pass


class InvalidServiceRoleException(LimitExceededException):
    pass


class ProjectConfigurationException(LimitExceededException):
    pass


class ConcurrentModificationException(LimitExceededException):
    pass


class ProjectAlreadyExistsException(LimitExceededException):
    pass


class ProjectCreationFailedException(LimitExceededException):
    pass


class UserProfileAlreadyExistsException(LimitExceededException):
    pass


class UserProfileNotFoundException(LimitExceededException):
    pass


class DisassociateTeamMemberResult(BaseModel):
    pass


class InvalidNextTokenException(LimitExceededException):
    pass


class UntagProjectResult(DisassociateTeamMemberResult):
    pass


class UpdateProjectResult(DisassociateTeamMemberResult):
    pass


class TeamMemberNotFoundException(LimitExceededException):
    pass


class ProjectId(BaseModel):
    __root__: Annotated[
        str, Field(max_length=15, min_length=2, regex='^[a-z][a-z0-9-]+$')
    ]


class ClientRequestToken(BaseModel):
    __root__: Annotated[str, Field(max_length=256, min_length=1, regex='^[\\w:/-]+$')]


class UserArn(BaseModel):
    __root__: Annotated[
        str,
        Field(
            max_length=95,
            min_length=32,
            regex='^arn:aws:iam::\\d{12}:user(?:(\\u002F)|(\\u002F[\\u0021-\\u007E]+\\u002F))[\\w+=,.@-]+$',
        ),
    ]


class Role(BaseModel):
    __root__: Annotated[str, Field(regex='^(Owner|Viewer|Contributor)$')]


class RemoteAccessAllowed(BaseModel):
    __root__: bool


class BucketKey(BaseModel):
    __root__: str


class BucketName(BaseModel):
    __root__: Annotated[str, Field(max_length=63, min_length=3)]


class RepositoryName(BaseModel):
    __root__: Annotated[str, Field(max_length=100, min_length=1, regex='^\\S[\\w.-]*$')]


class CodeCommitCodeDestination(BaseModel):
    """
    Information about the AWS CodeCommit repository to be created in AWS CodeStar. This is where the source code files provided with the project request will be uploaded after project creation.
    """

    name: RepositoryName


class S3Location(BaseModel):
    """
    The Amazon S3 location where the source code files provided with the project request are stored.
    """

    bucketName: Optional[BucketName] = None
    bucketKey: Optional[BucketKey] = None


class ProjectName(BaseModel):
    __root__: Annotated[
        SecretStr, Field(max_length=100, min_length=1, regex='^\\S(.*\\S)?$')
    ]


class ProjectDescription(BaseModel):
    __root__: Annotated[SecretStr, Field(max_length=1024, regex='^$|^\\S(.*\\S)?$')]


class Tags(BaseModel):
    pass

    class Config:
        extra = Extra.allow


class ProjectArn(BaseModel):
    __root__: Annotated[
        str,
        Field(
            regex='^arn:aws[^:\\s]*:codestar:[^:\\s]+:[0-9]{12}:project\\/[a-z]([a-z0-9|-])+$'
        ),
    ]


class ProjectTemplateId(BaseModel):
    __root__: Annotated[
        str,
        Field(
            min_length=1,
            regex='^arn:aws[^:\\s]{0,5}:codestar:[^:\\s]+::project-template(\\/(github|codecommit))?\\/[a-z0-9-]+$',
        ),
    ]


class UserProfileDisplayName(BaseModel):
    __root__: Annotated[
        SecretStr, Field(max_length=64, min_length=1, regex='^\\S(.*\\S)?$')
    ]


class Email(BaseModel):
    __root__: Annotated[
        SecretStr, Field(max_length=128, min_length=3, regex='^[\\w-.+]+@[\\w-.+]+$')
    ]


class SshPublicKey(BaseModel):
    __root__: Annotated[
        str, Field(max_length=16384, regex='^[\\t\\r\\n\\u0020-\\u00FF]*$')
    ]


class CreatedTimestamp(BaseModel):
    __root__: datetime


class LastModifiedTimestamp(CreatedTimestamp):
    pass


class DeleteStack(RemoteAccessAllowed):
    pass


class StackId(BaseModel):
    __root__: Annotated[
        str,
        Field(
            regex='^arn:aws[^:\\s]*:cloudformation:[^:\\s]+:[0-9]{12}:stack\\/[^:\\s]+\\/[^:\\s]+$'
        ),
    ]


class RepositoryDescription(BaseModel):
    __root__: Annotated[
        str, Field(max_length=1000, min_length=1, regex='^\\S(.*\\S)?$')
    ]


class RepositoryType(BaseModel):
    __root__: Annotated[str, Field(regex='^(user|organization|User|Organization)$')]


class RepositoryOwner(BaseModel):
    __root__: Annotated[str, Field(max_length=100, min_length=1, regex='^\\S(.*\\S)?$')]


class RepositoryIsPrivate(RemoteAccessAllowed):
    pass


class RepositoryEnableIssues(RemoteAccessAllowed):
    pass


class GitHubPersonalToken(BaseModel):
    __root__: Annotated[SecretStr, Field(min_length=1)]


class PaginationToken(BaseModel):
    __root__: Annotated[str, Field(max_length=512, min_length=1, regex='^[\\w/+=]+$')]


class MaxResults(BaseModel):
    __root__: Annotated[int, Field(ge=1.0, le=100.0)]


class State(BaseModel):
    __root__: Annotated[
        str,
        Field(
            regex='^(CreateInProgress|CreateComplete|CreateFailed|DeleteComplete|DeleteFailed|DeleteInProgress|UpdateComplete|UpdateInProgress|UpdateFailed|Unknown)$'
        ),
    ]


class Reason(BaseModel):
    __root__: Annotated[str, Field(max_length=1024, regex='^$|^\\S(.*\\S)?$')]


class ProjectSummary(BaseModel):
    """
    Information about the metadata for a project.
    """

    projectId: Optional[ProjectId] = None
    projectArn: Optional[ProjectArn] = None


class ResourceId(BaseModel):
    __root__: Annotated[str, Field(min_length=11, regex='^arn\\:aws\\:\\S.*\\:.*')]


class Resource(BaseModel):
    """
    Information about a resource for a project.
    """

    id: ResourceId


class RoleArn(BaseModel):
    __root__: Annotated[str, Field(max_length=1224, min_length=1)]


class TagKey(BaseModel):
    __root__: Annotated[
        str,
        Field(
            max_length=128, min_length=1, regex='^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-@]*)$'
        ),
    ]


class TagKeys(BaseModel):
    __root__: List[TagKey]


class TagValue(BaseModel):
    __root__: Annotated[
        str, Field(max_length=256, regex='^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-@]*)$')
    ]


class TeamMember(BaseModel):
    """
    Information about a team member in a project.
    """

    userArn: UserArn
    projectRole: Role
    remoteAccessAllowed: Optional[RemoteAccessAllowed] = None


class TemplateParameterKey(BaseModel):
    __root__: Annotated[str, Field(max_length=30, min_length=1, regex='^\\S(.*\\S)?$')]


class TemplateParameterValue(ProjectName):
    pass


class TemplateParameterMap(BaseModel):
    pass

    class Config:
        extra = Extra.allow


class ToolchainSource(BaseModel):
    """
    The Amazon S3 location where the toolchain template file provided with the project request is stored. AWS CodeStar retrieves the file during project creation.
    """

    s3: S3Location


class UserProfileSummary(BaseModel):
    """
    Information about a user's profile in AWS CodeStar.
    """

    userArn: Optional[UserArn] = None
    displayName: Optional[UserProfileDisplayName] = None
    emailAddress: Optional[Email] = None
    sshPublicKey: Optional[SshPublicKey] = None


class AssociateTeamMemberResult(BaseModel):
    clientRequestToken: Optional[ClientRequestToken] = None


class AssociateTeamMemberRequest(BaseModel):
    projectId: ProjectId
    clientRequestToken: Optional[ClientRequestToken] = None
    userArn: UserArn
    projectRole: Role
    remoteAccessAllowed: Optional[RemoteAccessAllowed] = None


class CreateProjectResult(BaseModel):
    id: ProjectId
    arn: ProjectArn
    clientRequestToken: Optional[ClientRequestToken] = None
    projectTemplateId: Optional[ProjectTemplateId] = None


class CreateUserProfileResult(BaseModel):
    userArn: UserArn
    displayName: Optional[UserProfileDisplayName] = None
    emailAddress: Optional[Email] = None
    sshPublicKey: Optional[SshPublicKey] = None
    createdTimestamp: Optional[CreatedTimestamp] = None
    lastModifiedTimestamp: Optional[LastModifiedTimestamp] = None


class CreateUserProfileRequest(BaseModel):
    userArn: UserArn
    displayName: UserProfileDisplayName
    emailAddress: Email
    sshPublicKey: Optional[SshPublicKey] = None


class DeleteProjectResult(BaseModel):
    stackId: Optional[StackId] = None
    projectArn: Optional[ProjectArn] = None


class DeleteProjectRequest(BaseModel):
    id: ProjectId
    clientRequestToken: Optional[ClientRequestToken] = None
    deleteStack: Optional[DeleteStack] = None


class DeleteUserProfileResult(BaseModel):
    userArn: UserArn


class DeleteUserProfileRequest(BaseModel):
    userArn: UserArn


class DescribeProjectRequest(BaseModel):
    id: ProjectId


class DescribeUserProfileResult(BaseModel):
    userArn: UserArn
    displayName: Optional[UserProfileDisplayName] = None
    emailAddress: Optional[Email] = None
    sshPublicKey: Optional[SshPublicKey] = None
    createdTimestamp: CreatedTimestamp
    lastModifiedTimestamp: LastModifiedTimestamp


class DescribeUserProfileRequest(BaseModel):
    userArn: UserArn


class DisassociateTeamMemberRequest(BaseModel):
    projectId: ProjectId
    userArn: UserArn


class ListProjectsRequest(BaseModel):
    nextToken: Optional[PaginationToken] = None
    maxResults: Optional[MaxResults] = None


class ListResourcesRequest(BaseModel):
    projectId: ProjectId
    nextToken: Optional[PaginationToken] = None
    maxResults: Optional[MaxResults] = None


class ListTagsForProjectResult(BaseModel):
    tags: Optional[Tags] = None
    nextToken: Optional[PaginationToken] = None


class ListTagsForProjectRequest(BaseModel):
    id: ProjectId
    nextToken: Optional[PaginationToken] = None
    maxResults: Optional[MaxResults] = None


class ListTeamMembersRequest(BaseModel):
    projectId: ProjectId
    nextToken: Optional[PaginationToken] = None
    maxResults: Optional[MaxResults] = None


class ListUserProfilesRequest(BaseModel):
    nextToken: Optional[PaginationToken] = None
    maxResults: Optional[MaxResults] = None


class TagProjectResult(BaseModel):
    tags: Optional[Tags] = None


class TagProjectRequest(BaseModel):
    id: ProjectId
    tags: Tags


class UntagProjectRequest(BaseModel):
    id: ProjectId
    tags: TagKeys


class UpdateProjectRequest(BaseModel):
    id: ProjectId
    name: Optional[ProjectName] = None
    description: Optional[ProjectDescription] = None


class UpdateTeamMemberResult(BaseModel):
    userArn: Optional[UserArn] = None
    projectRole: Optional[Role] = None
    remoteAccessAllowed: Optional[RemoteAccessAllowed] = None


class UpdateTeamMemberRequest(BaseModel):
    projectId: ProjectId
    userArn: UserArn
    projectRole: Optional[Role] = None
    remoteAccessAllowed: Optional[RemoteAccessAllowed] = None


class UpdateUserProfileResult(CreateUserProfileResult):
    pass


class UpdateUserProfileRequest(BaseModel):
    userArn: UserArn
    displayName: Optional[UserProfileDisplayName] = None
    emailAddress: Optional[Email] = None
    sshPublicKey: Optional[SshPublicKey] = None


class CodeSource(ToolchainSource):
    """
    The location where the source code files provided with the project request are stored. AWS CodeStar retrieves the files during project creation.
    """

    pass


class GitHubCodeDestination(BaseModel):
    """
    Information about the GitHub repository to be created in AWS CodeStar. This is where the source code files provided with the project request will be uploaded after project creation.
    """

    name: RepositoryName
    description: Optional[RepositoryDescription] = None
    type: RepositoryType
    owner: RepositoryOwner
    privateRepository: RepositoryIsPrivate
    issuesEnabled: RepositoryEnableIssues
    token: GitHubPersonalToken


class Toolchain(BaseModel):
    """
    The toolchain template file provided with the project request. AWS CodeStar uses the template to provision the toolchain stack in AWS CloudFormation.
    """

    source: ToolchainSource
    roleArn: Optional[RoleArn] = None
    stackParameters: Optional[TemplateParameterMap] = None


class ProjectStatus(BaseModel):
    """
    An indication of whether a project creation or deletion is failed or successful.
    """

    state: State
    reason: Optional[Reason] = None


class ProjectsList(BaseModel):
    __root__: List[ProjectSummary]


class ResourcesResult(BaseModel):
    __root__: List[Resource]


class TeamMemberResult(BaseModel):
    __root__: List[TeamMember]


class UserProfilesList(BaseModel):
    __root__: List[UserProfileSummary]


class DescribeProjectResult(BaseModel):
    name: Optional[ProjectName] = None
    id: Optional[ProjectId] = None
    arn: Optional[ProjectArn] = None
    description: Optional[ProjectDescription] = None
    clientRequestToken: Optional[ClientRequestToken] = None
    createdTimeStamp: Optional[CreatedTimestamp] = None
    stackId: Optional[StackId] = None
    projectTemplateId: Optional[ProjectTemplateId] = None
    status: Optional[ProjectStatus] = None


class ListProjectsResult(BaseModel):
    projects: ProjectsList
    nextToken: Optional[PaginationToken] = None


class ListResourcesResult(BaseModel):
    resources: Optional[ResourcesResult] = None
    nextToken: Optional[PaginationToken] = None


class ListTeamMembersResult(BaseModel):
    teamMembers: TeamMemberResult
    nextToken: Optional[PaginationToken] = None


class ListUserProfilesResult(BaseModel):
    userProfiles: UserProfilesList
    nextToken: Optional[PaginationToken] = None


class CodeDestination(BaseModel):
    """
    The repository to be created in AWS CodeStar. Valid values are AWS CodeCommit or GitHub. After AWS CodeStar provisions the new repository, the source code files provided with the project request are placed in the repository.
    """

    codeCommit: Optional[CodeCommitCodeDestination] = None
    gitHub: Optional[GitHubCodeDestination] = None


class Code(BaseModel):
    """
    Location and destination information about the source code files provided with the project request. The source code is uploaded to the new project source repository after project creation.
    """

    source: CodeSource
    destination: CodeDestination


class SourceCode(BaseModel):
    __root__: List[Code]


class CreateProjectRequest(BaseModel):
    name: ProjectName
    id: ProjectId
    description: Optional[ProjectDescription] = None
    clientRequestToken: Optional[ClientRequestToken] = None
    sourceCode: Optional[SourceCode] = None
    toolchain: Optional[Toolchain] = None
    tags: Optional[Tags] = None