from typing import List
from uuid import uuid4
from fastapi import FastAPI
from models import User, Gender, Role


app = FastAPI()

db: List[User] = [
    User(
        id=uuid4(),
        first_name="Jamila",
        last_name="Ahmed",
        middle_name="Zanna",
        gender=Gender.FEMALE,
        roles=[Role.STUDENT]
    ),
    User(
        id=uuid4(),
        first_name="Alex",
        last_name="Jones",
        middle_name="Pauli",
        gender=Gender.MALE,
        roles=[Role.ADMIN, Role.USER]
    )
]


@app.get("/")
async def root():
    return {"Hello": "Paul !"}


@app.get("/api/v1/users")
async def fetch_users():
    return db
