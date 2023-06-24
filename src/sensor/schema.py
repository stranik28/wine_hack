from pydantic import BaseModel
from datetime import datetime
import uuid

class Sensor(BaseModel):
    value: int
    type: int
    sector: uuid.UUID
    coordination: str


class Sensor_db(Sensor):
    id: uuid.UUID

class Sensor_type(BaseModel):
    name: str

class Sensor_type_db(Sensor_type):
    id: int

class Incident(BaseModel):
    type: int
    body: str  
    title: str
    sector: uuid.UUID

class Incident_db(Incident):
    id: uuid.UUID

class Weather(BaseModel):
    name: str
    type: int
    field: uuid.UUID

class Weather_db(Weather):
    id: uuid.UUID

class Weather_type(BaseModel):
    name: str

class Weather_type_db(Weather_type): 
    id: int

class Role(BaseModel):
    name: str

class Role_db(Role):
    id: int