from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_async_session
from typing import List
import uuid
from .schema import Task, TaskType, TaskStatus
from .repository import TaskRepository

router = APIRouter(prefix="/task", tags=["task"])

@router.post("/")
async def create_task(Task: Task, session: AsyncSession = Depends(get_async_session)):
    try:
        await TaskRepository.create_task(session, Task)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.post("/type")
async def create_task_type(TaskType: TaskType, session: AsyncSession = Depends(get_async_session)):
    try:
        await TaskRepository.create_task_type(session, TaskType)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.post("/status")
async def create_task_status(TaskStatus: TaskStatus, session: AsyncSession = Depends(get_async_session)):
    try:
        await TaskRepository.create_task_status(session, TaskStatus)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/types")
async def get_task_types(session: AsyncSession = Depends(get_async_session)):
    try:
        task_types = await TaskRepository.get_task_types(session)
        return task_types
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/statuses")
async def get_task_statuses(session: AsyncSession = Depends(get_async_session)):
    try:
        task_statuses = await TaskRepository.get_task_statuses(session)
        return task_statuses
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/")
async def get_tasks(session: AsyncSession = Depends(get_async_session)):
    try:
        tasks = await TaskRepository.get_tasks(session)
        return tasks
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/{task_id}")
async def get_task(task_id: uuid.UUID, session: AsyncSession = Depends(get_async_session)):
    try:
        task = await TaskRepository.get_task(session, task_id)
        return task
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))