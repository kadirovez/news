
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.crud.base import CRUDBase
from src.models.common.user import User
from src.models.news.posts import Post
from src.schemas.news.news import PostCreate, PostUpdate
from src.utils.generate_slug import generate_slug


class CRUDPost(CRUDBase[Post, PostCreate, PostUpdate]):
    """ CRUD for news posts"""

    async def get_by_slug(
            self,
            db: AsyncSession,
            slug: str,
    ) -> Post | None:
        query = select(self.model).where(self.model.slug == slug)
        query = self._apply_load_options(query)
        result = await db.execute(query)
        return result.scalar_one_or_none()

    async def get_paginated(
            self,
            db: AsyncSession,
            skip: int = 0,
            limit: int = 100,
    ):
        query = (
            select(self.model)
            .order_by(self.model.created_at.desc())
            .offset(skip)
            .limit(limit)
        )
        query = self._apply_load_options(query)
        result = await db.execute(query)
        return result.scalars().all()

    async def create_for_author(
            self,
            db: AsyncSession,
            obj_in: PostCreate,
            author: User,
    ) -> Post:
        slug = await generate_slug(db, obj_in.title)

        db_obj = Post(
            title=obj_in.title,
            content=obj_in.content,
            preview_image=obj_in.preview_image,
            slug=slug,
            author_id=author.id,
            author_name=f"{author.first_name} {author.last_name}",
        )
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    async def update_by_slug(
            self,
            db: AsyncSession,
            post: Post,
            obj_in: PostUpdate,
    ) -> Post:
        obj_data = obj_in.model_dump(exclude_unset=True)

        if "title" in obj_data and obj_data["title"] != post.title:
            obj_data["slug"] = await generate_slug(
                db,
                obj_data["title"],
                exclude_post_id=post.id,
            )

        for key, value in obj_data.items():
            setattr(post, key, value)

        db.add(post)
        await db.commit()
        await db.refresh(post)
        return post


post_crud = CRUDPost(Post)
