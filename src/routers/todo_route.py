from fastapi import APIRouter, HTTPException, Path
from starlette import status
from src.database.db_dependency import db_dependency
from src.models.TodoRequest import TodoRequest
import src.database.models as models

router = APIRouter(prefix="/todos", tags=["todos"])


@router.get("/", status_code=status.HTTP_200_OK)
async def get_todos(db: db_dependency):
    return db.query(models.Todos).all()


@router.get("/{todo_id}", status_code=status.HTTP_200_OK)
async def get_todo(db: db_dependency, todo_id: int = Path(gt=0)):
    todo_model = db.query(models.Todos).filter(models.Todos.id == todo_id).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail="Todo not found.")

    return todo_model


# Create Todo
@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_todo(db: db_dependency, todo_request: TodoRequest):
    todo_model = models.Todos(**todo_request.model_dump())

    db.add(todo_model)
    db.commit()


@router.put("/{todo_id}/update", status_code=status.HTTP_204_NO_CONTENT)
async def update_todo(
    db: db_dependency, todo_request: TodoRequest, todo_id: int = Path(gt=0)
):
    todo_model = db.query(models.Todos).filter(models.Todos.id == todo_id).first()

    if todo_model is None:
        raise HTTPException(status_code=404, detail="Todo not found.")

    todo_model.title = todo_request.title
    todo_model.description = todo_request.description
    todo_model.priority = todo_request.priority
    todo_model.complete = todo_request.complete
    db.add(todo_model)
    db.commit()


@router.delete("/{todo_id}/delete", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(db: db_dependency, todo_id: int = Path(gt=0)):
    todo_model = db.query(models.Todos).filter(models.Todos.id == todo_id).first()

    if todo_model is None:
        raise HTTPException(status_code=404, detail="Todo not found.")

    db.query(models.Todos).filter(models.Todos.id == todo_id).delete()
    db.commit()
