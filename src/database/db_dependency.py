from typing import Annotated

from fastapi import Depends
from src.database.db import engine, SessionLocal
import src.database.models as models
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]
