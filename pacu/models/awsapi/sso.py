# generated by datamodel-codegen:
#   filename:  openapi.yaml
#   timestamp: 2021-12-31T02:58:51+00:00

from __future__ import annotations

from typing import Annotated, Any, List, Optional

from pydantic import BaseModel, Field, SecretStr


class InvalidRequestException(BaseModel):
    __root__: Any


class UnauthorizedException(InvalidRequestException):
    pass


class TooManyRequestsException(InvalidRequestException):
    pass


class ResourceNotFoundException(InvalidRequestException):
    pass


class AccessKeyType(BaseModel):
    __root__: str


class AccessTokenType(BaseModel):
    __root__: SecretStr


class AccountIdType(AccessKeyType):
    pass


class AccountNameType(AccessKeyType):
    pass


class EmailAddressType(BaseModel):
    __root__: Annotated[str, Field(max_length=254, min_length=1)]


class AccountInfo(BaseModel):
    """
    Provides information about your AWS account.
    """

    accountId: Optional[AccountIdType] = None
    accountName: Optional[AccountNameType] = None
    emailAddress: Optional[EmailAddressType] = None


class AccountListType(BaseModel):
    __root__: List[AccountInfo]


class ExpirationTimestampType(BaseModel):
    __root__: int


class RoleNameType(AccessKeyType):
    pass


class GetRoleCredentialsRequest(BaseModel):
    pass


class NextTokenType(AccessKeyType):
    pass


class MaxResultType(BaseModel):
    __root__: Annotated[int, Field(ge=1.0, le=100.0)]


class ListAccountRolesRequest(BaseModel):
    pass


class ListAccountsRequest(BaseModel):
    pass


class LogoutRequest(BaseModel):
    pass


class SecretAccessKeyType(AccessTokenType):
    pass


class SessionTokenType(AccessTokenType):
    pass


class RoleInfo(BaseModel):
    """
    Provides information about the role that is assigned to the user.
    """

    roleName: Optional[RoleNameType] = None
    accountId: Optional[AccountIdType] = None


class ListAccountsResponse(BaseModel):
    nextToken: Optional[NextTokenType] = None
    accountList: Optional[AccountListType] = None


class RoleCredentials(BaseModel):
    """
    Provides information about the role credentials that are assigned to the user.
    """

    accessKeyId: Optional[AccessKeyType] = None
    secretAccessKey: Optional[SecretAccessKeyType] = None
    sessionToken: Optional[SessionTokenType] = None
    expiration: Optional[ExpirationTimestampType] = None


class RoleListType(BaseModel):
    __root__: List[RoleInfo]


class GetRoleCredentialsResponse(BaseModel):
    roleCredentials: Optional[RoleCredentials] = None


class ListAccountRolesResponse(BaseModel):
    nextToken: Optional[NextTokenType] = None
    roleList: Optional[RoleListType] = None
