
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.crud.news.news import post_crud
from src.models.news.posts import Post


async def view_post(
        db: AsyncSession,
        slug: str,
) -> Post:
    post = await post_crud.get_by_slug(db=db, slug=slug)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return post
