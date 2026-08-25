
from sqlalchemy.ext.asyncio import AsyncSession

from src.crud.news.news import post_crud


async def get_posts(
        db: AsyncSession,
        skip: int = 0,
        limit: int = 100,
):
    return await post_crud.get_paginated(db=db, skip=skip, limit=limit)
