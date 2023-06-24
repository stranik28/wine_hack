from sqlalchemy.ext.asyncio import AsyncSession
from .schema import Task, TaskType, TaskStatus, TaskInDB, TaskTypeInDB, TaskStatusInDB
from .model import Task as TaskModel
from .model import TaskType as TaskTypeModel
from .model import TaskStatus as TaskStatusModel
from sqlalchemy import select
from typing import List
import uuid

class TaskRepository:

    async def create_task(session: AsyncSession, Task: Task):
        task = TaskModel(**Task.dict())
        session.add(task)
        await session.commit()
        await session.refresh(task)
        return task
    
    async def create_task_type(session: AsyncSession, TaskType: TaskType):
        task_type = TaskTypeModel(**TaskType.dict())
        session.add(task_type)
        await session.commit()
        await session.refresh(task_type)
        return task_type
    
    async def create_task_status(session: AsyncSession, TaskStatus: TaskStatus):
        task_status = TaskStatusModel(**TaskStatus.dict())
        session.add(task_status)
        await session.commit()
        await session.refresh(task_status)
        return task_status
    
    async def get_task(session: AsyncSession, task_id: uuid.UUID) -> TaskInDB:
        task = await session.get(TaskModel, task_id)
        return TaskInDB(**task.dict())
    
    async def get_tasks(session: AsyncSession) -> List[TaskInDB]:
        tasks = await session.execute(select(TaskModel))
        res = tasks.scalars().all()
        res = [TaskInDB(**r.__dict__) for r in res]
        return res
    
    async def get_task_types(session: AsyncSession) -> List[TaskTypeInDB]:
        task_types = await session.execute(select(TaskTypeModel))
        res = task_types.scalars().all()
        res = [TaskTypeInDB(**r.__dict__) for r in res]
        return res
    
    async def get_task_statuses(session: AsyncSession) -> List[TaskStatusInDB]:
        task_statuses = await session.execute(select(TaskStatusModel))
        res = task_statuses.scalars().all()
        res = [TaskStatusInDB(**r.__dict__) for r in res]
        return res