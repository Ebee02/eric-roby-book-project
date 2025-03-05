from fastapi import FastAPI, status
from pydantic import BaseModel
from uuid import UUID, uuid4

app = FastAPI()


class UserCreate(BaseModel):
    email: str
    password: SystemError


class User(UserCreate):
    account_id: int


@app.post("/create_user/", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate):
    created_user = User(
        account_id="sdkjfkldjjfdue847545", email=user.email, password=user.password
    )
    return created_user
