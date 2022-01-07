# generated by datamodel-codegen:
#   filename:  openapi.yaml
#   timestamp: 2021-12-31T02:46:31+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Annotated, Any, List, Optional

from pydantic import BaseModel, Extra, Field


class TagValue(BaseModel):
    __root__: Annotated[str, Field(max_length=256)]


class KMSKeyId(BaseModel):
    __root__: Annotated[
        str, Field(max_length=2048, min_length=1, regex='[a-zA-Z0-9-]+')
    ]


class EncryptionOption(Enum):
    AWS_OWNED_CMK = 'AWS_OWNED_CMK'
    CUSTOMER_MANAGED_CMK = 'CUSTOMER_MANAGED_CMK'


class InternalServerException(BaseModel):
    __root__: Any


class ValidationException(InternalServerException):
    pass


class AccessDeniedException(InternalServerException):
    pass


class ConflictException(InternalServerException):
    pass


class ThrottlingException(InternalServerException):
    pass


class ResourceNotFoundException(InternalServerException):
    pass


class NotFoundException(InternalServerException):
    pass


class ProviderType(Enum):
    CodeCommit = 'CodeCommit'
    GitHub = 'GitHub'
    Bitbucket = 'Bitbucket'
    GitHubEnterpriseServer = 'GitHubEnterpriseServer'
    S3Bucket = 'S3Bucket'


class JobState(Enum):
    Completed = 'Completed'
    Pending = 'Pending'
    Failed = 'Failed'
    Deleting = 'Deleting'


class Name(BaseModel):
    __root__: Annotated[str, Field(max_length=100, min_length=1, regex='^\\S[\\w.-]*$')]


class UserId(BaseModel):
    __root__: Annotated[str, Field(max_length=256, min_length=1)]


class RecommendationId(BaseModel):
    __root__: Annotated[str, Field(max_length=64, min_length=1)]


class RepositoryAssociationState(Enum):
    Associated = 'Associated'
    Associating = 'Associating'
    Failed = 'Failed'
    Disassociating = 'Disassociating'
    Disassociated = 'Disassociated'


class Owner(BaseModel):
    __root__: Annotated[str, Field(max_length=100, min_length=1, regex='^\\S(.*\\S)?$')]


class PutRecommendationFeedbackResponse(BaseModel):
    pass


class Reaction(Enum):
    ThumbsUp = 'ThumbsUp'
    ThumbsDown = 'ThumbsDown'


class TagResourceResponse(PutRecommendationFeedbackResponse):
    pass


class UntagResourceResponse(PutRecommendationFeedbackResponse):
    pass


class TagKey(BaseModel):
    __root__: Annotated[str, Field(max_length=128, min_length=1)]


class AnalysisType(Enum):
    Security = 'Security'
    CodeQuality = 'CodeQuality'


class Arn(BaseModel):
    __root__: Annotated[
        str,
        Field(
            max_length=1600,
            min_length=1,
            regex='^arn:aws[^:\\s]*:codeguru-reviewer:[^:\\s]+:[\\d]{12}:[a-z-]+:[\\w-]+$',
        ),
    ]


class ClientRequestToken(BaseModel):
    __root__: Annotated[str, Field(max_length=64, min_length=1, regex='^[\\w-]+$')]


class TagMap(BaseModel):
    pass

    class Config:
        extra = Extra.allow


class KMSKeyDetails(BaseModel):
    """
    <p>An object that contains:</p> <ul> <li> <p>The encryption option for a repository association. It is either owned by Amazon Web Services Key Management Service (KMS) (<code>AWS_OWNED_CMK</code>) or customer managed (<code>CUSTOMER_MANAGED_CMK</code>).</p> </li> <li> <p>The ID of the Amazon Web Services KMS key that is associated with a respository association.</p> </li> </ul>
    """

    KMSKeyId: Optional[KMSKeyId] = None
    EncryptionOption: Optional[EncryptionOption] = None


class AssociationArn1(BaseModel):
    __root__: Annotated[
        str,
        Field(
            max_length=1600,
            min_length=1,
            regex='^arn:aws[^:\\s]*:codeguru-reviewer:[^:\\s]+:[\\d]{12}:association:[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$',
        ),
    ]


class AssociationId(RecommendationId):
    pass


class BranchName(UserId):
    pass


class BranchDiffSourceCodeType(BaseModel):
    """
    A type of <a href="https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_SourceCodeType"> <code>SourceCodeType</code> </a> that specifies a code diff between a source and destination branch in an associated repository.
    """

    SourceBranchName: BranchName
    DestinationBranchName: BranchName


class BuildArtifactsObjectKey(BaseModel):
    __root__: Annotated[
        str, Field(max_length=1024, min_length=1, regex='^\\S(.*\\S)?$')
    ]


class SourceCodeArtifactsObjectKey(BuildArtifactsObjectKey):
    pass


class CodeArtifacts(BaseModel):
    """
    <p>Code artifacts are source code artifacts and build artifacts used in a repository analysis or a pull request review.</p> <ul> <li> <p>Source code artifacts are source code files in a Git repository that are compressed into a .zip file.</p> </li> <li> <p>Build artifacts are .jar or .class files that are compressed in a .zip file.</p> </li> </ul>
    """

    SourceCodeArtifactsObjectKey: SourceCodeArtifactsObjectKey
    BuildArtifactsObjectKey: Optional[BuildArtifactsObjectKey] = None


class StateReason(BaseModel):
    __root__: Annotated[str, Field(max_length=256, min_length=0)]


class TimeStamp(BaseModel):
    __root__: datetime


class Type(Enum):
    PullRequest = 'PullRequest'
    RepositoryAnalysis = 'RepositoryAnalysis'


class PullRequestId(RecommendationId):
    pass


class CodeReviewName(BaseModel):
    __root__: Annotated[
        str, Field(max_length=100, min_length=1, regex='[a-zA-Z0-9-_]*')
    ]


class CommitId(BaseModel):
    __root__: Annotated[str, Field(max_length=64, min_length=6)]


class CommitDiffSourceCodeType(BaseModel):
    """
    A type of <a href="https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_SourceCodeType"> <code>SourceCodeType</code> </a> that specifies the commit diff for a pull request on an associated repository. The <code>SourceCommit</code> and <code>DestinationCommit</code> fields are required to do a pull request code review.
    """

    SourceCommit: Optional[CommitId] = None
    DestinationCommit: Optional[CommitId] = None
    MergeBaseCommit: Optional[CommitId] = None


class ConnectionArn(BaseModel):
    __root__: Annotated[
        str,
        Field(
            max_length=256, min_length=0, regex='arn:aws(-[\\w]+)*:.+:.+:[0-9]{12}:.+'
        ),
    ]


class DescribeCodeReviewRequest(BaseModel):
    pass


class DescribeRecommendationFeedbackRequest(BaseModel):
    pass


class DescribeRepositoryAssociationRequest(BaseModel):
    pass


class DisassociateRepositoryRequest(BaseModel):
    pass


class EventName(BaseModel):
    __root__: Annotated[
        str, Field(max_length=32, min_length=1, regex='^[ \\-A-Z_a-z]+$')
    ]


class EventState(EventName):
    pass


class EventInfo(BaseModel):
    """
    Information about an event. The event might be a push, pull request, scheduled request, or another type of event.
    """

    Name: Optional[EventName] = None
    State: Optional[EventState] = None


class FilePath(BaseModel):
    __root__: Annotated[str, Field(max_length=1024, min_length=1)]


class FindingsCount(BaseModel):
    __root__: int


class JobStates(BaseModel):
    __root__: Annotated[List[JobState], Field(max_items=3, min_items=1)]


class LineNumber(FindingsCount):
    pass


class ListCodeReviewsMaxResults(BaseModel):
    __root__: Annotated[int, Field(ge=1.0, le=100.0)]


class ProviderTypes(BaseModel):
    __root__: Annotated[List[ProviderType], Field(max_items=3, min_items=1)]


class RepositoryNames(BaseModel):
    __root__: Annotated[List[Name], Field(max_items=100, min_items=1)]


class NextToken(BaseModel):
    __root__: Annotated[str, Field(max_length=2048, min_length=1)]


class ListCodeReviewsRequest(BaseModel):
    pass


class MaxResults(ListCodeReviewsMaxResults):
    pass


class UserIds(BaseModel):
    __root__: Annotated[List[UserId], Field(max_items=100, min_items=1)]


class RecommendationIds(BaseModel):
    __root__: Annotated[List[RecommendationId], Field(max_items=100, min_items=1)]


class ListRecommendationFeedbackRequest(BaseModel):
    pass


class ListRecommendationsRequest(BaseModel):
    pass


class RepositoryAssociationStates(BaseModel):
    __root__: Annotated[
        List[RepositoryAssociationState], Field(max_items=5, min_items=1)
    ]


class Names(BaseModel):
    __root__: Annotated[List[Name], Field(max_items=3, min_items=1)]


class Owners(BaseModel):
    __root__: Annotated[List[Owner], Field(max_items=3, min_items=1)]


class ListRepositoryAssociationsRequest(BaseModel):
    pass


class ListTagsForResourceRequest(BaseModel):
    pass


class LongDescription(BaseModel):
    __root__: Annotated[
        str, Field(max_length=1000, min_length=1, regex='^\\S(.*\\S)?$')
    ]


class MeteredLinesOfCodeCount(FindingsCount):
    pass


class Reactions(BaseModel):
    __root__: Annotated[List[Reaction], Field(max_items=1, min_items=0)]


class PutRecommendationFeedbackRequest(BaseModel):
    CodeReviewArn: Arn
    RecommendationId: RecommendationId
    Reactions: Reactions


class RecommendationCategory(Enum):
    AWSBestPractices = 'AWSBestPractices'
    AWSCloudFormationIssues = 'AWSCloudFormationIssues'
    DuplicateCode = 'DuplicateCode'
    CodeMaintenanceIssues = 'CodeMaintenanceIssues'
    ConcurrencyIssues = 'ConcurrencyIssues'
    InputValidations = 'InputValidations'
    PythonBestPractices = 'PythonBestPractices'
    JavaBestPractices = 'JavaBestPractices'
    ResourceLeaks = 'ResourceLeaks'
    SecurityIssues = 'SecurityIssues'
    CodeInconsistencies = 'CodeInconsistencies'


class RecommendationFeedbackSummary(BaseModel):
    """
    Information about recommendation feedback summaries.
    """

    RecommendationId: Optional[RecommendationId] = None
    Reactions: Optional[Reactions] = None
    UserId: Optional[UserId] = None


class Text(NextToken):
    pass


class Severity(Enum):
    Info = 'Info'
    Low = 'Low'
    Medium = 'Medium'
    High = 'High'
    Critical = 'Critical'


class RepositoryHeadSourceCodeType(BaseModel):
    """
    A <a href="https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_SourceCodeType"> <code>SourceCodeType</code> </a> that specifies the tip of a branch in an associated repository.
    """

    BranchName: BranchName


class RepositoryAssociationSummary(BaseModel):
    """
    Summary information about a repository association. The <a href="https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_ListRepositoryAssociations.html"> <code>ListRepositoryAssociations</code> </a> operation returns a list of <code>RepositoryAssociationSummary</code> objects.
    """

    AssociationArn: Optional[Arn] = None
    ConnectionArn: Optional[ConnectionArn] = None
    LastUpdatedTimeStamp: Optional[TimeStamp] = None
    AssociationId: Optional[AssociationId] = None
    Name: Optional[Name] = None
    Owner: Optional[Owner] = None
    ProviderType: Optional[ProviderType] = None
    State: Optional[RepositoryAssociationState] = None


class RequestId(RecommendationId):
    pass


class Requester(Owner):
    pass


class VendorName(Enum):
    GitHub = 'GitHub'
    GitLab = 'GitLab'
    NativeS3 = 'NativeS3'


class RequestMetadata(BaseModel):
    """
    Metadata that is associated with a code review. This applies to both pull request and repository analysis code reviews.
    """

    RequestId: Optional[RequestId] = None
    Requester: Optional[Requester] = None
    EventInfo: Optional[EventInfo] = None
    VendorName: Optional[VendorName] = None


class RuleId(BaseModel):
    __root__: Annotated[
        str,
        Field(max_length=64, min_length=1, regex='^\\S+\\/[a-zA-Z0-9-]+@v\\d+\\.\\d+$'),
    ]


class RuleName(Owner):
    pass


class ShortDescription(BaseModel):
    __root__: Annotated[str, Field(max_length=200, min_length=1, regex='^\\S(.*\\S)?$')]


class RuleTag(BaseModel):
    __root__: Annotated[str, Field(max_length=50, min_length=1, regex='^\\S(.*\\S)?$')]


class S3BucketName(BaseModel):
    __root__: Annotated[str, Field(max_length=63, min_length=3, regex='^\\S(.*\\S)?$')]


class TagKeyList(BaseModel):
    __root__: Annotated[List[TagKey], Field(max_items=50, min_items=1)]


class TagResourceRequest(BaseModel):
    Tags: TagMap


class UntagResourceRequest(BaseModel):
    pass


class CodeCommitRepository(BaseModel):
    """
    Information about an Amazon Web Services CodeCommit repository. The CodeCommit repository must be in the same Amazon Web Services Region and Amazon Web Services account where its CodeGuru Reviewer code reviews are configured.
    """

    Name: Name


class ThirdPartySourceRepository(BaseModel):
    """
    Information about a third-party source repository connected to CodeGuru Reviewer.
    """

    Name: Name
    ConnectionArn: ConnectionArn
    Owner: Owner


class S3Repository(BaseModel):
    """
    Information about a repository in an S3 bucket.
    """

    Name: Name
    BucketName: S3BucketName


class AnalysisTypes(BaseModel):
    __root__: List[AnalysisType]


class ListTagsForResourceResponse(BaseModel):
    Tags: Optional[TagMap] = None


class Repository(BaseModel):
    """
    Information about an associated Amazon Web Services CodeCommit repository or an associated repository that is managed by Amazon Web Services CodeStar Connections (for example, Bitbucket). This <code>Repository</code> object is not used if your source code is in an associated GitHub repository.
    """

    CodeCommit: Optional[CodeCommitRepository] = None
    Bitbucket: Optional[ThirdPartySourceRepository] = None
    GitHubEnterpriseServer: Optional[ThirdPartySourceRepository] = None
    S3Bucket: Optional[S3Repository] = None


class AssociateRepositoryRequest(BaseModel):
    Repository: Repository
    ClientRequestToken: Optional[ClientRequestToken] = None
    Tags: Optional[TagMap] = None
    KMSKeyDetails: Optional[KMSKeyDetails] = None


class Metrics(BaseModel):
    """
    Information about the statistics from the code review.
    """

    MeteredLinesOfCodeCount: Optional[MeteredLinesOfCodeCount] = None
    FindingsCount: Optional[FindingsCount] = None


class MetricsSummary(Metrics):
    """
    Information about metrics summaries.
    """

    pass


class RecommendationFeedback(BaseModel):
    """
    Information about the recommendation feedback.
    """

    CodeReviewArn: Optional[Arn] = None
    RecommendationId: Optional[RecommendationId] = None
    Reactions: Optional[Reactions] = None
    UserId: Optional[UserId] = None
    CreatedTimeStamp: Optional[TimeStamp] = None
    LastUpdatedTimeStamp: Optional[TimeStamp] = None


class RecommendationFeedbackSummaries(BaseModel):
    __root__: List[RecommendationFeedbackSummary]


class RepositoryAssociationSummaries(BaseModel):
    __root__: List[RepositoryAssociationSummary]


class S3RepositoryDetails(BaseModel):
    """
    Specifies the name of an S3 bucket and a <code>CodeArtifacts</code> object that contains the S3 object keys for a source code .zip file and for a build artifacts .zip file that contains .jar or .class files.
    """

    BucketName: Optional[S3BucketName] = None
    CodeArtifacts: Optional[CodeArtifacts] = None


class RuleTags(BaseModel):
    __root__: Annotated[List[RuleTag], Field(max_items=20, min_items=1)]


class S3BucketRepository(BaseModel):
    """
    Information about an associated repository in an S3 bucket. The associated repository contains a source code .zip file and a build artifacts .zip file that contains .jar or .class files.
    """

    Name: Name
    Details: Optional[S3RepositoryDetails] = None


class DescribeRecommendationFeedbackResponse(BaseModel):
    RecommendationFeedback: Optional[RecommendationFeedback] = None


class ListRecommendationFeedbackResponse(BaseModel):
    RecommendationFeedbackSummaries: Optional[RecommendationFeedbackSummaries] = None
    NextToken: Optional[NextToken] = None


class ListRepositoryAssociationsResponse(BaseModel):
    RepositoryAssociationSummaries: Optional[RepositoryAssociationSummaries] = None
    NextToken: Optional[NextToken] = None


class RepositoryAssociation(BaseModel):
    """
    Information about a repository association. The <a href="https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_DescribeRepositoryAssociation.html"> <code>DescribeRepositoryAssociation</code> </a> operation returns a <code>RepositoryAssociation</code> object.
    """

    AssociationId: Optional[AssociationId] = None
    AssociationArn: Optional[Arn] = None
    ConnectionArn: Optional[ConnectionArn] = None
    Name: Optional[Name] = None
    Owner: Optional[Owner] = None
    ProviderType: Optional[ProviderType] = None
    State: Optional[RepositoryAssociationState] = None
    StateReason: Optional[StateReason] = None
    LastUpdatedTimeStamp: Optional[TimeStamp] = None
    CreatedTimeStamp: Optional[TimeStamp] = None
    KMSKeyDetails: Optional[KMSKeyDetails] = None
    S3RepositoryDetails: Optional[S3RepositoryDetails] = None


class SourceCodeType(BaseModel):
    """
    Specifies the source code that is analyzed in a code review.
    """

    CommitDiff: Optional[CommitDiffSourceCodeType] = None
    RepositoryHead: Optional[RepositoryHeadSourceCodeType] = None
    BranchDiff: Optional[BranchDiffSourceCodeType] = None
    S3BucketRepository: Optional[S3BucketRepository] = None
    RequestMetadata: Optional[RequestMetadata] = None


class CodeReview(BaseModel):
    """
    Information about a code review. A code review belongs to the associated repository that contains the reviewed code.
    """

    Name: Optional[Name] = None
    CodeReviewArn: Optional[Arn] = None
    RepositoryName: Optional[Name] = None
    Owner: Optional[Owner] = None
    ProviderType: Optional[ProviderType] = None
    State: Optional[JobState] = None
    StateReason: Optional[StateReason] = None
    CreatedTimeStamp: Optional[TimeStamp] = None
    LastUpdatedTimeStamp: Optional[TimeStamp] = None
    Type: Optional[Type] = None
    PullRequestId: Optional[PullRequestId] = None
    SourceCodeType: Optional[SourceCodeType] = None
    AssociationArn: Optional[AssociationArn1] = None
    Metrics: Optional[Metrics] = None
    AnalysisTypes: Optional[AnalysisTypes] = None


class CodeReviewSummary(BaseModel):
    """
    Information about the summary of the code review.
    """

    Name: Optional[Name] = None
    CodeReviewArn: Optional[Arn] = None
    RepositoryName: Optional[Name] = None
    Owner: Optional[Owner] = None
    ProviderType: Optional[ProviderType] = None
    State: Optional[JobState] = None
    CreatedTimeStamp: Optional[TimeStamp] = None
    LastUpdatedTimeStamp: Optional[TimeStamp] = None
    Type: Optional[Type] = None
    PullRequestId: Optional[PullRequestId] = None
    MetricsSummary: Optional[MetricsSummary] = None
    SourceCodeType: Optional[SourceCodeType] = None


class CodeReviewSummaries(BaseModel):
    __root__: List[CodeReviewSummary]


class RuleMetadata(BaseModel):
    """
    Metadata about a rule. Rule metadata includes an ID, a name, a list of tags, and a short and long description. CodeGuru Reviewer uses rules to analyze code. A rule's recommendation is included in analysis results if code is detected that violates the rule.
    """

    RuleId: Optional[RuleId] = None
    RuleName: Optional[RuleName] = None
    ShortDescription: Optional[ShortDescription] = None
    LongDescription: Optional[LongDescription] = None
    RuleTags: Optional[RuleTags] = None


class AssociateRepositoryResponse(BaseModel):
    RepositoryAssociation: Optional[RepositoryAssociation] = None
    Tags: Optional[TagMap] = None


class CreateCodeReviewResponse(BaseModel):
    CodeReview: Optional[CodeReview] = None


class RepositoryAnalysis(BaseModel):
    """
    A code review type that analyzes all code under a specified branch in an associated repository. The associated repository is specified using its ARN when you call <a href="https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_CreateCodeReview"> <code>CreateCodeReview</code> </a>.
    """

    RepositoryHead: Optional[RepositoryHeadSourceCodeType] = None
    SourceCodeType: Optional[SourceCodeType] = None


class DescribeCodeReviewResponse(CreateCodeReviewResponse):
    pass


class DescribeRepositoryAssociationResponse(AssociateRepositoryResponse):
    pass


class DisassociateRepositoryResponse(AssociateRepositoryResponse):
    pass


class ListCodeReviewsResponse(BaseModel):
    CodeReviewSummaries: Optional[CodeReviewSummaries] = None
    NextToken: Optional[NextToken] = None


class CodeReviewType(BaseModel):
    """
    <p> The type of a code review. There are two code review types: </p> <ul> <li> <p> <code>PullRequest</code> - A code review that is automatically triggered by a pull request on an associated repository. </p> </li> <li> <p> <code>RepositoryAnalysis</code> - A code review that analyzes all code under a specified branch in an associated repository. The associated repository is specified using its ARN in <a href="https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_CreateCodeReview"> <code>CreateCodeReview</code> </a>. </p> </li> </ul>
    """

    RepositoryAnalysis: RepositoryAnalysis
    AnalysisTypes: Optional[AnalysisTypes] = None


class CreateCodeReviewRequest(BaseModel):
    Name: CodeReviewName
    RepositoryAssociationArn: AssociationArn1
    Type: CodeReviewType
    ClientRequestToken: Optional[ClientRequestToken] = None


class RecommendationSummary(BaseModel):
    """
    Information about recommendations.
    """

    FilePath: Optional[FilePath] = None
    RecommendationId: Optional[RecommendationId] = None
    StartLine: Optional[LineNumber] = None
    EndLine: Optional[LineNumber] = None
    Description: Optional[Text] = None
    RecommendationCategory: Optional[RecommendationCategory] = None
    RuleMetadata: Optional[RuleMetadata] = None
    Severity: Optional[Severity] = None


class RecommendationSummaries(BaseModel):
    __root__: List[RecommendationSummary]


class ListRecommendationsResponse(BaseModel):
    RecommendationSummaries: Optional[RecommendationSummaries] = None
    NextToken: Optional[NextToken] = None
