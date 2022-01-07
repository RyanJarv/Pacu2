# generated by datamodel-codegen:
#   filename:  openapi.yaml
#   timestamp: 2021-12-31T02:44:40+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Annotated, Any, List, Optional

from pydantic import BaseModel, Field


class InvalidArgsException(BaseModel):
    __root__: Any


class InvalidPolicyException(InvalidArgsException):
    pass


class InvalidTagException(InvalidArgsException):
    pass


class LimitExceededException(InvalidArgsException):
    pass


class RequestInProgressException(InvalidArgsException):
    pass


class RequestFailedException(InvalidArgsException):
    pass


class ResourceNotFoundException(InvalidArgsException):
    pass


class InvalidArnException(InvalidArgsException):
    pass


class InvalidStateException(InvalidArgsException):
    pass


class PermissionAlreadyExistsException(InvalidArgsException):
    pass


class ConcurrentModificationException(InvalidArgsException):
    pass


class LockoutPreventedException(InvalidArgsException):
    pass


class InvalidRequestException(InvalidArgsException):
    pass


class MalformedCertificateException(InvalidArgsException):
    pass


class CertificateMismatchException(InvalidArgsException):
    pass


class MalformedCSRException(InvalidArgsException):
    pass


class InvalidNextTokenException(InvalidArgsException):
    pass


class RequestAlreadyProcessedException(InvalidArgsException):
    pass


class TooManyTagsException(InvalidArgsException):
    pass


class ASN1PrintableString64(BaseModel):
    __root__: Annotated[
        str, Field(max_length=64, min_length=0, regex="[a-zA-Z0-9'()+-.?:/= ]*")
    ]


class CountryCodeString(BaseModel):
    __root__: Annotated[str, Field(max_length=2, min_length=2, regex='[A-Za-z]{2}')]


class String64(BaseModel):
    __root__: Annotated[str, Field(max_length=64, min_length=0)]


class String128(BaseModel):
    __root__: Annotated[str, Field(max_length=128, min_length=0)]


class String40(BaseModel):
    __root__: Annotated[str, Field(max_length=40, min_length=0)]


class String16(BaseModel):
    __root__: Annotated[str, Field(max_length=16, min_length=0)]


class String5(BaseModel):
    __root__: Annotated[str, Field(max_length=5, min_length=0)]


class String3(BaseModel):
    __root__: Annotated[str, Field(max_length=3, min_length=0)]


class ASN1Subject(BaseModel):
    """
    Contains information about the certificate subject. The <code>Subject</code> field in the certificate identifies the entity that owns or controls the public key in the certificate. The entity can be a user, computer, device, or service. The <code>Subject </code>must contain an X.500 distinguished name (DN). A DN is a sequence of relative distinguished names (RDNs). The RDNs are separated by commas in the certificate.
    """

    Country: Optional[CountryCodeString] = None
    Organization: Optional[String64] = None
    OrganizationalUnit: Optional[String64] = None
    DistinguishedNameQualifier: Optional[ASN1PrintableString64] = None
    State: Optional[String128] = None
    CommonName: Optional[String64] = None
    SerialNumber: Optional[ASN1PrintableString64] = None
    Locality: Optional[String128] = None
    Title: Optional[String64] = None
    Surname: Optional[String40] = None
    GivenName: Optional[String16] = None
    Initials: Optional[String5] = None
    Pseudonym: Optional[String128] = None
    GenerationQualifier: Optional[String3] = None


class AWSPolicy(BaseModel):
    __root__: Annotated[
        str,
        Field(
            max_length=20480,
            min_length=1,
            regex='[\\u0009\\u000A\\u000D\\u0020-\\u00FF]+',
        ),
    ]


class CustomObjectIdentifier(BaseModel):
    __root__: Annotated[
        str,
        Field(
            max_length=64,
            min_length=0,
            regex='^([0-2])\\.([0-9]|([0-3][0-9]))((\\.([0-9]+)){0,126})$',
        ),
    ]


class AccessMethodType(Enum):
    CA_REPOSITORY = 'CA_REPOSITORY'
    RESOURCE_PKI_MANIFEST = 'RESOURCE_PKI_MANIFEST'
    RESOURCE_PKI_NOTIFY = 'RESOURCE_PKI_NOTIFY'


class AccountId(BaseModel):
    __root__: Annotated[str, Field(max_length=12, min_length=12, regex='[0-9]+')]


class ActionType(Enum):
    IssueCertificate = 'IssueCertificate'
    GetCertificate = 'GetCertificate'
    ListPermissions = 'ListPermissions'


class ActionList(BaseModel):
    __root__: Annotated[List[ActionType], Field(max_items=3, min_items=1)]


class Arn(BaseModel):
    __root__: Annotated[
        str,
        Field(
            max_length=200,
            min_length=5,
            regex='arn:[\\w+=/,.@-]+:[\\w+=/,.@-]+:[\\w+=/,.@-]*:[0-9]*:[\\w+=,.@-]+(/[\\w+=,.@-]+)*',
        ),
    ]


class AuditReportId(BaseModel):
    __root__: Annotated[
        str,
        Field(
            max_length=36,
            min_length=36,
            regex='[a-z0-9]{8}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{12}',
        ),
    ]


class AuditReportResponseFormat(Enum):
    JSON = 'JSON'
    CSV = 'CSV'


class AuditReportStatus(Enum):
    CREATING = 'CREATING'
    SUCCESS = 'SUCCESS'
    FAILED = 'FAILED'


class Boolean(BaseModel):
    __root__: bool


class TStamp(BaseModel):
    __root__: datetime


class CertificateAuthorityType(Enum):
    ROOT = 'ROOT'
    SUBORDINATE = 'SUBORDINATE'


class String(BaseModel):
    __root__: str


class CertificateAuthorityStatus(Enum):
    CREATING = 'CREATING'
    PENDING_CERTIFICATE = 'PENDING_CERTIFICATE'
    ACTIVE = 'ACTIVE'
    DELETED = 'DELETED'
    DISABLED = 'DISABLED'
    EXPIRED = 'EXPIRED'
    FAILED = 'FAILED'


class FailureReason(Enum):
    REQUEST_TIMED_OUT = 'REQUEST_TIMED_OUT'
    UNSUPPORTED_ALGORITHM = 'UNSUPPORTED_ALGORITHM'
    OTHER = 'OTHER'


class KeyStorageSecurityStandard(Enum):
    FIPS_140_2_LEVEL_2_OR_HIGHER = 'FIPS_140_2_LEVEL_2_OR_HIGHER'
    FIPS_140_2_LEVEL_3_OR_HIGHER = 'FIPS_140_2_LEVEL_3_OR_HIGHER'


class KeyAlgorithm(Enum):
    RSA_2048 = 'RSA_2048'
    RSA_4096 = 'RSA_4096'
    EC_prime256v1 = 'EC_prime256v1'
    EC_secp384r1 = 'EC_secp384r1'


class SigningAlgorithm(Enum):
    SHA256WITHECDSA = 'SHA256WITHECDSA'
    SHA384WITHECDSA = 'SHA384WITHECDSA'
    SHA512WITHECDSA = 'SHA512WITHECDSA'
    SHA256WITHRSA = 'SHA256WITHRSA'
    SHA384WITHRSA = 'SHA384WITHRSA'
    SHA512WITHRSA = 'SHA512WITHRSA'


class CertificateBody(String):
    pass


class CertificateBodyBlob(BaseModel):
    __root__: Annotated[str, Field(max_length=32768, min_length=1)]


class CertificateChain(String):
    pass


class CertificateChainBlob(BaseModel):
    __root__: Annotated[str, Field(max_length=2097152, min_length=0)]


class S3BucketName(BaseModel):
    __root__: Annotated[str, Field(max_length=63, min_length=3)]


class S3Key(BaseModel):
    __root__: Annotated[str, Field(max_length=1024)]


class IdempotencyToken(BaseModel):
    __root__: Annotated[
        str,
        Field(
            max_length=36, min_length=1, regex='[\\u0009\\u000A\\u000D\\u0020-\\u00FF]*'
        ),
    ]


class Principal(BaseModel):
    __root__: Annotated[str, Field(max_length=128, min_length=0, regex='^[^*]+$')]


class Integer1To5000(BaseModel):
    __root__: Annotated[int, Field(ge=1.0, le=5000.0)]


class String253(BaseModel):
    __root__: Annotated[str, Field(max_length=253, min_length=0)]


class String3To255(BaseModel):
    __root__: Annotated[str, Field(max_length=255, min_length=3)]


class S3ObjectAcl(Enum):
    PUBLIC_READ = 'PUBLIC_READ'
    BUCKET_OWNER_FULL_CONTROL = 'BUCKET_OWNER_FULL_CONTROL'


class CrlConfiguration(BaseModel):
    """
    <p>Contains configuration information for a certificate revocation list (CRL). Your private certificate authority (CA) creates base CRLs. Delta CRLs are not supported. You can enable CRLs for your new or an existing private CA by setting the <b>Enabled</b> parameter to <code>true</code>. Your private CA writes CRLs to an S3 bucket that you specify in the <b>S3BucketName</b> parameter. You can hide the name of your bucket by specifying a value for the <b>CustomCname</b> parameter. Your private CA copies the CNAME or the S3 bucket name to the <b>CRL Distribution Points</b> extension of each certificate it issues. Your S3 bucket policy must give write permission to ACM Private CA. </p> <p>ACM Private CA assets that are stored in Amazon S3 can be protected with encryption. For more information, see <a href="https://docs.aws.amazon.com/acm-pca/latest/userguide/PcaCreateCa.html#crl-encryption">Encrypting Your CRLs</a>.</p> <p>Your private CA uses the value in the <b>ExpirationInDays</b> parameter to calculate the <b>nextUpdate</b> field in the CRL. The CRL is refreshed at 1/2 the age of next update or when a certificate is revoked. When a certificate is revoked, it is recorded in the next CRL that is generated and in the next audit report. Only time valid certificates are listed in the CRL. Expired certificates are not included.</p> <p>A CRL is typically updated approximately 30 minutes after a certificate is revoked. If for any reason a CRL update fails, ACM Private CA makes further attempts every 15 minutes.</p> <p>CRLs contain the following fields:</p> <ul> <li> <p> <b>Version</b>: The current version number defined in RFC 5280 is V2. The integer value is 0x1. </p> </li> <li> <p> <b>Signature Algorithm</b>: The name of the algorithm used to sign the CRL.</p> </li> <li> <p> <b>Issuer</b>: The X.500 distinguished name of your private CA that issued the CRL.</p> </li> <li> <p> <b>Last Update</b>: The issue date and time of this CRL.</p> </li> <li> <p> <b>Next Update</b>: The day and time by which the next CRL will be issued.</p> </li> <li> <p> <b>Revoked Certificates</b>: List of revoked certificates. Each list item contains the following information.</p> <ul> <li> <p> <b>Serial Number</b>: The serial number, in hexadecimal format, of the revoked certificate.</p> </li> <li> <p> <b>Revocation Date</b>: Date and time the certificate was revoked.</p> </li> <li> <p> <b>CRL Entry Extensions</b>: Optional extensions for the CRL entry.</p> <ul> <li> <p> <b>X509v3 CRL Reason Code</b>: Reason the certificate was revoked.</p> </li> </ul> </li> </ul> </li> <li> <p> <b>CRL Extensions</b>: Optional extensions for the CRL.</p> <ul> <li> <p> <b>X509v3 Authority Key Identifier</b>: Identifies the public key associated with the private key used to sign the certificate.</p> </li> <li> <p> <b>X509v3 CRL Number:</b>: Decimal sequence number for the CRL.</p> </li> </ul> </li> <li> <p> <b>Signature Algorithm</b>: Algorithm used by your private CA to sign the CRL.</p> </li> <li> <p> <b>Signature Value</b>: Signature computed over the CRL.</p> </li> </ul> <p>Certificate revocation lists created by ACM Private CA are DER-encoded. You can use the following OpenSSL command to list a CRL.</p> <p> <code>openssl crl -inform DER -text -in <i>crl_path</i> -noout</code> </p> <p>For more information, see <a href="https://docs.aws.amazon.com/acm-pca/latest/userguide/crl-planning.html">Planning a certificate revocation list (CRL)</a> in the <i>AWS Certificate Manager Private Certificate Authority (PCA) User Guide</i> </p>
    """

    Enabled: Boolean
    ExpirationInDays: Optional[Integer1To5000] = None
    CustomCname: Optional[String253] = None
    S3BucketName: Optional[String3To255] = None
    S3ObjectAcl: Optional[S3ObjectAcl] = None


class CsrBlob(CertificateBodyBlob):
    pass


class CsrBody(String):
    pass


class KeyUsage(BaseModel):
    """
    Defines one or more purposes for which the key contained in the certificate can be used. Default value for each option is false.
    """

    DigitalSignature: Optional[Boolean] = None
    NonRepudiation: Optional[Boolean] = None
    KeyEncipherment: Optional[Boolean] = None
    DataEncipherment: Optional[Boolean] = None
    KeyAgreement: Optional[Boolean] = None
    KeyCertSign: Optional[Boolean] = None
    CRLSign: Optional[Boolean] = None
    EncipherOnly: Optional[Boolean] = None
    DecipherOnly: Optional[Boolean] = None


class PermanentDeletionTimeInDays(BaseModel):
    __root__: Annotated[int, Field(ge=7.0, le=30.0)]


class String256(BaseModel):
    __root__: Annotated[str, Field(max_length=256, min_length=0)]


class EdiPartyName(BaseModel):
    """
    Describes an Electronic Data Interchange (EDI) entity as described in as defined in <a href="https://tools.ietf.org/html/rfc5280">Subject Alternative Name</a> in RFC 5280.
    """

    PartyName: String256
    NameAssigner: Optional[String256] = None


class ExtendedKeyUsageType(Enum):
    SERVER_AUTH = 'SERVER_AUTH'
    CLIENT_AUTH = 'CLIENT_AUTH'
    CODE_SIGNING = 'CODE_SIGNING'
    EMAIL_PROTECTION = 'EMAIL_PROTECTION'
    TIME_STAMPING = 'TIME_STAMPING'
    OCSP_SIGNING = 'OCSP_SIGNING'
    SMART_CARD_LOGIN = 'SMART_CARD_LOGIN'
    DOCUMENT_SIGNING = 'DOCUMENT_SIGNING'
    CERTIFICATE_TRANSPARENCY = 'CERTIFICATE_TRANSPARENCY'


class ExtendedKeyUsage1(BaseModel):
    """
    Specifies additional purposes for which the certified public key may be used other than basic purposes indicated in the <code>KeyUsage</code> extension.
    """

    ExtendedKeyUsageType: Optional[ExtendedKeyUsageType] = None
    ExtendedKeyUsageObjectIdentifier: Optional[CustomObjectIdentifier] = None


class ExtendedKeyUsageList(BaseModel):
    __root__: Annotated[List[ExtendedKeyUsage1], Field(max_items=20, min_items=1)]


class OtherName(BaseModel):
    """
    Defines a custom ASN.1 X.400 <code>GeneralName</code> using an object identifier (OID) and value. The OID must satisfy the regular expression shown below. For more information, see NIST's definition of <a href="https://csrc.nist.gov/glossary/term/Object_Identifier">Object Identifier (OID)</a>.
    """

    TypeId: CustomObjectIdentifier
    Value: String256


class String39(BaseModel):
    __root__: Annotated[str, Field(max_length=39, min_length=0)]


class NextToken(BaseModel):
    __root__: Annotated[str, Field(max_length=500, min_length=1)]


class MaxResults(BaseModel):
    __root__: Annotated[int, Field(ge=1.0, le=1000.0)]


class ResourceOwner(Enum):
    SELF = 'SELF'
    OTHER_ACCOUNTS = 'OTHER_ACCOUNTS'


class OcspConfiguration(BaseModel):
    """
    <p>Contains information to enable and configure Online Certificate Status Protocol (OCSP) for validating certificate revocation status.</p> <p>When you revoke a certificate, OCSP responses may take up to 60 minutes to reflect the new status.</p>
    """

    Enabled: Boolean
    OcspCustomCname: Optional[String253] = None


class Permission(BaseModel):
    """
    Permissions designate which private CA actions can be performed by an AWS service or entity. In order for ACM to automatically renew private certificates, you must give the ACM service principal all available permissions (<code>IssueCertificate</code>, <code>GetCertificate</code>, and <code>ListPermissions</code>). Permissions can be assigned with the <a href="https://docs.aws.amazon.com/acm-pca/latest/APIReference/API_CreatePermission.html">CreatePermission</a> action, removed with the <a href="https://docs.aws.amazon.com/acm-pca/latest/APIReference/API_DeletePermission.html">DeletePermission</a> action, and listed with the <a href="https://docs.aws.amazon.com/acm-pca/latest/APIReference/API_ListPermissions.html">ListPermissions</a> action.
    """

    CertificateAuthorityArn: Optional[Arn] = None
    CreatedAt: Optional[TStamp] = None
    Principal: Optional[Principal] = None
    SourceAccount: Optional[AccountId] = None
    Actions: Optional[ActionList] = None
    Policy: Optional[AWSPolicy] = None


class PolicyQualifierId(Enum):
    CPS = 'CPS'


class Qualifier(BaseModel):
    """
    Defines a <code>PolicyInformation</code> qualifier. ACM Private CA supports the <a href="https://tools.ietf.org/html/rfc5280#section-4.2.1.4">certification practice statement (CPS) qualifier</a> defined in RFC 5280.
    """

    CpsUri: String256


class PolicyQualifierInfo(BaseModel):
    """
    Modifies the <code>CertPolicyId</code> of a <code>PolicyInformation</code> object with a qualifier. ACM Private CA supports the certification practice statement (CPS) qualifier.
    """

    PolicyQualifierId: PolicyQualifierId
    Qualifier: Qualifier


class PositiveLong(BaseModel):
    __root__: Annotated[int, Field(ge=1.0)]


class RevocationReason(Enum):
    UNSPECIFIED = 'UNSPECIFIED'
    KEY_COMPROMISE = 'KEY_COMPROMISE'
    CERTIFICATE_AUTHORITY_COMPROMISE = 'CERTIFICATE_AUTHORITY_COMPROMISE'
    AFFILIATION_CHANGED = 'AFFILIATION_CHANGED'
    SUPERSEDED = 'SUPERSEDED'
    CESSATION_OF_OPERATION = 'CESSATION_OF_OPERATION'
    PRIVILEGE_WITHDRAWN = 'PRIVILEGE_WITHDRAWN'
    A_A_COMPROMISE = 'A_A_COMPROMISE'


class TagKey(BaseModel):
    __root__: Annotated[
        str,
        Field(
            max_length=128, min_length=1, regex='^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-@]*)$'
        ),
    ]


class TagValue(BaseModel):
    __root__: Annotated[
        str,
        Field(
            max_length=256, min_length=0, regex='^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-@]*)$'
        ),
    ]


class Tag(BaseModel):
    """
    Tags are labels that you can use to identify and organize your private CAs. Each tag consists of a key and an optional value. You can associate up to 50 tags with a private CA. To add one or more tags to a private CA, call the <a href="https://docs.aws.amazon.com/acm-pca/latest/APIReference/API_TagCertificateAuthority.html">TagCertificateAuthority</a> action. To remove a tag, call the <a href="https://docs.aws.amazon.com/acm-pca/latest/APIReference/API_UntagCertificateAuthority.html">UntagCertificateAuthority</a> action.
    """

    Key: TagKey
    Value: Optional[TagValue] = None


class ValidityPeriodType(Enum):
    END_DATE = 'END_DATE'
    ABSOLUTE = 'ABSOLUTE'
    DAYS = 'DAYS'
    MONTHS = 'MONTHS'
    YEARS = 'YEARS'


class CreateCertificateAuthorityResponse(BaseModel):
    CertificateAuthorityArn: Optional[Arn] = None


class CreateCertificateAuthorityAuditReportResponse(BaseModel):
    AuditReportId: Optional[AuditReportId] = None
    S3Key: Optional[S3Key] = None


class CreateCertificateAuthorityAuditReportRequest(BaseModel):
    CertificateAuthorityArn: Arn
    S3BucketName: S3BucketName
    AuditReportResponseFormat: AuditReportResponseFormat


class CreatePermissionRequest(BaseModel):
    CertificateAuthorityArn: Arn
    Principal: Principal
    SourceAccount: Optional[AccountId] = None
    Actions: ActionList


class DeleteCertificateAuthorityRequest(BaseModel):
    CertificateAuthorityArn: Arn
    PermanentDeletionTimeInDays: Optional[PermanentDeletionTimeInDays] = None


class DeletePermissionRequest(BaseModel):
    CertificateAuthorityArn: Arn
    Principal: Principal
    SourceAccount: Optional[AccountId] = None


class DeletePolicyRequest(BaseModel):
    ResourceArn: Arn


class DescribeCertificateAuthorityRequest(BaseModel):
    CertificateAuthorityArn: Arn


class DescribeCertificateAuthorityAuditReportResponse(BaseModel):
    AuditReportStatus: Optional[AuditReportStatus] = None
    S3BucketName: Optional[S3BucketName] = None
    S3Key: Optional[S3Key] = None
    CreatedAt: Optional[TStamp] = None


class DescribeCertificateAuthorityAuditReportRequest(BaseModel):
    CertificateAuthorityArn: Arn
    AuditReportId: AuditReportId


class GetCertificateResponse(BaseModel):
    Certificate: Optional[CertificateBody] = None
    CertificateChain: Optional[CertificateChain] = None


class GetCertificateRequest(BaseModel):
    CertificateAuthorityArn: Arn
    CertificateArn: Arn


class GetCertificateAuthorityCertificateResponse(GetCertificateResponse):
    pass


class GetCertificateAuthorityCertificateRequest(BaseModel):
    CertificateAuthorityArn: Arn


class GetCertificateAuthorityCsrResponse(BaseModel):
    Csr: Optional[CsrBody] = None


class GetCertificateAuthorityCsrRequest(BaseModel):
    CertificateAuthorityArn: Arn


class GetPolicyResponse(BaseModel):
    Policy: Optional[AWSPolicy] = None


class GetPolicyRequest(BaseModel):
    ResourceArn: Arn


class ImportCertificateAuthorityCertificateRequest(BaseModel):
    CertificateAuthorityArn: Arn
    Certificate: CertificateBodyBlob
    CertificateChain: Optional[CertificateChainBlob] = None


class IssueCertificateResponse(BaseModel):
    CertificateArn: Optional[Arn] = None


class ListCertificateAuthoritiesRequest(BaseModel):
    NextToken: Optional[NextToken] = None
    MaxResults: Optional[MaxResults] = None
    ResourceOwner: Optional[ResourceOwner] = None


class ListPermissionsRequest(BaseModel):
    CertificateAuthorityArn: Arn
    NextToken: Optional[NextToken] = None
    MaxResults: Optional[MaxResults] = None


class ListTagsRequest(BaseModel):
    CertificateAuthorityArn: Arn
    NextToken: Optional[NextToken] = None
    MaxResults: Optional[MaxResults] = None


class PutPolicyRequest(BaseModel):
    ResourceArn: Arn
    Policy: AWSPolicy


class RestoreCertificateAuthorityRequest(BaseModel):
    CertificateAuthorityArn: Arn


class RevokeCertificateRequest(BaseModel):
    CertificateAuthorityArn: Arn
    CertificateSerial: String128
    RevocationReason: RevocationReason


class AccessMethod(BaseModel):
    """
    Describes the type and format of extension access. Only one of <code>CustomObjectIdentifier</code> or <code>AccessMethodType</code> may be provided. Providing both results in <code>InvalidArgsException</code>.
    """

    CustomObjectIdentifier: Optional[CustomObjectIdentifier] = None
    AccessMethodType: Optional[AccessMethodType] = None


class GeneralName(BaseModel):
    """
    Describes an ASN.1 X.400 <code>GeneralName</code> as defined in <a href="https://tools.ietf.org/html/rfc5280">RFC 5280</a>. Only one of the following naming options should be provided. Providing more than one option results in an <code>InvalidArgsException</code> error.
    """

    OtherName: Optional[OtherName] = None
    Rfc822Name: Optional[String256] = None
    DnsName: Optional[String253] = None
    DirectoryName: Optional[ASN1Subject] = None
    EdiPartyName: Optional[EdiPartyName] = None
    UniformResourceIdentifier: Optional[String253] = None
    IpAddress: Optional[String39] = None
    RegisteredId: Optional[CustomObjectIdentifier] = None


class AccessDescription(BaseModel):
    """
    Provides access information used by the <code>authorityInfoAccess</code> and <code>subjectInfoAccess</code> extensions described in <a href="https://tools.ietf.org/html/rfc5280">RFC 5280</a>.
    """

    AccessMethod: AccessMethod
    AccessLocation: GeneralName


class AccessDescriptionList(BaseModel):
    __root__: List[AccessDescription]


class RevocationConfiguration(BaseModel):
    """
    Certificate revocation information used by the <a href="https://docs.aws.amazon.com/acm-pca/latest/APIReference/API_CreateCertificateAuthority.html">CreateCertificateAuthority</a> and <a href="https://docs.aws.amazon.com/acm-pca/latest/APIReference/API_UpdateCertificateAuthority.html">UpdateCertificateAuthority</a> actions. Your private certificate authority (CA) can configure Online Certificate Status Protocol (OCSP) support and/or maintain a certificate revocation list (CRL). OCSP returns validation information about certificates as requested by clients, and a CRL contains an updated list of certificates revoked by your CA. For more information, see <a href="https://docs.aws.amazon.com/acm-pca/latest/APIReference/API_RevokeCertificate.html">RevokeCertificate</a> and <a href="https://docs.aws.amazon.com/acm-pca/latest/userguide/revocation-setup.html">Setting up a certificate revocation method</a> in the <i>AWS Certificate Manager Private Certificate Authority (PCA) User Guide</i>.
    """

    CrlConfiguration: Optional[CrlConfiguration] = None
    OcspConfiguration: Optional[OcspConfiguration] = None


class CsrExtensions(BaseModel):
    """
    Describes the certificate extensions to be added to the certificate signing request (CSR).
    """

    KeyUsage: Optional[KeyUsage] = None
    SubjectInformationAccess: Optional[AccessDescriptionList] = None


class TagList(BaseModel):
    __root__: Annotated[List[Tag], Field(max_items=50, min_items=1)]


class GeneralNameList(BaseModel):
    __root__: Annotated[List[GeneralName], Field(max_items=20, min_items=1)]


class Validity(BaseModel):
    """
    <p>Validity specifies the period of time during which a certificate is valid. Validity can be expressed as an explicit date and time when the validity of a certificate starts or expires, or as a span of time after issuance, stated in days, months, or years. For more information, see <a href="https://tools.ietf.org/html/rfc5280#section-4.1.2.5">Validity</a> in RFC 5280.</p> <p>ACM Private CA API consumes the <code>Validity</code> data type differently in two distinct parameters of the <code>IssueCertificate</code> action. The required parameter <code>IssueCertificate</code>:<code>Validity</code> specifies the end of a certificate's validity period. The optional parameter <code>IssueCertificate</code>:<code>ValidityNotBefore</code> specifies a customized starting time for the validity period.</p>
    """

    Value: PositiveLong
    Type: ValidityPeriodType


class PermissionList(BaseModel):
    __root__: Annotated[List[Permission], Field(min_items=0)]


class PolicyQualifierInfoList(BaseModel):
    __root__: Annotated[List[PolicyQualifierInfo], Field(max_items=20, min_items=1)]


class ListPermissionsResponse(BaseModel):
    Permissions: Optional[PermissionList] = None
    NextToken: Optional[NextToken] = None


class ListTagsResponse(BaseModel):
    Tags: Optional[TagList] = None
    NextToken: Optional[NextToken] = None


class TagCertificateAuthorityRequest(BaseModel):
    CertificateAuthorityArn: Arn
    Tags: TagList


class UntagCertificateAuthorityRequest(BaseModel):
    CertificateAuthorityArn: Arn
    Tags: TagList


class UpdateCertificateAuthorityRequest(BaseModel):
    CertificateAuthorityArn: Arn
    RevocationConfiguration: Optional[RevocationConfiguration] = None
    Status: Optional[CertificateAuthorityStatus] = None


class CertificateAuthorityConfiguration(BaseModel):
    """
    Contains configuration information for your private certificate authority (CA). This includes information about the class of public key algorithm and the key pair that your private CA creates when it issues a certificate. It also includes the signature algorithm that it uses when issuing certificates, and its X.500 distinguished name. You must specify this information when you call the <a href="https://docs.aws.amazon.com/acm-pca/latest/APIReference/API_CreateCertificateAuthority.html">CreateCertificateAuthority</a> action.
    """

    KeyAlgorithm: KeyAlgorithm
    SigningAlgorithm: SigningAlgorithm
    Subject: ASN1Subject
    CsrExtensions: Optional[CsrExtensions] = None


class PolicyInformation(BaseModel):
    """
    Defines the X.509 <code>CertificatePolicies</code> extension.
    """

    CertPolicyId: CustomObjectIdentifier
    PolicyQualifiers: Optional[PolicyQualifierInfoList] = None


class CertificatePolicyList(BaseModel):
    __root__: Annotated[List[PolicyInformation], Field(max_items=20, min_items=1)]


class CreateCertificateAuthorityRequest(BaseModel):
    CertificateAuthorityConfiguration: CertificateAuthorityConfiguration
    RevocationConfiguration: Optional[RevocationConfiguration] = None
    CertificateAuthorityType: CertificateAuthorityType
    IdempotencyToken: Optional[IdempotencyToken] = None
    KeyStorageSecurityStandard: Optional[KeyStorageSecurityStandard] = None
    Tags: Optional[TagList] = None


class Extensions(BaseModel):
    """
    Contains X.509 extension information for a certificate.
    """

    CertificatePolicies: Optional[CertificatePolicyList] = None
    ExtendedKeyUsage: Optional[ExtendedKeyUsageList] = None
    KeyUsage: Optional[KeyUsage] = None
    SubjectAlternativeNames: Optional[GeneralNameList] = None


class ApiPassthrough(BaseModel):
    """
    <p>Contains X.509 certificate information to be placed in an issued certificate. An <code>APIPassthrough</code> or <code>APICSRPassthrough</code> template variant must be selected, or else this parameter is ignored. </p> <p>If conflicting or duplicate certificate information is supplied from other sources, ACM Private CA applies <a href="https://docs.aws.amazon.com/acm-pca/latest/userguide/UsingTemplates.html#template-order-of-operations">order of operation rules</a> to determine what information is used.</p>
    """

    Extensions: Optional[Extensions] = None
    Subject: Optional[ASN1Subject] = None


class CertificateAuthority(BaseModel):
    """
    Contains information about your private certificate authority (CA). Your private CA can issue and revoke X.509 digital certificates. Digital certificates verify that the entity named in the certificate <b>Subject</b> field owns or controls the public key contained in the <b>Subject Public Key Info</b> field. Call the <a href="https://docs.aws.amazon.com/acm-pca/latest/APIReference/API_CreateCertificateAuthority.html">CreateCertificateAuthority</a> action to create your private CA. You must then call the <a href="https://docs.aws.amazon.com/acm-pca/latest/APIReference/API_GetCertificateAuthorityCertificate.html">GetCertificateAuthorityCertificate</a> action to retrieve a private CA certificate signing request (CSR). Sign the CSR with your ACM Private CA-hosted or on-premises root or subordinate CA certificate. Call the <a href="https://docs.aws.amazon.com/acm-pca/latest/APIReference/API_ImportCertificateAuthorityCertificate.html">ImportCertificateAuthorityCertificate</a> action to import the signed certificate into AWS Certificate Manager (ACM).
    """

    Arn: Optional[Arn] = None
    OwnerAccount: Optional[AccountId] = None
    CreatedAt: Optional[TStamp] = None
    LastStateChangeAt: Optional[TStamp] = None
    Type: Optional[CertificateAuthorityType] = None
    Serial: Optional[String] = None
    Status: Optional[CertificateAuthorityStatus] = None
    NotBefore: Optional[TStamp] = None
    NotAfter: Optional[TStamp] = None
    FailureReason: Optional[FailureReason] = None
    CertificateAuthorityConfiguration: Optional[
        CertificateAuthorityConfiguration
    ] = None
    RevocationConfiguration: Optional[RevocationConfiguration] = None
    RestorableUntil: Optional[TStamp] = None
    KeyStorageSecurityStandard: Optional[KeyStorageSecurityStandard] = None


class CertificateAuthorities(BaseModel):
    __root__: List[CertificateAuthority]


class DescribeCertificateAuthorityResponse(BaseModel):
    CertificateAuthority: Optional[CertificateAuthority] = None


class IssueCertificateRequest(BaseModel):
    ApiPassthrough: Optional[ApiPassthrough] = None
    CertificateAuthorityArn: Arn
    Csr: CsrBlob
    SigningAlgorithm: SigningAlgorithm
    TemplateArn: Optional[Arn] = None
    Validity: Validity
    ValidityNotBefore: Optional[Validity] = None
    IdempotencyToken: Optional[IdempotencyToken] = None


class ListCertificateAuthoritiesResponse(BaseModel):
    CertificateAuthorities: Optional[CertificateAuthorities] = None
    NextToken: Optional[NextToken] = None
