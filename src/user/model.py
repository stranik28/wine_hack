from sqlalchemy import Column, ForeignKey, String, Integer
from database import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid

class User(Base):
    __tablename__ = "User"
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    name = Column(String)
    surname = Column(String)
    age = Column(Integer)
    role = Column(Integer, ForeignKey('Role.id'))

class Role(Base):
    __tablename__ = "Role"
    id = Column(Integer, autoincrement=True, primary_key=True, index=True )
    name = Column(String)
    description = Column(String)