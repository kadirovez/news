
from sqlalchemy.ext.asyncio import AsyncSession

from src.crud.news.news import post_crud
from src.models.common import User
from src.models.news.posts import Post
from src.schemas.news.news import PostCreate


async def create_post(
        db: AsyncSession,
        data: PostCreate,
        current_user: User,
) -> Post:
    """ Creates post with auto generated slug """
    return await post_crud.create_for_author(
        db=db,
        obj_in=data,
        author=current_user,
    )
