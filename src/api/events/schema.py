from pydantic import BaseModel
from typing import List

class EventSchema(BaseModel):
    id: int
    page: str | None = None

class EventListSchema(BaseModel):
    results: List[EventSchema]