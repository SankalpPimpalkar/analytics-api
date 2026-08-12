import sqlmodel
from sqlmodel import SQLModel
from .config import DATABASE_URL

if DATABASE_URL == "":
    raise NotImplemented("DATABASE_URL not set")

engine = sqlmodel.create_engine(DATABASE_URL)

def init_db():
    print("Creating Database")
    SQLModel.metadata.create_all(engine)