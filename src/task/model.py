from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Task (Base):
    __tablename__ = "Task"
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    sector = Column(UUID(as_uuid=True))
    user = Column(UUID(as_uuid=True), ForeignKey('User.id'))
    task_type = Column(UUID(as_uuid=True), ForeignKey('TaskType.id'))
    status = Column(UUID(as_uuid=True), ForeignKey('TaskStatus.id'))
    description = Column(String)

class TaskType (Base):
    __tablename__ = "TaskType"
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    name = Column(String)

class TaskStatus (Base):
    __tablename__ = "TaskStatus"
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    name = Column(String)
    description = Column(String)