from fastapi import APIRouter
from .schema import EventSchema, EventListSchema
from ..db.config import DATABASE_URL

router = APIRouter()

@router.get("/")
def read_events() -> EventListSchema:
    print("DATABASE_URL", DATABASE_URL)
    return EventListSchema(results=[])

@router.post("/")
def create_event(event: EventSchema) -> EventSchema:
    return EventSchema(**event.dict())

@router.get("/{event_id}")
def get_event(event_id: int) -> EventSchema:
    return EventSchema(id=event_id)

@router.delete("/{event_id}")
def delete_event(event_id: int) -> EventSchema:
    return EventSchema(id=event_id)