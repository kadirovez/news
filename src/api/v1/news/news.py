
from fastapi import APIRouter, Depends, UploadFile, File, Query
from sqlalchemy.ext.asyncio import AsyncSession

from src.deps.database import get_db
from src.deps.user import get_current_user
from src.models.common import User
from src.schemas.news.news import (
    PostCreate,
    PostUpdate,
    PostListItem,
    PostDetail,
    ImageUploadResponse,
)
from src.services.news.create_post import create_post
from src.services.news.edit_post import edit_post
from src.services.news.delete_post import delete_post
from src.services.news.get_posts import get_posts as get_posts_list
from src.services.news.get_post import view_post
from src.services.news.upload_image import upload_image as upload_image_service

router = APIRouter(prefix='/news', tags=['news'])


@router.get("/", response_model=list[PostListItem])
async def get_posts(
        skip: int = Query(default=0, ge=0),
        limit: int = Query(default=20, ge=1, le=100),
        db: AsyncSession = Depends(get_db),
):
    return await get_posts_list(db=db, skip=skip, limit=limit)


@router.post("/upload-image", response_model=ImageUploadResponse)
async def upload_image_endpoint(
        file: UploadFile = File(...),
        _current_user: User = Depends(get_current_user),
):
    key = await upload_image_service(file=file)
    return ImageUploadResponse(key=key)


@router.get("/{slug}", response_model=PostDetail)
async def view_post_endpoint(
        slug: str,
        db: AsyncSession = Depends(get_db),
):
    return await view_post(db=db, slug=slug)


@router.post("/", response_model=PostDetail)
async def create_post_endpoint(
        data: PostCreate,
        db: AsyncSession = Depends(get_db),
        current_user: User = Depends(get_current_user),
):
    return await create_post(
        db=db,
        data=data,
        current_user=current_user,
    )


@router.patch("/{slug}", response_model=PostDetail)
async def edit_post_endpoint(
        slug: str,
        data: PostUpdate,
        db: AsyncSession = Depends(get_db),
        current_user: User = Depends(get_current_user),
):
    return await edit_post(
        db=db,
        slug=slug,
        data=data,
        current_user=current_user,
    )


@router.delete("/{slug}", response_model=PostDetail)
async def delete_post_endpoint(
        slug: str,
        db: AsyncSession = Depends(get_db),
        current_user: User = Depends(get_current_user),
):
    return await delete_post(
        db=db,
        slug=slug,
        current_user=current_user,
    )
