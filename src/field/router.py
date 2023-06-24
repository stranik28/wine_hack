from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_async_session
from typing import List
import uuid
from .schema import Grape, Sector, SectorInDB, Field, FieldInDB
from .repository import GrapeRepository


router = APIRouter(prefix="/field", tags=["field"])

@router.post("/grape")
async def create_grape(grape: Grape, session: AsyncSession = Depends(get_async_session)):
    try:
        await GrapeRepository.create_grape(session, grape)
        return status.HTTP_201_CREATED
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    
@router.get("/grape/{grape_id}")
async def get_grape(grape_id: uuid.UUID, session: AsyncSession = Depends(get_async_session)):
    try:
        grape = await GrapeRepository.get_grape(session, grape_id)
        return grape
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    
@router.get("/grapes")
async def get_grapes(session: AsyncSession = Depends(get_async_session)):
    try:
        grapes = await GrapeRepository.get_grapes(session)
        return grapes
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.post("/sector")
async def create_sector(sector: Sector, session: AsyncSession = Depends(get_async_session)):
    try:
        await GrapeRepository.create_sector(session, sector)
        return status.HTTP_201_CREATED
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    
@router.get("/sector/{sector_id}")
async def get_sector(sector_id: uuid.UUID, session: AsyncSession = Depends(get_async_session)):
    try:
        sector = await GrapeRepository.get_sector(session, sector_id)
        return SectorInDB(**sector.dict())
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    
@router.get("/sectors")
async def get_sectors(session: AsyncSession = Depends(get_async_session)):
    try:
        sectors = await GrapeRepository.get_sectors(session)
        return sectors
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    
@router.get("/fields", response_model=List[FieldInDB])
async def get_fields(session: AsyncSession = Depends(get_async_session)):
    try:
        fields = await GrapeRepository.get_fields(session)
        return fields
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    
@router.post("/field")
async def create_field(field: Field, session: AsyncSession = Depends(get_async_session)):
    try:
        await GrapeRepository.create_field(session, field)
        return status.HTTP_201_CREATED
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))