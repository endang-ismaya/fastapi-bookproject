from fastapi import FastAPI, Body

app = FastAPI()

BOOKS = [
    {"title": "Title One", "author": "Author One", "category": "science"},
    {"title": "Title Two", "author": "Author Two", "category": "science"},
    {"title": "Title Three", "author": "Author Three", "category": "history"},
    {"title": "Title Four", "author": "Author Four", "category": "math"},
    {"title": "Title Five", "author": "Author Five", "category": "math"},
    {"title": "Title Six", "author": "Author Two", "category": "math"},
]


@app.get("/books")
async def read_all_books():
    print(BOOKS)
    return BOOKS


@app.get("/books/{book_title}")
async def read_book_by_title(book_title: str):
    for book in BOOKS:
        if book.get("title").casefold() == book_title.casefold():
            return book

    return {"message": "book title not found"}


@app.get("/books/")
async def read_cat_by_query(category: str):
    """
    http://127.0.0.1:8000/books/?category=science
    result:
    [
        {
            "title": "Title One",
            "author": "Author One",
            "category": "science"
        },
        {
            "title": "Title Two",
            "author": "Author Two",
            "category": "science"
        }
    ]
    """
    books = [
        book for book in BOOKS if book.get("category").casefold() == category.casefold()
    ]
    return books


@app.get("/books/{book_author}/")
async def read_author_category_by_query(book_author: str, category: str):
    """
    http://127.0.0.1:8000/books/author%20two/?category=science
    result:
    [
        {
            "title": "Title Two",
            "author": "Author Two",
            "category": "science"
        }
    ]
    """
    books = [
        book
        for book in BOOKS
        if book.get("author").casefold() == book_author.casefold()
        and book.get("category").casefold() == category.casefold()
    ]
    return books


# create a book
@app.post("/books/create")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)


# update a book
@app.put("/books/update")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == updated_book.get("title").casefold():
            BOOKS[i] = updated_book


# delete a book
@app.delete("/books/delete/{book_title}")
async def delete_book(book_title: str):
    print(book_title)
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == book_title.casefold():
            BOOKS.pop(i)
            break
