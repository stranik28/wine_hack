from pydantic import BaseModel
import uuid
from typing import List

class Grape(BaseModel):
    name: str
    description: str

class GrapeInDB(Grape):
    id: uuid.UUID

class Sector(BaseModel):
    coordinates: str
    name: str
    weight: int
    year: int
    grape: uuid.UUID

class SectorInDB(Sector):
    id: uuid.UUID
    color: int

class Field(BaseModel):
    name: str
    year: int
    sectors: List[uuid.UUID]

class FieldInDB(Field):
    id: uuid.UUID
