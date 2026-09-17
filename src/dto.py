import re

from pydantic import BaseModel, Field, field_validator

class CreateUserRequest(BaseModel):
    name: str
    phone_number: str
    height: float = Field(strict=True)
    bio: str | None = None

    @field_validator("phone_number")
    @classmethod
    def validate_phone_number(cls, value: str) -> str:
        if re.fullmatch(r"010-[0-9]{4}-[0-9]{4}", value) is None:
            raise ValueError("phone_number must have the format 010-XXXX-XXXX")
        return value

    @field_validator("bio")
    @classmethod
    def validate_bio(cls, value: str | None) -> str | None:
        if value is not None and len(value) > 500:
            raise ValueError("bio must not exceed 500 characters")
        return value

class UserResponse(CreateUserRequest):
    user_id: int
