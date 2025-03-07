from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI()


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    published_date: int

    def __init__(self, id, title, author, description, rating, published_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date


class BookRequest(BaseModel):
    id: Optional[int] = Field(decription="Id is not needed on create", default=None)
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=6)
    published_date: int = Field()

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "A new book",
                "author": "codingwithroby",
                "description": "A very nice book!",
                "rating": 5,
                "published_date": 2003,
            }
        }
    }


BOOKS = [
    Book(1, "Computer Science Pro", "codingwithroby", "A very nice book!", 5, 1999),
    Book(2, "Be fast with FastAPI", "codingwithroby", "A great book!", 5, 2000),
    Book(3, "Master Endpoints", "codingwithroby", "A awesome book!", 5, 2003),
    Book(4, "HP1", "Author 1", "lorem", 3, 2005),
    Book(5, "HP2", "Author 2", "lorem", 2, 2003),
    Book(6, "HP3", "Author 3", "lorem", 1, 2003),
]


@app.get("/books")
async def read_all_books():
    return BOOKS


@app.get("/books/{book_id}")
async def read_book(book_id: int):
    for book in BOOKS:
        if book.id == book_id:
            return book


@app.get("/books/")
async def fetch_book_by_rating(book_rating: int):
    books_to_return = []
    for book in BOOKS:
        if book.rating == book_rating:
            books_to_return.append(book)
    return books_to_return


@app.get("/books/published_date/")
async def fetch_book_by_published_date(published_date: int):
    books_to_return = []
    for book in BOOKS:
        if book.published_date == published_date:
            books_to_return.append(book)
    return books_to_return


@app.post("/create_book")
async def create_book(create_book_request: BookRequest):
    new_book = Book(**create_book_request.model_dump())
    BOOKS.append(find_book_id(new_book))


def find_book_id(book: Book):
    if len(BOOKS) > 0:
        book.id = BOOKS[-1].id + 1
    else:
        book.id = 1
    return book


@app.put("/books/update_book")
async def update_book(update_book_request: BookRequest):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == update_book_request.id:
            BOOKS[i] = update_book_request


@app.delete("/books/delete/")
async def delete_book(book_id: int):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            break
