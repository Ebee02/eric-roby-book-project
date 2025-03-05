from fastapi import Body, FastAPI

app = FastAPI()


class Books:
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating


BOOKS = [
    Books(1, "Computer Science Pro", "codingwithroby", "A very nice book!", "5"),
    Books(2, "Be fast with FastAPI", "codingwithroby", "A great book!", "5"),
    Books(3, "Master Endpoints", "codingwithroby", "A awesome book!", "5"),
    Books(4, "HP1", "Author 1", "lorem", "3"),
    Books(5, "HP2", "Author 2", "lorem", "2"),
    Books(6, "HP3", "Author 3", "lorem", "1"),
]


@app.get("/books")
async def read_all_books():
    return BOOKS


@app.post("/create_book")
async def create_book(create_book_request=Body()):
    BOOKS.append(create_book_request)
