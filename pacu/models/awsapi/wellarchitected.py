# generated by datamodel-codegen:
#   filename:  openapi.yaml
#   timestamp: 2021-12-31T02:59:33+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Annotated, Any, List, Optional

from pydantic import BaseModel, Extra, Field


class LensAlias(BaseModel):
    __root__: Annotated[
        str,
        Field(
            description='<p>The alias of the lens, for example, <code>serverless</code>.</p> <p>Each lens is identified by its <a>LensSummary$LensAlias</a>.</p>',
            max_length=64,
            min_length=1,
        ),
    ]


class ValidationException(BaseModel):
    __root__: Any


class ResourceNotFoundException(ValidationException):
    pass


class ConflictException(ValidationException):
    pass


class InternalServerException(ValidationException):
    pass


class AccessDeniedException(ValidationException):
    pass


class ThrottlingException(ValidationException):
    pass


class ServiceQuotaExceededException(ValidationException):
    pass


class AwsAccountId(BaseModel):
    __root__: Annotated[str, Field(description='An AWS account ID.', regex='[0-9]{12}')]


class AwsRegion(BaseModel):
    __root__: Annotated[
        str,
        Field(
            description='An AWS Region, for example, <code>us-west-2</code> or <code>ap-northeast-1</code>.',
            max_length=100,
        ),
    ]


class WorkloadNonAwsRegion(BaseModel):
    __root__: Annotated[str, Field(max_length=25, min_length=3)]


class PillarId(BaseModel):
    __root__: Annotated[
        str,
        Field(
            description='<p>The ID used to identify a pillar, for example, <code>security</code>.</p> <p>A pillar is identified by its <a>PillarReviewSummary$PillarId</a>.</p>',
            max_length=64,
            min_length=1,
        ),
    ]


class TagValue(BaseModel):
    __root__: Annotated[str, Field(max_length=256, min_length=0)]


class TagResourceOutput(BaseModel):
    pass


class UntagResourceOutput(TagResourceOutput):
    pass


class TagKey(BaseModel):
    __root__: Annotated[str, Field(max_length=128, min_length=1)]


class ChoiceId(BaseModel):
    __root__: Annotated[
        str, Field(description='The ID of a choice.', max_length=64, min_length=1)
    ]


class Notes1(BaseModel):
    __root__: Annotated[
        str,
        Field(description='The notes associated with the workload.', max_length=2084),
    ]


class QuestionId(BaseModel):
    __root__: Annotated[
        str, Field(description='The ID of the question.', max_length=128, min_length=1)
    ]


class QuestionTitle(BaseModel):
    __root__: Annotated[
        str,
        Field(description='The title of the question.', max_length=512, min_length=1),
    ]


class QuestionDescription(BaseModel):
    __root__: Annotated[
        str,
        Field(
            description='The description of the question.',
            max_length=1024,
            min_length=1,
        ),
    ]


class ImprovementPlanUrl(BaseModel):
    __root__: Annotated[
        str,
        Field(
            description='<p>The improvement plan URL for a question.</p> <p>This value is only available if the question has been answered.</p>',
            max_length=2048,
            min_length=1,
        ),
    ]


class HelpfulResourceUrl(BaseModel):
    __root__: Annotated[
        str,
        Field(
            description='The helpful resource URL for a question.',
            max_length=2048,
            min_length=1,
        ),
    ]


class SelectedChoices(BaseModel):
    """
    <p>List of selected choice IDs in a question answer.</p> <p>The values entered replace the previously selected choices.</p>
    """

    __root__: Annotated[
        List[ChoiceId],
        Field(
            description='<p>List of selected choice IDs in a question answer.</p> <p>The values entered replace the previously selected choices.</p>'
        ),
    ]


class IsApplicable(BaseModel):
    __root__: Annotated[
        bool,
        Field(
            description='Defines whether this question is applicable to a lens review.'
        ),
    ]


class Risk(Enum):
    """
    The risk for a given workload, lens review, pillar, or question.
    """

    UNANSWERED = 'UNANSWERED'
    HIGH = 'HIGH'
    MEDIUM = 'MEDIUM'
    NONE = 'NONE'
    NOT_APPLICABLE = 'NOT_APPLICABLE'


class AnswerReason(Enum):
    OUT_OF_SCOPE = 'OUT_OF_SCOPE'
    BUSINESS_PRIORITIES = 'BUSINESS_PRIORITIES'
    ARCHITECTURE_CONSTRAINTS = 'ARCHITECTURE_CONSTRAINTS'
    OTHER = 'OTHER'
    NONE = 'NONE'


class WorkloadId(BaseModel):
    __root__: Annotated[
        str,
        Field(
            description='The ID assigned to the workload. This ID is unique within an AWS Region.',
            regex='[0-9a-f]{32}',
        ),
    ]


class LensAliases(BaseModel):
    """
    <p>List of lens aliases to associate or disassociate with a workload.</p> <p>Identify a lens using its <a>LensSummary$LensAlias</a>.</p>
    """

    __root__: Annotated[
        List[LensAlias],
        Field(
            description='<p>List of lens aliases to associate or disassociate with a workload.</p> <p>Identify a lens using its <a>LensSummary$LensAlias</a>.</p>',
            min_items=1,
        ),
    ]


class AssociateLensesInput(BaseModel):
    """
    Input to associate lens reviews.
    """

    LensAliases: LensAliases


class Base64String(BaseModel):
    __root__: Annotated[
        str,
        Field(
            description='<p>The Base64-encoded string representation of a lens review report.</p> <p>This data can be used to create a PDF file.</p>'
        ),
    ]


class ChoiceTitle(BaseModel):
    __root__: Annotated[
        str, Field(description='The title of a choice.', max_length=512, min_length=1)
    ]


class ChoiceDescription(BaseModel):
    __root__: Annotated[
        str,
        Field(
            description='The description of a choice.', max_length=1024, min_length=1
        ),
    ]


class Choice(BaseModel):
    """
    A choice available to answer question.
    """

    ChoiceId: Optional[ChoiceId] = None
    Title: Optional[ChoiceTitle] = None
    Description: Optional[ChoiceDescription] = None


class ChoiceStatus(Enum):
    SELECTED = 'SELECTED'
    NOT_APPLICABLE = 'NOT_APPLICABLE'
    UNSELECTED = 'UNSELECTED'


class ChoiceNotes(BaseModel):
    __root__: Annotated[str, Field(max_length=250)]


class ChoiceAnswer(BaseModel):
    """
    A choice that has been answered on a question in your workload.
    """

    ChoiceId: Optional[ChoiceId] = None
    Status: Optional[ChoiceStatus] = None
    Reason: Optional[AnswerReason] = None
    Notes: Optional[ChoiceNotes] = None


class ChoiceAnswerSummary(BaseModel):
    """
    A choice summary that has been answered on a question in your workload.
    """

    ChoiceId: Optional[ChoiceId] = None
    Status: Optional[ChoiceStatus] = None
    Reason: Optional[AnswerReason] = None


class ChoiceUpdates(BaseModel):
    pass

    class Config:
        extra = Extra.allow


class ClientRequestToken(BaseModel):
    __root__: Annotated[
        str,
        Field(
            description='<p>A unique case-sensitive string used to ensure that this request is idempotent (executes only once).</p> <p>You should not reuse the same token for other requests. If you retry a request with the same client request token and the same parameters after it has completed successfully, the result of the original request is returned. </p> <important> <p>This token is listed as required, however, if you do not specify it, the AWS SDKs automatically generate one for you. If you are not using the AWS SDK or the AWS CLI, you must provide this token or the request will fail.</p> </important>'
        ),
    ]


class Count(BaseModel):
    __root__: Annotated[
        int, Field(description='A non-negative integer that denotes how many.', ge=0.0)
    ]


class MilestoneName(BaseModel):
    __root__: Annotated[
        str,
        Field(
            description='<p>The name of the milestone in a workload.</p> <p>Milestone names must be unique within a workload.</p>',
            max_length=100,
            min_length=3,
        ),
    ]


class CreateMilestoneInput(BaseModel):
    """
    Input for milestone creation.
    """

    MilestoneName: MilestoneName
    ClientRequestToken: ClientRequestToken


class MilestoneNumber(BaseModel):
    __root__: Annotated[
        int,
        Field(
            description='<p>The milestone number.</p> <p>A workload can have a maximum of 100 milestones.</p>',
            ge=1.0,
            le=100.0,
        ),
    ]


class WorkloadName(BaseModel):
    __root__: Annotated[
        str,
        Field(
            description='<p>The name of the workload.</p> <p>The name must be unique within an account within a Region. Spaces and capitalization are ignored when checking for uniqueness.</p>',
            max_length=100,
            min_length=3,
        ),
    ]


class WorkloadDescription(BaseModel):
    __root__: Annotated[
        str,
        Field(
            description='The description for the workload.',
            max_length=250,
            min_length=3,
        ),
    ]


class WorkloadEnvironment(Enum):
    """
    The environment for the workload.
    """

    PRODUCTION = 'PRODUCTION'
    PREPRODUCTION = 'PREPRODUCTION'


class WorkloadAccountIds(BaseModel):
    """
    The list of AWS account IDs associated with the workload.
    """

    __root__: Annotated[
        List[AwsAccountId],
        Field(
            description='The list of AWS account IDs associated with the workload.',
            max_items=100,
        ),
    ]


class WorkloadAwsRegions(BaseModel):
    """
    The list of AWS Regions associated with the workload, for example, <code>us-east-2</code>, or <code>ca-central-1</code>.
    """

    __root__: Annotated[
        List[AwsRegion],
        Field(
            description='The list of AWS Regions associated with the workload, for example, <code>us-east-2</code>, or <code>ca-central-1</code>.',
            max_items=50,
        ),
    ]


class WorkloadNonAwsRegions(BaseModel):
    """
    The list of non-AWS Regions associated with the workload.
    """

    __root__: Annotated[
        List[WorkloadNonAwsRegion],
        Field(
            description=' The list of non-AWS Regions associated with the workload.',
            max_items=5,
        ),
    ]


class WorkloadPillarPriorities(BaseModel):
    """
    The priorities of the pillars, which are used to order items in the improvement plan. Each pillar is represented by its <a>PillarReviewSummary$PillarId</a>.
    """

    __root__: Annotated[
        List[PillarId],
        Field(
            description='The priorities of the pillars, which are used to order items in the improvement plan. Each pillar is represented by its <a>PillarReviewSummary$PillarId</a>.'
        ),
    ]


class WorkloadArchitecturalDesign(BaseModel):
    __root__: Annotated[
        str,
        Field(
            description='The URL of the architectural design for the workload.',
            max_length=2048,
        ),
    ]


class WorkloadReviewOwner(BaseModel):
    __root__: Annotated[
        str,
        Field(
            description='The review owner of the workload. The name, email address, or identifier for the primary group or individual that owns the workload review process.',
            max_length=255,
            min_length=3,
        ),
    ]


class WorkloadIndustryType(BaseModel):
    __root__: Annotated[
        str,
        Field(
            description='<p>The industry type for the workload.</p> <p>If specified, must be one of the following:</p> <ul> <li> <p> <code>Agriculture</code> </p> </li> <li> <p> <code>Automobile</code> </p> </li> <li> <p> <code>Defense</code> </p> </li> <li> <p> <code>Design and Engineering</code> </p> </li> <li> <p> <code>Digital Advertising</code> </p> </li> <li> <p> <code>Education</code> </p> </li> <li> <p> <code>Environmental Protection</code> </p> </li> <li> <p> <code>Financial Services</code> </p> </li> <li> <p> <code>Gaming</code> </p> </li> <li> <p> <code>General Public Services</code> </p> </li> <li> <p> <code>Healthcare</code> </p> </li> <li> <p> <code>Hospitality</code> </p> </li> <li> <p> <code>InfoTech</code> </p> </li> <li> <p> <code>Justice and Public Safety</code> </p> </li> <li> <p> <code>Life Sciences</code> </p> </li> <li> <p> <code>Manufacturing</code> </p> </li> <li> <p> <code>Media &amp; Entertainment</code> </p> </li> <li> <p> <code>Mining &amp; Resources</code> </p> </li> <li> <p> <code>Oil &amp; Gas</code> </p> </li> <li> <p> <code>Power &amp; Utilities</code> </p> </li> <li> <p> <code>Professional Services</code> </p> </li> <li> <p> <code>Real Estate &amp; Construction</code> </p> </li> <li> <p> <code>Retail &amp; Wholesale</code> </p> </li> <li> <p> <code>Social Protection</code> </p> </li> <li> <p> <code>Telecommunications</code> </p> </li> <li> <p> <code>Travel, Transportation &amp; Logistics</code> </p> </li> <li> <p> <code>Other</code> </p> </li> </ul>',
            max_length=100,
        ),
    ]


class WorkloadIndustry(BaseModel):
    __root__: Annotated[
        str, Field(description='The industry for the workload.', max_length=100)
    ]


class WorkloadLenses(BaseModel):
    """
    The list of lenses associated with the workload. Each lens is identified by its <a>LensSummary$LensAlias</a>.
    """

    __root__: Annotated[
        List[LensAlias],
        Field(
            description='The list of lenses associated with the workload. Each lens is identified by its <a>LensSummary$LensAlias</a>.'
        ),
    ]


class TagMap(BaseModel):
    pass

    class Config:
        extra = Extra.allow


class CreateWorkloadInput(BaseModel):
    """
    Input for workload creation.
    """

    WorkloadName: WorkloadName
    Description: WorkloadDescription
    Environment: WorkloadEnvironment
    AccountIds: Optional[WorkloadAccountIds] = None
    AwsRegions: Optional[WorkloadAwsRegions] = None
    NonAwsRegions: Optional[WorkloadNonAwsRegions] = None
    PillarPriorities: Optional[WorkloadPillarPriorities] = None
    ArchitecturalDesign: Optional[WorkloadArchitecturalDesign] = None
    ReviewOwner: WorkloadReviewOwner
    IndustryType: Optional[WorkloadIndustryType] = None
    Industry: Optional[WorkloadIndustry] = None
    Lenses: WorkloadLenses
    Notes: Optional[Notes1] = None
    ClientRequestToken: ClientRequestToken
    Tags: Optional[TagMap] = None


class WorkloadArn(BaseModel):
    __root__: Annotated[str, Field(description='The ARN for the workload.')]


class SharedWith(BaseModel):
    __root__: Annotated[
        str,
        Field(
            description='The AWS account ID or IAM role with which the workload is shared.',
            max_length=2048,
            min_length=12,
        ),
    ]


class PermissionType(Enum):
    """
    Permission granted on a workload share.
    """

    READONLY = 'READONLY'
    CONTRIBUTOR = 'CONTRIBUTOR'


class CreateWorkloadShareInput(BaseModel):
    """
    Input for Create Workload Share
    """

    SharedWith: SharedWith
    PermissionType: PermissionType
    ClientRequestToken: ClientRequestToken


class ShareId(BaseModel):
    __root__: Annotated[
        str,
        Field(
            description='The ID associated with the workload share.',
            regex='[0-9a-f]{32}',
        ),
    ]


class DeleteWorkloadInput(BaseModel):
    """
    Input for workload deletion.
    """

    pass


class DeleteWorkloadShareInput(BaseModel):
    """
    Input for Delete Workload Share
    """

    pass


class DifferenceStatus(Enum):
    UPDATED = 'UPDATED'
    NEW = 'NEW'
    DELETED = 'DELETED'


class DisassociateLensesInput(BaseModel):
    """
    Input to disassociate lens reviews.
    """

    LensAliases: LensAliases


class GetAnswerInput(BaseModel):
    """
    Input to get answer.
    """

    pass


class GetLensReviewInput(BaseModel):
    """
    Input to get lens review.
    """

    pass


class GetLensReviewReportInput(BaseModel):
    """
    Input to get lens review report.
    """

    pass


class LensReviewReport(BaseModel):
    """
    A report of a lens review.
    """

    LensAlias: Optional[LensAlias] = None
    Base64String: Optional[Base64String] = None


class LensVersion(TagKey):
    pass


class GetLensVersionDifferenceInput(BaseModel):
    pass


class GetMilestoneInput(BaseModel):
    """
    Input to get a milestone.
    """

    pass


class GetWorkloadInput(BaseModel):
    """
    Input to get a workload.
    """

    pass


class ImprovementSummary(BaseModel):
    """
    An improvement summary of a lens review in a workload.
    """

    QuestionId: Optional[QuestionId] = None
    PillarId: Optional[PillarId] = None
    QuestionTitle: Optional[QuestionTitle] = None
    Risk: Optional[Risk] = None
    ImprovementPlanUrl: Optional[ImprovementPlanUrl] = None


class ImprovementSummaries(BaseModel):
    """
    List of improvement summaries of lens review in a workload.
    """

    __root__: Annotated[
        List[ImprovementSummary],
        Field(
            description='List of improvement summaries of lens review in a workload.'
        ),
    ]


class IsReviewOwnerUpdateAcknowledged(BaseModel):
    __root__: bool


class LensDescription(BaseModel):
    __root__: Annotated[
        str,
        Field(
            description='The description of the lens.', max_length=1024, min_length=1
        ),
    ]


class LensName(BaseModel):
    __root__: Annotated[
        str,
        Field(description='The full name of the lens.', max_length=128, min_length=1),
    ]


class LensStatus(Enum):
    CURRENT = 'CURRENT'
    NOT_CURRENT = 'NOT_CURRENT'
    DEPRECATED = 'DEPRECATED'


class Timestamp(BaseModel):
    __root__: Annotated[datetime, Field(description='The date and time recorded.')]


class RiskCounts(BaseModel):
    """
    A map from risk names to the count of how questions have that rating.
    """

    pass

    class Config:
        extra = Extra.allow


class NextToken(BaseModel):
    __root__: Annotated[
        str, Field(description='The token to use to retrieve the next set of results.')
    ]


class LensReviewSummary(BaseModel):
    """
    A lens review summary of a workload.
    """

    LensAlias: Optional[LensAlias] = None
    LensVersion: Optional[LensVersion] = None
    LensName: Optional[LensName] = None
    LensStatus: Optional[LensStatus] = None
    UpdatedAt: Optional[Timestamp] = None
    RiskCounts: Optional[RiskCounts] = None


class LensReviewSummaries(BaseModel):
    """
    List of lens summaries of lens reviews of a workload.
    """

    __root__: Annotated[
        List[LensReviewSummary],
        Field(description='List of lens summaries of lens reviews of a workload.'),
    ]


class LensSummary(BaseModel):
    """
    A lens summary of a lens.
    """

    LensAlias: Optional[LensAlias] = None
    LensVersion: Optional[LensVersion] = None
    LensName: Optional[LensName] = None
    Description: Optional[LensDescription] = None


class LensSummaries(BaseModel):
    """
    List of lens summaries of available lenses.
    """

    __root__: Annotated[
        List[LensSummary],
        Field(description='List of lens summaries of available lenses.'),
    ]


class LensUpgradeSummary(BaseModel):
    """
    Lens upgrade summary return object.
    """

    WorkloadId: Optional[WorkloadId] = None
    WorkloadName: Optional[WorkloadName] = None
    LensAlias: Optional[LensAlias] = None
    CurrentLensVersion: Optional[LensVersion] = None
    LatestLensVersion: Optional[LensVersion] = None


class ListAnswersMaxResults(BaseModel):
    __root__: Annotated[int, Field(ge=1.0, le=50.0)]


class ListAnswersInput(BaseModel):
    """
    Input to list answers.
    """

    pass


class ListLensReviewImprovementsMaxResults(BaseModel):
    __root__: Annotated[int, Field(ge=1.0, le=100.0)]


class ListLensReviewImprovementsInput(BaseModel):
    """
    Input to list lens review improvements.
    """

    pass


class MaxResults(BaseModel):
    __root__: Annotated[
        int,
        Field(
            description='The maximum number of results to return for this request.',
            ge=1.0,
            le=50.0,
        ),
    ]


class ListLensReviewsInput(BaseModel):
    """
    Input to list lens reviews.
    """

    pass


class ListLensesInput(BaseModel):
    """
    Input to list lenses.
    """

    pass


class ListMilestonesInput(BaseModel):
    """
    Input to list all milestones for a workload.
    """

    NextToken: Optional[NextToken] = None
    MaxResults: Optional[MaxResults] = None


class ListNotificationsMaxResults(ListAnswersMaxResults):
    pass


class ListNotificationsInput(BaseModel):
    WorkloadId: Optional[WorkloadId] = None
    NextToken: Optional[NextToken] = None
    MaxResults: Optional[ListNotificationsMaxResults] = None


class WorkloadNamePrefix(BaseModel):
    __root__: Annotated[
        str,
        Field(
            description='An optional string added to the beginning of each workload name returned in the results.',
            max_length=100,
        ),
    ]


class ListShareInvitationsMaxResults(ListAnswersMaxResults):
    pass


class ListShareInvitationsInput(BaseModel):
    """
    Input for List Share Invitations
    """

    pass


class ListTagsForResourceInput(BaseModel):
    pass


class SharedWithPrefix(BaseModel):
    __root__: Annotated[str, Field(max_length=100)]


class ListWorkloadSharesMaxResults(ListAnswersMaxResults):
    pass


class ListWorkloadSharesInput(BaseModel):
    """
    Input for List Workload Share
    """

    pass


class ListWorkloadsMaxResults(ListAnswersMaxResults):
    pass


class ListWorkloadsInput(BaseModel):
    """
    Input to list all workloads.
    """

    WorkloadNamePrefix: Optional[WorkloadNamePrefix] = None
    NextToken: Optional[NextToken] = None
    MaxResults: Optional[ListWorkloadsMaxResults] = None


class NotificationType(Enum):
    LENS_VERSION_UPGRADED = 'LENS_VERSION_UPGRADED'
    LENS_VERSION_DEPRECATED = 'LENS_VERSION_DEPRECATED'


class PillarName(BaseModel):
    __root__: Annotated[
        str, Field(description='The name of the pillar.', max_length=128, min_length=1)
    ]


class PillarNotes(BaseModel):
    """
    List of pillar notes of a lens review in a workload.
    """

    pass

    class Config:
        extra = Extra.allow


class PillarReviewSummary(BaseModel):
    """
    A pillar review summary of a lens review.
    """

    PillarId: Optional[PillarId] = None
    PillarName: Optional[PillarName] = None
    Notes: Optional[Notes1] = None
    RiskCounts: Optional[RiskCounts] = None


class QuestionDifference(BaseModel):
    """
    A question difference return object.
    """

    QuestionId: Optional[QuestionId] = None
    QuestionTitle: Optional[QuestionTitle] = None
    DifferenceStatus: Optional[DifferenceStatus] = None


class ShareInvitationId(BaseModel):
    __root__: Annotated[str, Field(regex='[0-9a-f]{32}')]


class ShareInvitation(BaseModel):
    """
    The share invitation.
    """

    ShareInvitationId: Optional[ShareInvitationId] = None
    WorkloadId: Optional[WorkloadId] = None


class ShareInvitationAction(Enum):
    """
    Share invitation action taken by contributor.
    """

    ACCEPT = 'ACCEPT'
    REJECT = 'REJECT'


class ShareInvitationSummary(BaseModel):
    """
    A share invitation summary return object.
    """

    ShareInvitationId: Optional[ShareInvitationId] = None
    SharedBy: Optional[AwsAccountId] = None
    SharedWith: Optional[SharedWith] = None
    PermissionType: Optional[PermissionType] = None
    WorkloadName: Optional[WorkloadName] = None
    WorkloadId: Optional[WorkloadId] = None


class ShareStatus(Enum):
    """
    The status of a workload share.
    """

    ACCEPTED = 'ACCEPTED'
    REJECTED = 'REJECTED'
    PENDING = 'PENDING'
    REVOKED = 'REVOKED'
    EXPIRED = 'EXPIRED'


class TagKeyList(BaseModel):
    __root__: Annotated[List[TagKey], Field(max_items=50, min_items=1)]


class TagResourceInput(BaseModel):
    Tags: TagMap


class UntagResourceInput(BaseModel):
    pass


class UpdateAnswerInput(BaseModel):
    """
    Input to update answer.
    """

    SelectedChoices: Optional[SelectedChoices] = None
    ChoiceUpdates: Optional[ChoiceUpdates] = None
    Notes: Optional[Notes1] = None
    IsApplicable: Optional[IsApplicable] = None
    Reason: Optional[AnswerReason] = None


class UpdateLensReviewInput(BaseModel):
    """
    Input for update lens review.
    """

    LensNotes: Optional[Notes1] = None
    PillarNotes: Optional[PillarNotes] = None


class UpdateShareInvitationInput(BaseModel):
    """
    Input for Update Share Invitation
    """

    ShareInvitationAction: ShareInvitationAction


class WorkloadImprovementStatus(Enum):
    """
    The improvement status for a workload.
    """

    NOT_APPLICABLE = 'NOT_APPLICABLE'
    NOT_STARTED = 'NOT_STARTED'
    IN_PROGRESS = 'IN_PROGRESS'
    COMPLETE = 'COMPLETE'
    RISK_ACKNOWLEDGED = 'RISK_ACKNOWLEDGED'


class UpdateWorkloadInput(BaseModel):
    """
    Input to update a workload.
    """

    WorkloadName: Optional[WorkloadName] = None
    Description: Optional[WorkloadDescription] = None
    Environment: Optional[WorkloadEnvironment] = None
    AccountIds: Optional[WorkloadAccountIds] = None
    AwsRegions: Optional[WorkloadAwsRegions] = None
    NonAwsRegions: Optional[WorkloadNonAwsRegions] = None
    PillarPriorities: Optional[WorkloadPillarPriorities] = None
    ArchitecturalDesign: Optional[WorkloadArchitecturalDesign] = None
    ReviewOwner: Optional[WorkloadReviewOwner] = None
    IsReviewOwnerUpdateAcknowledged: Optional[IsReviewOwnerUpdateAcknowledged] = None
    IndustryType: Optional[WorkloadIndustryType] = None
    Industry: Optional[WorkloadIndustry] = None
    Notes: Optional[Notes1] = None
    ImprovementStatus: Optional[WorkloadImprovementStatus] = None


class UpdateWorkloadShareInput(BaseModel):
    """
    Input for Update Workload Share
    """

    PermissionType: PermissionType


class WorkloadShare(BaseModel):
    """
    A workload share return object.
    """

    ShareId: Optional[ShareId] = None
    SharedBy: Optional[AwsAccountId] = None
    SharedWith: Optional[SharedWith] = None
    PermissionType: Optional[PermissionType] = None
    Status: Optional[ShareStatus] = None
    WorkloadName: Optional[WorkloadName] = None
    WorkloadId: Optional[WorkloadId] = None


class UpgradeLensReviewInput(BaseModel):
    MilestoneName: MilestoneName
    ClientRequestToken: Optional[ClientRequestToken] = None


class WorkloadShareSummary(BaseModel):
    """
    A workload share summary return object.
    """

    ShareId: Optional[ShareId] = None
    SharedWith: Optional[SharedWith] = None
    PermissionType: Optional[PermissionType] = None
    Status: Optional[ShareStatus] = None


class CreateMilestoneOutput(BaseModel):
    """
    Output of a create milestone call.
    """

    WorkloadId: Optional[WorkloadId] = None
    MilestoneNumber: Optional[MilestoneNumber] = None


class CreateWorkloadOutput(BaseModel):
    """
    Output of a create workload call.
    """

    WorkloadId: Optional[WorkloadId] = None
    WorkloadArn: Optional[WorkloadArn] = None


class CreateWorkloadShareOutput(BaseModel):
    """
    Input for Create Workload Share
    """

    WorkloadId: Optional[WorkloadId] = None
    ShareId: Optional[ShareId] = None


class GetLensReviewReportOutput(BaseModel):
    """
    Output of a get lens review report call.
    """

    WorkloadId: Optional[WorkloadId] = None
    MilestoneNumber: Optional[MilestoneNumber] = None
    LensReviewReport: Optional[LensReviewReport] = None


class ListLensReviewImprovementsOutput(BaseModel):
    """
    Output of a list lens review improvements call.
    """

    WorkloadId: Optional[WorkloadId] = None
    MilestoneNumber: Optional[MilestoneNumber] = None
    LensAlias: Optional[LensAlias] = None
    ImprovementSummaries: Optional[ImprovementSummaries] = None
    NextToken: Optional[NextToken] = None


class ListLensReviewsOutput(BaseModel):
    """
    Output of a list lens reviews call.
    """

    WorkloadId: Optional[WorkloadId] = None
    MilestoneNumber: Optional[MilestoneNumber] = None
    LensReviewSummaries: Optional[LensReviewSummaries] = None
    NextToken: Optional[NextToken] = None


class ListLensesOutput(BaseModel):
    """
    Output of a list lenses call.
    """

    LensSummaries: Optional[LensSummaries] = None
    NextToken: Optional[NextToken] = None


class ListTagsForResourceOutput(BaseModel):
    Tags: Optional[TagMap] = None


class ChoiceUpdate(BaseModel):
    """
    A list of choices to be updated.
    """

    Status: ChoiceStatus
    Reason: Optional[AnswerReason] = None
    Notes: Optional[ChoiceNotes] = None


class UpdateShareInvitationOutput(BaseModel):
    ShareInvitation: Optional[ShareInvitation] = None


class UpdateWorkloadShareOutput(BaseModel):
    """
    Input for Update Workload Share
    """

    WorkloadId: Optional[WorkloadId] = None
    WorkloadShare: Optional[WorkloadShare] = None


class Choices(BaseModel):
    """
    List of choices available for a question.
    """

    __root__: Annotated[
        List[Choice], Field(description='List of choices available for a question.')
    ]


class ChoiceAnswers(BaseModel):
    __root__: List[ChoiceAnswer]


class Answer(BaseModel):
    """
    An answer of the question.
    """

    QuestionId: Optional[QuestionId] = None
    PillarId: Optional[PillarId] = None
    QuestionTitle: Optional[QuestionTitle] = None
    QuestionDescription: Optional[QuestionDescription] = None
    ImprovementPlanUrl: Optional[ImprovementPlanUrl] = None
    HelpfulResourceUrl: Optional[HelpfulResourceUrl] = None
    Choices: Optional[Choices] = None
    SelectedChoices: Optional[SelectedChoices] = None
    ChoiceAnswers: Optional[ChoiceAnswers] = None
    IsApplicable: Optional[IsApplicable] = None
    Risk: Optional[Risk] = None
    Notes: Optional[Notes1] = None
    Reason: Optional[AnswerReason] = None


class ChoiceAnswerSummaries(BaseModel):
    __root__: List[ChoiceAnswerSummary]


class Workload(BaseModel):
    """
    A workload return object.
    """

    WorkloadId: Optional[WorkloadId] = None
    WorkloadArn: Optional[WorkloadArn] = None
    WorkloadName: Optional[WorkloadName] = None
    Description: Optional[WorkloadDescription] = None
    Environment: Optional[WorkloadEnvironment] = None
    UpdatedAt: Optional[Timestamp] = None
    AccountIds: Optional[WorkloadAccountIds] = None
    AwsRegions: Optional[WorkloadAwsRegions] = None
    NonAwsRegions: Optional[WorkloadNonAwsRegions] = None
    ArchitecturalDesign: Optional[WorkloadArchitecturalDesign] = None
    ReviewOwner: Optional[WorkloadReviewOwner] = None
    ReviewRestrictionDate: Optional[Timestamp] = None
    IsReviewOwnerUpdateAcknowledged: Optional[IsReviewOwnerUpdateAcknowledged] = None
    IndustryType: Optional[WorkloadIndustryType] = None
    Industry: Optional[WorkloadIndustry] = None
    Notes: Optional[Notes1] = None
    ImprovementStatus: Optional[WorkloadImprovementStatus] = None
    RiskCounts: Optional[RiskCounts] = None
    PillarPriorities: Optional[WorkloadPillarPriorities] = None
    Lenses: Optional[WorkloadLenses] = None
    Owner: Optional[AwsAccountId] = None
    ShareInvitationId: Optional[ShareInvitationId] = None
    Tags: Optional[TagMap] = None


class PillarReviewSummaries(BaseModel):
    """
    List of pillar review summaries of lens review in a workload.
    """

    __root__: Annotated[
        List[PillarReviewSummary],
        Field(
            description='List of pillar review summaries of lens review in a workload.'
        ),
    ]


class ShareInvitationSummaries(BaseModel):
    __root__: List[ShareInvitationSummary]


class WorkloadShareSummaries(BaseModel):
    """
    A list of workload share summaries.
    """

    __root__: Annotated[
        List[WorkloadShareSummary],
        Field(description='A list of workload share summaries.'),
    ]


class WorkloadSummary(BaseModel):
    """
    A workload summary return object.
    """

    WorkloadId: Optional[WorkloadId] = None
    WorkloadArn: Optional[WorkloadArn] = None
    WorkloadName: Optional[WorkloadName] = None
    Owner: Optional[AwsAccountId] = None
    UpdatedAt: Optional[Timestamp] = None
    Lenses: Optional[WorkloadLenses] = None
    RiskCounts: Optional[RiskCounts] = None
    ImprovementStatus: Optional[WorkloadImprovementStatus] = None


class NotificationSummary(BaseModel):
    """
    A notification summary return object.
    """

    Type: Optional[NotificationType] = None
    LensUpgradeSummary: Optional[LensUpgradeSummary] = None


class QuestionDifferences(BaseModel):
    __root__: List[QuestionDifference]


class PillarDifference(BaseModel):
    """
    A pillar difference return object.
    """

    PillarId: Optional[PillarId] = None
    DifferenceStatus: Optional[DifferenceStatus] = None
    QuestionDifferences: Optional[QuestionDifferences] = None


class PillarDifferences(BaseModel):
    __root__: List[PillarDifference]


class GetAnswerOutput(BaseModel):
    """
    Output of a get answer call.
    """

    WorkloadId: Optional[WorkloadId] = None
    MilestoneNumber: Optional[MilestoneNumber] = None
    LensAlias: Optional[LensAlias] = None
    Answer: Optional[Answer] = None


class GetWorkloadOutput(BaseModel):
    """
    Output of a get workload call.
    """

    Workload: Optional[Workload] = None


class ListShareInvitationsOutput(BaseModel):
    """
    Input for List Share Invitations
    """

    ShareInvitationSummaries: Optional[ShareInvitationSummaries] = None
    NextToken: Optional[NextToken] = None


class ListWorkloadSharesOutput(BaseModel):
    """
    Input for List Workload Share
    """

    WorkloadId: Optional[WorkloadId] = None
    WorkloadShareSummaries: Optional[WorkloadShareSummaries] = None
    NextToken: Optional[NextToken] = None


class UpdateAnswerOutput(BaseModel):
    """
    Output of a update answer call.
    """

    WorkloadId: Optional[WorkloadId] = None
    LensAlias: Optional[LensAlias] = None
    Answer: Optional[Answer] = None


class UpdateWorkloadOutput(GetWorkloadOutput):
    """
    Output of an update workload call.
    """

    pass


class AnswerSummary(BaseModel):
    """
    An answer summary of a lens review in a workload.
    """

    QuestionId: Optional[QuestionId] = None
    PillarId: Optional[PillarId] = None
    QuestionTitle: Optional[QuestionTitle] = None
    Choices: Optional[Choices] = None
    SelectedChoices: Optional[SelectedChoices] = None
    ChoiceAnswerSummaries: Optional[ChoiceAnswerSummaries] = None
    IsApplicable: Optional[IsApplicable] = None
    Risk: Optional[Risk] = None
    Reason: Optional[AnswerReason] = None


class AnswerSummaries(BaseModel):
    """
    List of answer summaries of lens review in a workload.
    """

    __root__: Annotated[
        List[AnswerSummary],
        Field(description='List of answer summaries of lens review in a workload.'),
    ]


class LensReview(BaseModel):
    """
    A lens review of a question.
    """

    LensAlias: Optional[LensAlias] = None
    LensVersion: Optional[LensVersion] = None
    LensName: Optional[LensName] = None
    LensStatus: Optional[LensStatus] = None
    PillarReviewSummaries: Optional[PillarReviewSummaries] = None
    UpdatedAt: Optional[Timestamp] = None
    Notes: Optional[Notes1] = None
    RiskCounts: Optional[RiskCounts] = None
    NextToken: Optional[NextToken] = None


class VersionDifferences(BaseModel):
    """
    The differences between the base and latest versions of the lens.
    """

    PillarDifferences: Optional[PillarDifferences] = None


class Milestone(BaseModel):
    """
    A milestone return object.
    """

    MilestoneNumber: Optional[MilestoneNumber] = None
    MilestoneName: Optional[MilestoneName] = None
    RecordedAt: Optional[Timestamp] = None
    Workload: Optional[Workload] = None


class NotificationSummaries(BaseModel):
    __root__: List[NotificationSummary]


class WorkloadSummaries(BaseModel):
    """
    A list of workload summaries.
    """

    __root__: Annotated[
        List[WorkloadSummary], Field(description='A list of workload summaries.')
    ]


class MilestoneSummary(BaseModel):
    """
    A milestone summary return object.
    """

    MilestoneNumber: Optional[MilestoneNumber] = None
    MilestoneName: Optional[MilestoneName] = None
    RecordedAt: Optional[Timestamp] = None
    WorkloadSummary: Optional[WorkloadSummary] = None


class GetLensReviewOutput(BaseModel):
    """
    Output of a get lens review call.
    """

    WorkloadId: Optional[WorkloadId] = None
    MilestoneNumber: Optional[MilestoneNumber] = None
    LensReview: Optional[LensReview] = None


class GetLensVersionDifferenceOutput(BaseModel):
    LensAlias: Optional[LensAlias] = None
    BaseLensVersion: Optional[LensVersion] = None
    LatestLensVersion: Optional[LensVersion] = None
    VersionDifferences: Optional[VersionDifferences] = None


class GetMilestoneOutput(BaseModel):
    """
    Output of a get milestone call.
    """

    WorkloadId: Optional[WorkloadId] = None
    Milestone: Optional[Milestone] = None


class ListAnswersOutput(BaseModel):
    """
    Output of a list answers call.
    """

    WorkloadId: Optional[WorkloadId] = None
    MilestoneNumber: Optional[MilestoneNumber] = None
    LensAlias: Optional[LensAlias] = None
    AnswerSummaries: Optional[AnswerSummaries] = None
    NextToken: Optional[NextToken] = None


class ListNotificationsOutput(BaseModel):
    NotificationSummaries: Optional[NotificationSummaries] = None
    NextToken: Optional[NextToken] = None


class ListWorkloadsOutput(BaseModel):
    """
    Output of a list workloads call.
    """

    WorkloadSummaries: Optional[WorkloadSummaries] = None
    NextToken: Optional[NextToken] = None


class UpdateLensReviewOutput(BaseModel):
    """
    Output of a update lens review call.
    """

    WorkloadId: Optional[WorkloadId] = None
    LensReview: Optional[LensReview] = None


class MilestoneSummaries(BaseModel):
    """
    A list of milestone summaries.
    """

    __root__: Annotated[
        List[MilestoneSummary], Field(description='A list of milestone summaries.')
    ]


class ListMilestonesOutput(BaseModel):
    """
    Output of a list milestones call.
    """

    WorkloadId: Optional[WorkloadId] = None
    MilestoneSummaries: Optional[MilestoneSummaries] = None
    NextToken: Optional[NextToken] = None
