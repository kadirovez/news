
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.crud.news.news import post_crud
from src.models.common import User
from src.models.news.posts import Post
from src.schemas.news.news import PostUpdate
from src.services.news import check_post_edit_permission


async def edit_post(
        db: AsyncSession,
        slug: str,
        data: PostUpdate,
        current_user: User,
) -> Post:
    post = await post_crud.get_by_slug(db=db, slug=slug)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")

    check_post_edit_permission(post, current_user)

    return await post_crud.update_by_slug(db=db, post=post, obj_in=data)
