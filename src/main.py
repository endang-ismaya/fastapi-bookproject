from fastapi import FastAPI
from src.routers import auth_route, todo_route
from src.database.db import engine
import src.database.models as models

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

# auth route
app.include_router(auth_route.router)
app.include_router(todo_route.router)
