
from typing import Annotated

from fastapi import UploadFile, File, Form
from pydantic import BaseModel, field_validator

from src.schemas.fields import NAME_FIELD, EMAIL_FIELD, PHONE_FIELD


class ApplicationData(BaseModel):

    name: NAME_FIELD
    surname: NAME_FIELD
    email: EMAIL_FIELD
    phone: PHONE_FIELD
    resume: Annotated[UploadFile, File()] | None = None
    message: str | None = None

    @field_validator("resume", mode="before")
    @classmethod
    def empty_resume_to_none(cls, value):
        if value == "":
            return None
        return value

    # @classmethod
    # def as_form(
    #     cls,
    #     name: Annotated[str, Form()],
    #     surname: Annotated[str, Form()],
    #     email: Annotated[str, Form()],
    #     phone: Annotated[str, Form()],
    #     message: Annotated[str | None, Form()] = None,
    #     resume: Annotated[UploadFile | None, File()] = None,
    # ) -> "ApplicationData":
    #     return cls(
    #         name=name,
    #         surname=surname,
    #         email=email,
    #         phone=phone,
    #         message=message,
    #         resume=resume,
    #     )