
from typing import TYPE_CHECKING

from sqlalchemy import String, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import BaseDataModel

if TYPE_CHECKING:
    from src.models.common.user import User


class Post(BaseDataModel):
    __tablename__ = "post"

    title: Mapped[str] = mapped_column(
        String(256),
        nullable=False,
    )

    content: Mapped[dict] = mapped_column(
        JSONB,
        nullable=False,
        default=dict,
    )

    slug: Mapped[str] = mapped_column(
        String(256),
        nullable=False,
        index=True,
        unique=True,
    )

    author_id: Mapped[int | None] = mapped_column(
        ForeignKey('user.id', ondelete='SET NULL'),
        nullable=True,
        index=True,
    )

    author: Mapped["User | None"] = relationship(
        "User",
        back_populates="posts",
    )

    author_name: Mapped[str] = mapped_column(
        String(256),
        nullable=False,
    )

    preview_image: Mapped[str | None] = mapped_column(
        String(512),
        nullable=True,
    )
