from fastapi import FastAPI

app = FastAPI()


class Books:
    id: int
    title: str
    author: str
    descrition: str
    rating: str

    def __init__(self, id, title, author, descrition, rating):
        self.id = id
        self.title = title
        self.author = author
        self.descrition = descrition
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
