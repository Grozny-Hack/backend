import uuid
import phonenumbers
from enum import StrEnum

from pydantic import EmailStr

from vizme.config import settings
from vizme.protocol import BaseModel
from pydantic.validators import strict_str_validator


class PhoneNumber(str):
    """Phone Number Pydantic type, using google's phonenumbers"""

    @classmethod
    def __get_validators__(cls):
        yield strict_str_validator
        yield cls.validate

    @classmethod
    def validate(cls, v: str):
        v = v.strip().replace(" ", "")

        try:
            parsed_number = phonenumbers.parse(v)
        except phonenumbers.phonenumberutil.NumberParseException:
            raise ValueError("invalid phone number format")

        return cls(phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164))


class TokenRequestView(BaseModel):
    access_token: str
    refresh_token: str


class TokenResponseView(BaseModel):
    access_token: str
    refresh_token: str
    exp: int


class TokenType(StrEnum):
    ACCESS = "ACCESS"
    REFRESH = "REFRESH"


class UserLoginView(BaseModel):
    email: EmailStr
    password: str


class AccessTokenView(BaseModel):
    iss: str = settings.APP_NAME
    sub: str | uuid.UUID
    exp: int
    email: EmailStr
    first_name: str | None
    last_name: str | None


class RefreshTokenView(BaseModel):
    iss: str = settings.APP_NAME
    sub: str | uuid.UUID
    exp: int


class UpdateProfileView(BaseModel):
    first_name: str | None
    last_name: str | None
    picture_url: str | None
    phone: PhoneNumber | None
    address: str | None
    ip_or_ur_face: int | None


class UserProfileView(BaseModel):
    first_name: str | None
    last_name: str | None
    picture_url: str | None
    email: str
    phone: PhoneNumber | None
    address: str | None
    ip_or_ur_face: int | None
