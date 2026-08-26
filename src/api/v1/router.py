
from fastapi import APIRouter

from src.api.v1.auth.login import router as login_router
from src.api.v1.auth.registration import router as registration_router
from src.api.v1.news.news import router as news_router
from src.api.v1.common.application import router as application_router

api_router = APIRouter()
api_router.include_router(registration_router)
api_router.include_router(login_router)
api_router.include_router(news_router)
api_router.include_router(application_router)
