# from datetime import datetime
# from typing import Optional
#
# from pydantic import BaseModel, Field, field_validator, EmailStr
# from pydantic_extra_types.phone_numbers import PhoneNumber
#
# from src.core.settings import settings
# from src.schemas.auth.base import CreateSessionSchema
# from src.schemas.base import StatusResponseSchema, BaseResponseSchema
# from src.schemas.fields import USERNAME_FIELD, OTP_FIELD, EMAIL_FIELD, PASSWORD_FIELD
# from src.utils.enum import MFAMethod
# from src.utils.validator import validate_password_policy
#
#
# class ForgotPasswordUsernameRequest(BaseModel):
#     username: USERNAME_FIELD
#
#
# class ForgotPasswordFirstMFAMethodRequest(BaseModel):
#     first_mfa_method: MFA_METHOD_FIELD
#
#
# class ForgotPasswordSecondMFAMethodRequest(BaseModel):
#     second_mfa_method: MFA_METHOD_FIELD
#
#
# class ForgotPasswordTOTPRequest(BaseModel):
#     totp_code: TOTP_FIELD
#
#
# class ForgotPasswordPhoneRequest(BaseModel):
#     phone: PHONE_FIELD
#
#
# class ForgotPasswordPhoneOTPRequest(BaseModel):
#     phone_code_sent: OTP_FIELD
#
#
# class ForgotPasswordEmailRequest(BaseModel):
#     email: EMAIL_FIELD
#
#
# class ForgotPasswordEmailOTPRequest(BaseModel):
#     email_code_sent: OTP_FIELD
#
#
# class ForgotPasswordPasswordRequest(BaseModel):
#     password: PASSWORD_FIELD
#
#
# class ForgotPasswordConfirmPasswordRequest(BaseModel):
#     confirm_password: PASSWORD_FIELD
#
#
# class ForgotPasswordUsernameResponse(BaseResponseSchema):
#     phone: Optional[str]
#     email: Optional[str]
#
#
# class ForgotPasswordSendOTPResponse(BaseResponseSchema):
#     otp_code_id: str
#     otp_code_expire_at: datetime
#
#
# class ForgotPasswordUpdate(BaseModel):
#     user_id: Optional[int] = None
#     password: Optional[str] = None
#     password_is_confirmed: Optional[bool] = None
#     first_mfa_method: Optional[MFAMethod] = None
#     first_mfa_method_is_confirmed: Optional[bool] = None
#     second_mfa_method: Optional[MFAMethod] = None
#     second_mfa_method_is_confirmed: Optional[bool] = None
#     totp_code_is_confirmed: Optional[bool] = None
#     phone: Optional[str] = None
#     phone_code_sent: Optional[str] = None
#     phone_code_id: Optional[str] = None
#     phone_code_expire_at: Optional[datetime] = None
#     phone_code_is_confirmed: Optional[bool] = None
#     email: Optional[str] = None
#     email_code_sent: Optional[str] = None
#     email_code_id: Optional[str] = None
#     email_code_expire_at: Optional[datetime] = None
#     email_code_is_confirmed: Optional[bool] = None
#     is_completed: Optional[bool] = None
