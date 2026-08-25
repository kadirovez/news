
from fastapi import HTTPException

from src.core.settings import settings
from src.models.common import User
from src.models.news.posts import Post


def check_post_edit_permission(post: Post, current_user: User) -> None:
    if post.author_id != current_user.id and settings.author_rights:
        raise HTTPException(
            status_code=403,
            detail="You do not have permission to modify this post",
        )
