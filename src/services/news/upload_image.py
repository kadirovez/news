
from fastapi import HTTPException, UploadFile

from src.utils.s3 import upload_image_to_s3, validate_image_file


async def upload_image(file: UploadFile) -> str:
    if not file.filename:
        raise HTTPException(status_code=400, detail="Filename is required")

    content = await file.read()
    if not content:
        raise HTTPException(status_code=400, detail="Empty file")

    extension = validate_image_file(file, content)
    return upload_image_to_s3(content, extension)
