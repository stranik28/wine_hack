from pydantic import BaseModel
import uuid

class User_filter(BaseModel):
    name: str = None
    surname: str = None
    role: int = None

class UserCreate(BaseModel):
    name: str
    surname: str
    role: int

class User(UserCreate):
    id: uuid.UUID

class RoleCreate(BaseModel):
    name: str
    description: str

class Role(RoleCreate):
    id: int

class ResponseUser(BaseModel):
    id: uuid.UUID
    name: str
    surname: str

class ResponseUserDev(ResponseUser):
    id: uuid.UUID
    name: str
    surname: str
    role: str

