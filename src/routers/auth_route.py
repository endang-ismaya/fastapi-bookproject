from fastapi import APIRouter
from starlette import status
from src.models.UserRequest import CreateUserRequest
from src.database.models import Users
from src.database.db_dependency import db_dependency
from passlib.context import CryptContext

router = APIRouter()

bcrypt_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.post("/auth/create", status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependency, create_user_request: CreateUserRequest):
    cr_user_model = Users(
        email=create_user_request.email,
        first_name=create_user_request.first_name,
        last_name=create_user_request.last_name,
        role=create_user_request.role,
        hashed_password=bcrypt_ctx.hash(create_user_request.password),
        is_active=True,
    )

    db.add(cr_user_model)
    db.commit()
