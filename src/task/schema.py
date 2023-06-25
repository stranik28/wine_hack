from pydantic import BaseModel
from uuid import UUID

class Task(BaseModel):
    sector: UUID
    user: UUID
    task_type: UUID
    status: UUID
    description: str

class TaskType(BaseModel):
    name: str

class TaskStatus(BaseModel):
    name: str
    description: str

class TaskInDB(Task):
    id: UUID

class TaskTypeInDB(TaskType):
    id: UUID

class TaskStatusInDB(TaskStatus):
    id: UUID

class ResponesTask(BaseModel):
    id: UUID
    sector: UUID
    user: UUID
    task_type: str
    status: UUID
    description: str