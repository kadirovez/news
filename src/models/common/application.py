
from datetime import datetime

from sqlalchemy import String, Text, LargeBinary, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column

from src.models.base import BaseDataModel


class Application(BaseDataModel):

    __tablename__ = "application"


    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    surname: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    email: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    phone: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    message: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    resume_filename: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    resume_content_type: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    resume_data: Mapped[bytes | None] = mapped_column(
        LargeBinary,
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )
