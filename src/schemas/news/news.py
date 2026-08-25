
from datetime import datetime

from pydantic import BaseModel, ConfigDict


class PostCreate(BaseModel):
    title: str
    content: dict
    preview_image: str | None = None


class PostUpdate(BaseModel):
    title: str | None = None
    content: dict | None = None
    preview_image: str | None = None


class PostListItem(BaseModel):
    title: str
    preview_image: str | None
    author_name: str
    created_at: datetime
    slug: str

    model_config = ConfigDict(from_attributes=True)


class PostDetail(BaseModel):
    id: int
    title: str
    content: dict
    slug: str
    author_id: int | None
    author_name: str
    preview_image: str | None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class ImageUploadResponse(BaseModel):
    key: str
