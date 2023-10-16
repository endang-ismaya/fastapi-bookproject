from typing import Optional
from pydantic import BaseModel, Field


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self, id, title, author, description, rating) -> None:
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating


class BookRequest(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=3)
    author: str = Field(min_length=3)
    description: str = Field(min_length=3, max_length=100)
    rating: int = Field(gt=-1, lt=6)

    class Config:
        # Example Value on swagger API
        json_schema_extra = {
            "example": {
                "title": "A new book",
                "author": "Endang",
                "description": "A new description of a book",
                "rating": "5",
            }
        }
