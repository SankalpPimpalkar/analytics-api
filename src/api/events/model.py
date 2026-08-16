from sqlmodel import SQLModel, Field
from typing import Sequence

class EventModel(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    page: str | None = Field(default=None)
    description: str | None = Field(default=None) 

class EventListSchema(SQLModel):
    results: Sequence[EventModel]