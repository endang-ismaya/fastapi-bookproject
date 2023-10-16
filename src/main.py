from fastapi import FastAPI
import src.database.models as models
from src.database.db import engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)
