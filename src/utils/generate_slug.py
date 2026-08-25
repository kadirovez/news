
from slugify import slugify
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.news.posts import Post


async def generate_slug(
    session: AsyncSession,
    title: str,
    exclude_post_id: int | None = None,
) -> str:
    base_slug = slugify(title, max_length=100) or "post"
    slug = base_slug
    counter = 1

    while True:
        query = select(Post.id).where(Post.slug == slug)
        if exclude_post_id is not None:
            query = query.where(Post.id != exclude_post_id)

        existing = await session.scalar(query)
        if existing is None:
            return slug

        counter += 1
        slug = f"{base_slug}-{counter}"
