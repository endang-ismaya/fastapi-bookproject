from fastapi import FastAPI, Path, Query, HTTPException
from starlette import status
from src.models.BookRequest import BookRequest, Book

app = FastAPI()


BOOKS = [
    Book(1, "Computer Science Pro", "Endang", "A computer science first book", 5, 2012),
    Book(2, "Be Fast with FastAPI", "Endang", "A Great Book", 5, 2023),
    Book(3, "Mastering Django", "John", "A take a look book", 5, 2022),
    Book(4, "Learn Flask", "Mary", "A Flask web app", 3, 2000),
    Book(5, "Python API", "Jane", "Many things to do with API", 3, 2021),
    Book(
        6, "Python Object Oriented Programming", "Mary", "OOP at first glance", 4, 2019
    ),
]


def find_book_id(book: Book):
    if len(BOOKS) > 0:
        book.id = BOOKS[-1].id + 1
    else:
        book.id = 1

    return book


@app.get("/books", status_code=status.HTTP_200_OK)
async def read_books():
    return BOOKS


@app.get("/books/{book_id}", status_code=status.HTTP_200_OK)  # by URL
async def get_book(book_id: int = Path(gt=0)):
    book: Book = next((item for item in BOOKS if item.id == book_id), None)

    if book is None:
        raise HTTPException(status_code=404, detail="Item not found")

    return book


@app.get("/books/q1/", status_code=status.HTTP_200_OK)  # by Query Parameters
async def get_books_from_rating(book_rating: int = Query(gt=0, lt=6)):
    books = [item for item in BOOKS if item.rating == book_rating]
    return books


@app.get("/books/q2/", status_code=status.HTTP_200_OK)  # by Query Parameters
async def get_books_from_published_date(published_date: int = Query(gt=1999, lt=2099)):
    books = [item for item in BOOKS if item.published_date == published_date]
    return books


@app.post("/books/create", status_code=status.HTTP_201_CREATED)
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(find_book_id(new_book))


@app.put("/books/update", status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book: BookRequest):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book
            return {"msg": "book has been updated"}

    raise HTTPException(status_code=404, detail="Item not found")


@app.delete("/books/delete/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int = Path(gt=0)):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            return {"msg": "book has been deleted"}

    raise HTTPException(status_code=404, detail="Item not found")
