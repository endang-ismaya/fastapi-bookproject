from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class CreateUserRequest(BaseModel):
    email: str
    first_name: str
    last_name: str
    password: str
    role: str
