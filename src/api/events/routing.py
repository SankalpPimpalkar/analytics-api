from fastapi import APIRouter
from .schema import EventSchema, EventListSchema

router = APIRouter()

@router.get("/")
def read_events() -> EventListSchema:
    return EventListSchema(results=[])

@router.post("/")
def create_event(event: EventSchema) -> EventSchema:
    return EventSchema(id=event.id)

@router.get("/{event_id}")
def get_event(event_id: int) -> EventSchema:
    return EventSchema(id=event_id)

@router.delete("/{event_id}")
def delete_event(event_id: int) -> EventSchema:
    return EventSchema(id=event_id)