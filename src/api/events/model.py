from sqlmodel import SQLModel, Field
from datetime import datetime, timezone
from typing import Sequence
from sqlalchemy import DateTime

def get_utc_now():
    return datetime.now(timezone.utc).replace(tzinfo=timezone.utc)

class EventModel(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    page: str | None = Field(default=None)
    description: str | None = Field(default=None)
    created_at: datetime = Field(
        default_factory= get_utc_now,
        sa_type=DateTime(timezone=True),  # pyright: ignore[reportArgumentType]
        nullable=False
    )
    updated_at: datetime = Field(
        default_factory= get_utc_now,
        sa_type=DateTime(timezone=True),  # pyright: ignore[reportArgumentType]
        nullable=False
    )

class EventListSchema(SQLModel):
    results: Sequence[EventModel]