from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_async_session
from src.user.repository import UserRepository
from typing import List
from src.user.schema import ResponseUserDev, User_filter, UserCreate, RoleCreate, Role
import uuid

router = APIRouter(prefix="/user", tags=["user"])

@router.get("/", response_model=List[ResponseUserDev])
async def get_users(session: AsyncSession = Depends(get_async_session)):
    '''
        Поля фильтрации опциональоные, если не указаны, то фильтрация не производится
    '''
    try:
        users = await UserRepository.get_all(session)
        return users
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.post("/")
async def create_user(User: UserCreate, session: AsyncSession = Depends(get_async_session)):
    try:
        await UserRepository.create(session, User)
        return status.HTTP_201_CREATED
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.post("/role")
async def create_role(role: RoleCreate, session: AsyncSession = Depends(get_async_session)):
    try:
        await UserRepository.create_role(session, role)
        return status.HTTP_201_CREATED
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/role", response_model=List[Role])
async def get_roles(session: AsyncSession = Depends(get_async_session)):
    try:
        roles = await UserRepository.get_roles(session)
        return roles
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/{user_id}")
async def get_user(user_id: uuid.UUID, session: AsyncSession = Depends(get_async_session)) -> ResponseUserDev:
    try:
        user = await UserRepository.get(session, user_id)
        return user
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))