
from typing import Annotated

from fastapi import APIRouter, Depends, Form
from sqlalchemy.ext.asyncio import AsyncSession

from src.deps.database import get_db
from src.schemas.common.application import ApplicationData
from src.services.common import application_service

router = APIRouter(prefix="/application", tags=["application"])


@router.post("/")
async def upload_application(
        data: Annotated[ApplicationData, Form()],
        # data: ApplicationData = Depends(ApplicationData.as_form),
        db: AsyncSession = Depends(get_db),
):
    return await application_service.upload_application(db,data)
