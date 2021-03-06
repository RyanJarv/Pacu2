# generated by datamodel-codegen:
#   filename:  openapi.yaml
#   timestamp: 2021-12-31T02:59:10+00:00

from __future__ import annotations

from enum import Enum
from typing import Annotated, Any, List, Optional

from pydantic import BaseModel, Field


class InvalidParameterException(BaseModel):
    __root__: Any


class InvalidS3ObjectException(InvalidParameterException):
    pass


class UnsupportedDocumentException(InvalidParameterException):
    pass


class DocumentTooLargeException(InvalidParameterException):
    pass


class BadDocumentException(InvalidParameterException):
    pass


class AccessDeniedException(InvalidParameterException):
    pass


class ProvisionedThroughputExceededException(InvalidParameterException):
    pass


class InternalServerError(InvalidParameterException):
    pass


class ThrottlingException(InvalidParameterException):
    pass


class HumanLoopQuotaExceededException(InvalidParameterException):
    pass


class InvalidJobIdException(InvalidParameterException):
    pass


class InvalidKMSKeyException(InvalidParameterException):
    pass


class IdempotentParameterMismatchException(InvalidParameterException):
    pass


class LimitExceededException(InvalidParameterException):
    pass


class String(BaseModel):
    __root__: str


class BlockType(Enum):
    KEY_VALUE_SET = 'KEY_VALUE_SET'
    PAGE = 'PAGE'
    LINE = 'LINE'
    WORD = 'WORD'
    TABLE = 'TABLE'
    CELL = 'CELL'
    SELECTION_ELEMENT = 'SELECTION_ELEMENT'


class Percent(BaseModel):
    __root__: Annotated[float, Field(ge=0.0, le=100.0)]


class TextType(Enum):
    HANDWRITING = 'HANDWRITING'
    PRINTED = 'PRINTED'


class UInteger(BaseModel):
    __root__: Annotated[int, Field(ge=0.0)]


class NonEmptyString(BaseModel):
    __root__: Annotated[str, Field(regex='.*\\S.*')]


class SelectionStatus(Enum):
    SELECTED = 'SELECTED'
    NOT_SELECTED = 'NOT_SELECTED'


class Float(BaseModel):
    __root__: float


class BoundingBox(BaseModel):
    """
    <p>The bounding box around the detected page, text, key-value pair, table, table cell, or selection element on a document page. The <code>left</code> (x-coordinate) and <code>top</code> (y-coordinate) are coordinates that represent the top and left sides of the bounding box. Note that the upper-left corner of the image is the origin (0,0). </p> <p>The <code>top</code> and <code>left</code> values returned are ratios of the overall document page size. For example, if the input image is 700 x 200 pixels, and the top-left coordinate of the bounding box is 350 x 50 pixels, the API returns a <code>left</code> value of 0.5 (350/700) and a <code>top</code> value of 0.25 (50/200).</p> <p>The <code>width</code> and <code>height</code> values represent the dimensions of the bounding box as a ratio of the overall document page dimension. For example, if the document page size is 700 x 200 pixels, and the bounding box width is 70 pixels, the width returned is 0.1. </p>
    """

    Width: Optional[Float] = None
    Height: Optional[Float] = None
    Left: Optional[Float] = None
    Top: Optional[Float] = None


class ClientRequestToken(BaseModel):
    __root__: Annotated[
        str, Field(max_length=64, min_length=1, regex='^[a-zA-Z0-9-_]+$')
    ]


class ContentClassifier(Enum):
    FreeOfPersonallyIdentifiableInformation = 'FreeOfPersonallyIdentifiableInformation'
    FreeOfAdultContent = 'FreeOfAdultContent'


class ContentClassifiers(BaseModel):
    __root__: Annotated[List[ContentClassifier], Field(max_items=256)]


class ImageBlob(BaseModel):
    __root__: Annotated[str, Field(max_length=10485760, min_length=1)]


class EntityType(Enum):
    KEY = 'KEY'
    VALUE = 'VALUE'


class ErrorCode(String):
    pass


class ExpenseType(BaseModel):
    """
    An object used to store information about the Type detected by Amazon Textract.
    """

    Text: Optional[String] = None
    Confidence: Optional[Percent] = None


class FeatureType(Enum):
    TABLES = 'TABLES'
    FORMS = 'FORMS'


class FlowDefinitionArn(BaseModel):
    __root__: Annotated[str, Field(max_length=256)]


class JobId(ClientRequestToken):
    pass


class MaxResults(BaseModel):
    __root__: Annotated[int, Field(ge=1.0)]


class PaginationToken(BaseModel):
    __root__: Annotated[str, Field(max_length=255, min_length=1, regex='.*\\S.*')]


class JobStatus(Enum):
    IN_PROGRESS = 'IN_PROGRESS'
    SUCCEEDED = 'SUCCEEDED'
    FAILED = 'FAILED'
    PARTIAL_SUCCESS = 'PARTIAL_SUCCESS'


class StatusMessage(String):
    pass


class HumanLoopActivationConditionsEvaluationResults(BaseModel):
    __root__: Annotated[str, Field(max_length=10240)]


class HumanLoopArn(FlowDefinitionArn):
    pass


class HumanLoopActivationReason(String):
    pass


class HumanLoopName(BaseModel):
    __root__: Annotated[
        str, Field(max_length=63, min_length=1, regex='^[a-z0-9](-*[a-z0-9])*')
    ]


class HumanLoopDataAttributes(BaseModel):
    """
    Allows you to set attributes of the image. Currently, you can declare an image as free of personally identifiable information and adult content.
    """

    ContentClassifiers: Optional[ContentClassifiers] = None


class IdList(BaseModel):
    __root__: List[NonEmptyString]


class JobTag(BaseModel):
    __root__: Annotated[
        str, Field(max_length=64, min_length=1, regex='[a-zA-Z0-9_.\\-:]+')
    ]


class KMSKeyId(BaseModel):
    __root__: Annotated[
        str,
        Field(
            max_length=2048,
            min_length=1,
            regex='^[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,2048}$',
        ),
    ]


class SNSTopicArn(BaseModel):
    __root__: Annotated[
        str,
        Field(
            max_length=1024,
            min_length=20,
            regex='(^arn:([a-z\\d-]+):sns:[a-zA-Z\\d-]{1,20}:\\w{12}:.+$)',
        ),
    ]


class RoleArn(BaseModel):
    __root__: Annotated[
        str,
        Field(
            max_length=2048,
            min_length=20,
            regex='arn:([a-z\\d-]+):iam::\\d{12}:role/?[a-zA-Z_0-9+=,.@\\-_/]+',
        ),
    ]


class NotificationChannel(BaseModel):
    """
    The Amazon Simple Notification Service (Amazon SNS) topic to which Amazon Textract publishes the completion status of an asynchronous document operation, such as <a>StartDocumentTextDetection</a>.
    """

    SNSTopicArn: SNSTopicArn
    RoleArn: RoleArn


class S3Bucket(BaseModel):
    __root__: Annotated[
        str, Field(max_length=255, min_length=3, regex='[0-9A-Za-z\\.\\-_]*')
    ]


class S3ObjectName(BaseModel):
    __root__: Annotated[str, Field(max_length=1024, min_length=1, regex='.*\\S.*')]


class OutputConfig(BaseModel):
    """
    <p>Sets whether or not your output will go to a user created bucket. Used to set the name of the bucket, and the prefix on the output file.</p> <p> <code>OutputConfig</code> is an optional parameter which lets you adjust where your output will be placed. By default, Amazon Textract will store the results internally and can only be accessed by the Get API operations. With OutputConfig enabled, you can set the name of the bucket the output will be sent to and the file prefix of the results where you can download your results. Additionally, you can set the <code>KMSKeyID</code> parameter to a customer master key (CMK) to encrypt your output. Without this parameter set Amazon Textract will encrypt server-side using the AWS managed CMK for Amazon S3.</p> <p>Decryption of Customer Content is necessary for processing of the documents by Amazon Textract. If your account is opted out under an AI services opt out policy then all unencrypted Customer Content is immediately and permanently deleted after the Customer Content has been processed by the service. No copy of of the output is retained by Amazon Textract. For information about how to opt out, see <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_ai-opt-out.html"> Managing AI services opt-out policy. </a> </p> <p>For more information on data privacy, see the <a href="https://aws.amazon.com/compliance/data-privacy-faq/">Data Privacy FAQ</a>.</p>
    """

    S3Bucket: S3Bucket
    S3Prefix: Optional[S3ObjectName] = None


class Pages1(BaseModel):
    __root__: List[UInteger]


class Point(BaseModel):
    """
    <p>The X and Y coordinates of a point on a document page. The X and Y values that are returned are ratios of the overall document page size. For example, if the input document is 700 x 200 and the operation returns X=0.5 and Y=0.25, then the point is at the (350,50) pixel coordinate on the document page.</p> <p>An array of <code>Point</code> objects, <code>Polygon</code>, is returned by <a>DetectDocumentText</a>. <code>Polygon</code> represents a fine-grained polygon around detected text. For more information, see Geometry in the Amazon Textract Developer Guide. </p>
    """

    X: Optional[Float] = None
    Y: Optional[Float] = None


class RelationshipType(Enum):
    VALUE = 'VALUE'
    CHILD = 'CHILD'
    COMPLEX_FEATURES = 'COMPLEX_FEATURES'


class Relationship(BaseModel):
    """
    <p>Information about how blocks are related to each other. A <code>Block</code> object contains 0 or more <code>Relation</code> objects in a list, <code>Relationships</code>. For more information, see <a>Block</a>.</p> <p>The <code>Type</code> element provides the type of the relationship for all blocks in the <code>IDs</code> array. </p>
    """

    Type: Optional[RelationshipType] = None
    Ids: Optional[IdList] = None


class S3ObjectVersion(S3ObjectName):
    pass


class Warning(BaseModel):
    """
    A warning about an issue that occurred during asynchronous text analysis (<a>StartDocumentAnalysis</a>) or asynchronous document text detection (<a>StartDocumentTextDetection</a>).
    """

    ErrorCode: Optional[ErrorCode] = None
    Pages: Optional[Pages1] = None


class GetDocumentAnalysisRequest(BaseModel):
    JobId: JobId
    MaxResults: Optional[MaxResults] = None
    NextToken: Optional[PaginationToken] = None


class GetDocumentTextDetectionRequest(BaseModel):
    JobId: JobId
    MaxResults: Optional[MaxResults] = None
    NextToken: Optional[PaginationToken] = None


class StartDocumentAnalysisResponse(BaseModel):
    JobId: Optional[JobId] = None


class StartDocumentTextDetectionResponse(StartDocumentAnalysisResponse):
    pass


class FeatureTypes(BaseModel):
    __root__: List[FeatureType]


class HumanLoopConfig(BaseModel):
    """
    Sets up the human review workflow the document will be sent to if one of the conditions is met. You can also set certain attributes of the image before review.
    """

    HumanLoopName: HumanLoopName
    FlowDefinitionArn: FlowDefinitionArn
    DataAttributes: Optional[HumanLoopDataAttributes] = None


class DocumentMetadata(BaseModel):
    """
    Information about the input document.
    """

    Pages: Optional[UInteger] = None


class RelationshipList(BaseModel):
    __root__: List[Relationship]


class EntityTypes(BaseModel):
    __root__: List[EntityType]


class S3Object(BaseModel):
    """
    <p>The S3 bucket name and file name that identifies the document.</p> <p>The AWS Region for the S3 bucket that contains the document must match the Region that you use for Amazon Textract operations.</p> <p>For Amazon Textract to process a file in an S3 bucket, the user must have permission to access the S3 bucket and file. </p>
    """

    Bucket: Optional[S3Bucket] = None
    Name: Optional[S3ObjectName] = None
    Version: Optional[S3ObjectVersion] = None


class DocumentLocation(BaseModel):
    """
    <p>The Amazon S3 bucket that contains the document to be processed. It's used by asynchronous operations such as <a>StartDocumentTextDetection</a>.</p> <p>The input document can be an image file in JPEG or PNG format. It can also be a file in PDF format.</p>
    """

    S3Object: Optional[S3Object] = None


class Polygon(BaseModel):
    __root__: List[Point]


class Warnings(BaseModel):
    __root__: List[Warning]


class HumanLoopActivationReasons(BaseModel):
    __root__: Annotated[List[HumanLoopActivationReason], Field(min_items=1)]


class StartDocumentAnalysisRequest(BaseModel):
    DocumentLocation: DocumentLocation
    FeatureTypes: FeatureTypes
    ClientRequestToken: Optional[ClientRequestToken] = None
    JobTag: Optional[JobTag] = None
    NotificationChannel: Optional[NotificationChannel] = None
    OutputConfig: Optional[OutputConfig] = None
    KMSKeyId: Optional[KMSKeyId] = None


class StartDocumentTextDetectionRequest(BaseModel):
    DocumentLocation: DocumentLocation
    ClientRequestToken: Optional[ClientRequestToken] = None
    JobTag: Optional[JobTag] = None
    NotificationChannel: Optional[NotificationChannel] = None
    OutputConfig: Optional[OutputConfig] = None
    KMSKeyId: Optional[KMSKeyId] = None


class Document(BaseModel):
    """
    <p>The input document, either as bytes or as an S3 object.</p> <p>You pass image bytes to an Amazon Textract API operation by using the <code>Bytes</code> property. For example, you would use the <code>Bytes</code> property to pass a document loaded from a local file system. Image bytes passed by using the <code>Bytes</code> property must be base64 encoded. Your code might not need to encode document file bytes if you're using an AWS SDK to call Amazon Textract API operations. </p> <p>You pass images stored in an S3 bucket to an Amazon Textract API operation by using the <code>S3Object</code> property. Documents stored in an S3 bucket don't need to be base64 encoded.</p> <p>The AWS Region for the S3 bucket that contains the S3 object must match the AWS Region that you use for Amazon Textract operations.</p> <p>If you use the AWS CLI to call Amazon Textract operations, passing image bytes using the Bytes property isn't supported. You must first upload the document to an Amazon S3 bucket, and then call the operation using the S3Object property.</p> <p>For Amazon Textract to process an S3 object, the user must have permission to access the S3 object. </p>
    """

    Bytes: Optional[ImageBlob] = None
    S3Object: Optional[S3Object] = None


class HumanLoopActivationOutput(BaseModel):
    """
    Shows the results of the human in the loop evaluation. If there is no HumanLoopArn, the input did not trigger human review.
    """

    HumanLoopArn: Optional[HumanLoopArn] = None
    HumanLoopActivationReasons: Optional[HumanLoopActivationReasons] = None
    HumanLoopActivationConditionsEvaluationResults: Optional[
        HumanLoopActivationConditionsEvaluationResults
    ] = None


class Geometry(BaseModel):
    """
    Information about where the following items are located on a document page: detected page, text, key-value pairs, tables, table cells, and selection elements.
    """

    BoundingBox: Optional[BoundingBox] = None
    Polygon: Optional[Polygon] = None


class Block(BaseModel):
    """
    <p>A <code>Block</code> represents items that are recognized in a document within a group of pixels close to each other. The information returned in a <code>Block</code> object depends on the type of operation. In text detection for documents (for example <a>DetectDocumentText</a>), you get information about the detected words and lines of text. In text analysis (for example <a>AnalyzeDocument</a>), you can also get information about the fields, tables, and selection elements that are detected in the document.</p> <p>An array of <code>Block</code> objects is returned by both synchronous and asynchronous operations. In synchronous operations, such as <a>DetectDocumentText</a>, the array of <code>Block</code> objects is the entire set of results. In asynchronous operations, such as <a>GetDocumentAnalysis</a>, the array is returned over one or more responses.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/textract/latest/dg/how-it-works.html">How Amazon Textract Works</a>.</p>
    """

    BlockType: Optional[BlockType] = None
    Confidence: Optional[Percent] = None
    Text: Optional[String] = None
    TextType: Optional[TextType] = None
    RowIndex: Optional[UInteger] = None
    ColumnIndex: Optional[UInteger] = None
    RowSpan: Optional[UInteger] = None
    ColumnSpan: Optional[UInteger] = None
    Geometry: Optional[Geometry] = None
    Id: Optional[NonEmptyString] = None
    Relationships: Optional[RelationshipList] = None
    EntityTypes: Optional[EntityTypes] = None
    SelectionStatus: Optional[SelectionStatus] = None
    Page: Optional[UInteger] = None


class ExpenseDetection(BaseModel):
    """
    An object used to store information about the Value or Label detected by Amazon Textract.
    """

    Text: Optional[String] = None
    Geometry: Optional[Geometry] = None
    Confidence: Optional[Percent] = None


class ExpenseField(BaseModel):
    """
    Breakdown of detected information, seperated into the catagories Type, LableDetection, and ValueDetection
    """

    Type: Optional[ExpenseType] = None
    LabelDetection: Optional[ExpenseDetection] = None
    ValueDetection: Optional[ExpenseDetection] = None
    PageNumber: Optional[UInteger] = None


class AnalyzeDocumentRequest(BaseModel):
    Document: Document
    FeatureTypes: FeatureTypes
    HumanLoopConfig: Optional[HumanLoopConfig] = None


class AnalyzeExpenseRequest(BaseModel):
    Document: Document


class DetectDocumentTextRequest(BaseModel):
    Document: Document


class BlockList(BaseModel):
    __root__: List[Block]


class ExpenseFieldList(BaseModel):
    __root__: List[ExpenseField]


class LineItemFields(BaseModel):
    """
    A structure that holds information about the different lines found in a document's tables.
    """

    LineItemExpenseFields: Optional[ExpenseFieldList] = None


class LineItemList(BaseModel):
    __root__: List[LineItemFields]


class LineItemGroup(BaseModel):
    """
    A grouping of tables which contain LineItems, with each table identified by the table's <code>LineItemGroupIndex</code>.
    """

    LineItemGroupIndex: Optional[UInteger] = None
    LineItems: Optional[LineItemList] = None


class AnalyzeDocumentResponse(BaseModel):
    DocumentMetadata: Optional[DocumentMetadata] = None
    Blocks: Optional[BlockList] = None
    HumanLoopActivationOutput: Optional[HumanLoopActivationOutput] = None
    AnalyzeDocumentModelVersion: Optional[String] = None


class DetectDocumentTextResponse(BaseModel):
    DocumentMetadata: Optional[DocumentMetadata] = None
    Blocks: Optional[BlockList] = None
    DetectDocumentTextModelVersion: Optional[String] = None


class GetDocumentAnalysisResponse(BaseModel):
    DocumentMetadata: Optional[DocumentMetadata] = None
    JobStatus: Optional[JobStatus] = None
    NextToken: Optional[PaginationToken] = None
    Blocks: Optional[BlockList] = None
    Warnings: Optional[Warnings] = None
    StatusMessage: Optional[StatusMessage] = None
    AnalyzeDocumentModelVersion: Optional[String] = None


class GetDocumentTextDetectionResponse(BaseModel):
    DocumentMetadata: Optional[DocumentMetadata] = None
    JobStatus: Optional[JobStatus] = None
    NextToken: Optional[PaginationToken] = None
    Blocks: Optional[BlockList] = None
    Warnings: Optional[Warnings] = None
    StatusMessage: Optional[StatusMessage] = None
    DetectDocumentTextModelVersion: Optional[String] = None


class LineItemGroupList(BaseModel):
    __root__: List[LineItemGroup]


class ExpenseDocument(BaseModel):
    """
    The structure holding all the information returned by AnalyzeExpense
    """

    ExpenseIndex: Optional[UInteger] = None
    SummaryFields: Optional[ExpenseFieldList] = None
    LineItemGroups: Optional[LineItemGroupList] = None


class ExpenseDocumentList(BaseModel):
    __root__: List[ExpenseDocument]


class AnalyzeExpenseResponse(BaseModel):
    DocumentMetadata: Optional[DocumentMetadata] = None
    ExpenseDocuments: Optional[ExpenseDocumentList] = None
