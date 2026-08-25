# from datetime import datetime
# from typing import Optional
#
# from pydantic import BaseModel
#
# from src_old.schemas.base import  BaseResponseSchema
# from src_old.schemas.fields import RECOVERY_METHOD_FIELD, PHONE_FIELD, OTP_FIELD, EMAIL_FIELD
# from src_old.utils.enum import RecoveryMethod
#
#
# class ForgotUsernameRecoveryMethodRequest(BaseModel):
#     recovery_method: RECOVERY_METHOD_FIELD
#
#
# class ForgotUsernamePhoneRequest(BaseModel):
#     phone: PHONE_FIELD
#
#
# class ForgotUsernamePhoneOTPRequest(BaseModel):
#     phone_code_sent: OTP_FIELD
#
#
# class ForgotUsernameEmailRequest(BaseModel):
#     email: EMAIL_FIELD
#
#
# class ForgotUsernameEmailOTPRequest(BaseModel):
#     email_code_sent: OTP_FIELD
#
#
# class ForgotUsernameSendOTPResponse(BaseResponseSchema):
#     otp_code_id: str
#     otp_code_expire_at: datetime
#
#
# class ForgotUsernameFinish(BaseResponseSchema):
#     username: str
#     first_name: str
#     last_name: str
#
#
# class ForgotUsernameUpdate(BaseModel):
#     recovery_method: Optional[RecoveryMethod] = None
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
#     user_id: Optional[int] = None
#     is_completed: Optional[bool] = None
