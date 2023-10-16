from fastapi import FastAPI

from src.models.BookRequest import BookRequest, Book

app = FastAPI()


BOOKS = [
    Book(1, "Computer Science Pro", "Endang", "A computer science first book", 5),
    Book(2, "Be Fast with FastAPI", "Endang", "A Great Book", 5),
    Book(3, "Mastering Django", "John", "A take a look book", 5),
    Book(4, "Learn Flask", "Mary", "A Flask web app", 3),
    Book(5, "Python API", "Jane", "Many things to do with API", 3),
    Book(
        6,
        "Python Object Oriented Programming",
        "Mary",
        "OOP at first glance",
        4,
    ),
]


def find_book_id(book: Book):
    if len(BOOKS) > 0:
        book.id = BOOKS[-1].id + 1
    else:
        book.id = 1

    return book


@app.get("/books")
async def read_books():
    return BOOKS


@app.get("/books/{book_id}")
async def get_book(book_id: int):
    return next((item for item in BOOKS if item.id == book_id), None)


@app.post("/books/create")
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(find_book_id(new_book))
