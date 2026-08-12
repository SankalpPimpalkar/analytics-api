from fastapi import APIRouter
from .model import EventModel, EventListSchema
from ..db.config import DATABASE_URL

router = APIRouter()

@router.get("/")
def read_events() -> EventListSchema:
    print("DATABASE_URL", DATABASE_URL)
    return EventListSchema(results=[])

@router.post("/")
def create_event(event: EventModel) -> EventModel:
    return EventModel(**event.dict())

@router.get("/{event_id}")
def get_event(event_id: int) -> EventModel:
    return EventModel(id=event_id)

@router.delete("/{event_id}")
def delete_event(event_id: int) -> EventModel:
    return EventModel(id=event_id)