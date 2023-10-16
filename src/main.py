from typing import Annotated
from fastapi import FastAPI, Depends
import src.database.models as models
from src.database.db import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@app.get("/")
async def read_all_todos(db: db_dependency):
    return db.query(models.Todos).all()
