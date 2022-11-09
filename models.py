from typing import Optional, List
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum


class Gender(str, Enum):
    MALE = "male"
    FEMALE = "female"


class Role(str, Enum):
    ADMIN = "admin"
    USER = "user"
    STUDENT = "student"


class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name:  str
    middle_name: str
    gender: Gender
    roles: List[Role]
