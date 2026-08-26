
from fastapi import HTTPException

from src.crud.common.application import create_application
from src.models.common.application import Application
from src.schemas.common.application import ApplicationData


ALLOWED_RESUME_TYPES = {
    "application/pdf",
    "application/msword",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
}

MAX_RESUME_SIZE = 10 * 1024 * 1024  # 10 MB

async def upload_application(db, data: ApplicationData) -> Application:
    resume_bytes = None

    if data.resume is not None:
        if data.resume.content_type not in ALLOWED_RESUME_TYPES:
            raise HTTPException(status_code=400, detail="Unsupported resume format")

        resume_bytes = await data.resume.read()
        print(f"DEBUG: resume_bytes length = {len(resume_bytes) if resume_bytes else 0}") # temporarily

        if not resume_bytes:
            raise HTTPException(status_code=400, detail="Empty resume file")

        if len(resume_bytes) > MAX_RESUME_SIZE:
            raise HTTPException(status_code=400, detail="Resume file too large")

    return await create_application(db, data, resume_bytes)