from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from .model import EventModel, EventListSchema, get_utc_now
from ..db.session import get_session
from ..db.config import DATABASE_URL

router = APIRouter()

@router.get("/", response_model=EventListSchema)
def read_events(session: Session = Depends(get_session)) -> EventListSchema:
    query = select(EventModel).limit(10)
    results = session.exec(query).all()
    print("DATABASE_URL", DATABASE_URL)
    return EventListSchema(results=results)

@router.post("/", response_model=EventModel)
def create_event(event: EventModel, session: Session = Depends(get_session)):
    data = event.model_dump()
    obj = EventModel.model_validate(data)
    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj

@router.get("/{event_id}", response_model=EventModel)
def get_event(event_id: int, session: Session = Depends(get_session)):
    query = select(EventModel).where(EventModel.id == event_id)
    result = session.exec(query).first()

    if not result:
        raise HTTPException(status_code=404, detail="Event not found")

    return result

@router.put("/{event_id}", response_model=EventModel)
def update_event(event_id: int, event: EventModel, session: Session = Depends(get_session)):
    query = select(EventModel).where(EventModel.id == event_id)
    result = session.exec(query).first()

    if not result:
        raise HTTPException(status_code=404, detail="Event not found")

    data = event.model_dump()
    for k,v in data.items():
        if k == 'id':
            continue
        setattr(result, k, v)
    setattr(result, 'updated_at', get_utc_now())
    session.add(data)
    session.commit()
    session.refresh(result)
    return result

@router.delete("/{event_id}")
def delete_event(event_id: int) -> EventModel:
    return EventModel(id=event_id)