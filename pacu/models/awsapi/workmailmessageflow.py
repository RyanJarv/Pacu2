# generated by datamodel-codegen:
#   filename:  openapi.yaml
#   timestamp: 2021-12-31T02:59:41+00:00

from __future__ import annotations

from typing import Annotated, Any, Optional

from pydantic import BaseModel, Field


class ResourceNotFoundException(BaseModel):
    __root__: Any


class PutRawMessageContentResponse(BaseModel):
    pass


class InvalidContentLocation(ResourceNotFoundException):
    pass


class MessageRejected(ResourceNotFoundException):
    pass


class MessageFrozen(ResourceNotFoundException):
    pass


class MessageIdType(BaseModel):
    __root__: Annotated[str, Field(max_length=120, min_length=1, regex='[a-z0-9\\-]*')]


class GetRawMessageContentRequest(BaseModel):
    pass


class MessageContentBlob(BaseModel):
    __root__: str


class S3BucketIdType(BaseModel):
    __root__: Annotated[
        str, Field(max_length=63, min_length=3, regex='^[a-z0-9][a-z0-9\\-]*')
    ]


class S3KeyIdType(BaseModel):
    __root__: Annotated[
        str, Field(max_length=1024, min_length=1, regex='[a-zA-Z0-9\\-/]*')
    ]


class S3VersionType(BaseModel):
    __root__: Annotated[str, Field(max_length=1024, min_length=1, regex='.+')]


class GetRawMessageContentResponse(BaseModel):
    messageContent: MessageContentBlob


class S3Reference(BaseModel):
    """
    <p>Amazon S3 object representing the updated message content, in MIME format.</p> <note> <p>The region for the S3 bucket containing the S3 object must match the region used for WorkMail operations. Also, for WorkMail to process an S3 object, it must have permission to access that object. For more information, see <a href="https://docs.aws.amazon.com/workmail/latest/adminguide/update-with-lambda.html"> Updating message content with AWS Lambda</a>.</p> </note>
    """

    bucket: S3BucketIdType
    key: S3KeyIdType
    objectVersion: Optional[S3VersionType] = None


class RawMessageContent(BaseModel):
    """
    <p>Provides the MIME content of the updated email message as an S3 object. All MIME content must meet the following criteria:</p> <ul> <li> <p>Each part of a multipart MIME message must be formatted properly.</p> </li> <li> <p>Attachments must be of a content type that Amazon SES supports. For more information, see <a href="https://docs.aws.amazon.com/ses/latest/DeveloperGuide/mime-types-appendix.html">Unsupported Attachment Types</a>.</p> </li> <li> <p>If any of the MIME parts in a message contain content that is outside of the 7-bit ASCII character range, we recommend encoding that content.</p> </li> <li> <p>Per <a href="https://tools.ietf.org/html/rfc5321#section-4.5.3.1.6">RFC 5321</a>, the maximum length of each line of text, including the &lt;CRLF&gt;, must not exceed 1,000 characters.</p> </li> <li> <p>The message must contain all the required header fields. Check the returned error message for more information.</p> </li> <li> <p>The value of immutable headers must remain unchanged. Check the returned error message for more information.</p> </li> <li> <p>Certain unique headers can only appear once. Check the returned error message for more information.</p> </li> </ul>
    """

    s3Reference: S3Reference


class PutRawMessageContentRequest(BaseModel):
    content: RawMessageContent