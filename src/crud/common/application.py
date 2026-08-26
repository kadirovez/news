
from src.models.common.application import Application
from src.schemas.common.application import ApplicationData


async def create_application(
        db,
        data: ApplicationData,
        resume_bytes: bytes | None = None,
) -> Application:
    application = Application(
        name=data.name,
        surname=data.surname,
        email=data.email,
        phone=data.phone,
        message=data.message,
        resume_filename=data.resume.filename if data.resume else None,
        resume_content_type=data.resume.content_type if data.resume else None,
        resume_data=resume_bytes,
    )
    db.add(application)
    await db.commit()
    await db.refresh(application)
    return application

