from sqlalchemy import Column, Integer, String, ForeignKey, ARRAY
from database import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Sector(Base):
    __tablename__ = "Sector"
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    coordinates = Column(String)
    name = Column(String)
    weight = Column(Integer)
    year = Column(Integer)
    grade = Column(Integer)
    air = Column(Integer)
    ground = Column(Integer)
    water = Column(Integer)
    grape = Column(UUID(as_uuid=True), ForeignKey('Grape.id'))

class Grape(Base):
    __tablename__ = "Grape"
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    name = Column(String)
    description = Column(String, nullable=True)

class Field(Base):
    __tablename__ = "Field"
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    #Array of sectors
    sectors = Column(ARRAY(UUID(as_uuid=True)))
    year = Column(Integer)
    name = Column(String)
    

class Bushe(Base):
    __tablename__ = "Bushe"
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    status = Column(Integer, ForeignKey('BusheStatus.id'))
    year = Column(Integer)
    sector = Column(UUID(as_uuid=True), ForeignKey('Sector.id'))

class BusheStatus(Base):
    __tablename__ = "BusheStatus"
    id = Column(Integer, primary_key=True, index=True, default=uuid.uuid4)
    name = Column(String)
