from contextlib import asynccontextmanager
from fastapi import FastAPI
from .api.events import router as event_router
from .api.db.session import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)

# Routers
app.include_router(event_router, prefix='/api/events')

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

@app.get('/healthz')
def read_api_health():
    return {'status': 'ok'}