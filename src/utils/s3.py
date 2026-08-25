
import uuid

import boto3
from botocore.config import Config
from botocore.exceptions import ClientError
from fastapi import HTTPException, UploadFile

from src.core.settings import settings

ALLOWED_IMAGE_CONTENT_TYPES = {
    "image/jpeg": ".jpg",
    "image/png": ".png",
    "image/webp": ".webp",
    "image/gif": ".gif",
}


def get_s3_client():
    return boto3.client(
        "s3",
        endpoint_url=settings.s3_endpoint,
        aws_access_key_id=settings.s3_access_key,
        aws_secret_access_key=settings.s3_secret_key,
        region_name=settings.s3_region_name,
        config=Config(signature_version="s3v4"),
        verify=False,
    )


def validate_image_file(file: UploadFile, content: bytes) -> str:
    content_type = file.content_type or ""
    if content_type not in ALLOWED_IMAGE_CONTENT_TYPES:
        raise HTTPException(
            status_code=400,
            detail="Unsupported image type. Allowed: JPEG, PNG, WebP, GIF",
        )

    max_size = settings.image_max_size_mb * 1024 * 1024
    if len(content) > max_size:
        raise HTTPException(
            status_code=400,
            detail=f"Image size exceeds {settings.image_max_size_mb} MB limit",
        )

    return ALLOWED_IMAGE_CONTENT_TYPES[content_type]


def upload_image_to_s3(content: bytes, extension: str) -> str:
    key = f"news/images/{uuid.uuid4().hex}{extension}"

    try:
        client = get_s3_client()
        client.put_object(
            Bucket=settings.s3_bucket,
            Key=key,
            Body=content,
            ContentType=_content_type_for_extension(extension),
        )
    except ClientError as exc:
        raise HTTPException(
            status_code=502,
            detail="Failed to upload image to storage",
        ) from exc

    return key


def _content_type_for_extension(extension: str) -> str:
    for content_type, ext in ALLOWED_IMAGE_CONTENT_TYPES.items():
        if ext == extension:
            return content_type
    return "application/octet-stream"
