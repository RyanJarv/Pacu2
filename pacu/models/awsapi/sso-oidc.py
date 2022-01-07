# generated by datamodel-codegen:
#   filename:  openapi.yaml
#   timestamp: 2021-12-31T02:58:54+00:00

from __future__ import annotations

from typing import Annotated, Any, List, Optional

from pydantic import BaseModel


class Scope(BaseModel):
    __root__: str


class InvalidRequestException(BaseModel):
    __root__: Any


class InvalidClientException(InvalidRequestException):
    pass


class InvalidGrantException(InvalidRequestException):
    pass


class UnauthorizedClientException(InvalidRequestException):
    pass


class UnsupportedGrantTypeException(InvalidRequestException):
    pass


class InvalidScopeException(InvalidRequestException):
    pass


class AuthorizationPendingException(InvalidRequestException):
    pass


class SlowDownException(InvalidRequestException):
    pass


class AccessDeniedException(InvalidRequestException):
    pass


class ExpiredTokenException(InvalidRequestException):
    pass


class InternalServerException(InvalidRequestException):
    pass


class InvalidClientMetadataException(InvalidRequestException):
    pass


class AccessToken(Scope):
    pass


class AuthCode(Scope):
    pass


class ClientId(Scope):
    pass


class ClientName(Scope):
    pass


class ClientSecret(Scope):
    pass


class ClientType(Scope):
    pass


class GrantType(Scope):
    pass


class DeviceCode(Scope):
    pass


class RefreshToken(Scope):
    pass


class Scopes(BaseModel):
    __root__: List[Scope]


class URI(Scope):
    pass


class CreateTokenRequest(BaseModel):
    clientId: ClientId
    clientSecret: ClientSecret
    grantType: GrantType
    deviceCode: DeviceCode
    code: Optional[AuthCode] = None
    refreshToken: Optional[RefreshToken] = None
    scope: Optional[Scopes] = None
    redirectUri: Optional[URI] = None


class TokenType(Scope):
    pass


class ExpirationInSeconds(BaseModel):
    __root__: int


class IdToken(Scope):
    pass


class IntervalInSeconds(ExpirationInSeconds):
    pass


class LongTimeStampType(ExpirationInSeconds):
    pass


class RegisterClientRequest(BaseModel):
    clientName: ClientName
    clientType: ClientType
    scopes: Optional[Scopes] = None


class StartDeviceAuthorizationRequest(BaseModel):
    clientId: ClientId
    clientSecret: ClientSecret
    startUrl: URI


class UserCode(Scope):
    pass


class CreateTokenResponse(BaseModel):
    accessToken: Optional[AccessToken] = None
    tokenType: Optional[TokenType] = None
    expiresIn: Optional[ExpirationInSeconds] = None
    refreshToken: Optional[RefreshToken] = None
    idToken: Optional[IdToken] = None


class RegisterClientResponse(BaseModel):
    clientId: Optional[ClientId] = None
    clientSecret: Optional[ClientSecret] = None
    clientIdIssuedAt: Optional[LongTimeStampType] = None
    clientSecretExpiresAt: Optional[LongTimeStampType] = None
    authorizationEndpoint: Optional[URI] = None
    tokenEndpoint: Optional[URI] = None


class StartDeviceAuthorizationResponse(BaseModel):
    deviceCode: Optional[DeviceCode] = None
    userCode: Optional[UserCode] = None
    verificationUri: Optional[URI] = None
    verificationUriComplete: Optional[URI] = None
    expiresIn: Optional[ExpirationInSeconds] = None
    interval: Optional[IntervalInSeconds] = None