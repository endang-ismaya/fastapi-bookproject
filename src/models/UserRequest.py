from pydantic import BaseModel


class CreateUserRequest(BaseModel):
    email: str
    first_name: str
    last_name: str
    password: str
    role: str
