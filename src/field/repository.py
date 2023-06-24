from sqlalchemy.ext.asyncio import AsyncSession
from .schema import Grape, GrapeInDB, Sector, SectorInDB, Field, FieldInDB
from .model import Grape as GrapeModel
from .model import Sector as SectorModel
from .model import Field as FieldModel
from sqlalchemy import select
import uuid
from typing import List

class GrapeRepository():

    async def create_grape(session: AsyncSession, grape: Grape):
        try:
            grape = GrapeModel(**grape.dict())
            session.add(grape)
            await session.commit()
        except Exception as e:
            raise e
        
    async def get_grape(session: AsyncSession, grape_id: uuid.UUID) -> GrapeInDB:
        try:
            grape = await session.get(GrapeModel, grape_id)
            return GrapeInDB(**grape.dict())
        except Exception as e:
            raise e
        
    async def get_grapes(session: AsyncSession) -> List[GrapeInDB]:
        try:
            grapes = await session.execute(select(GrapeModel))
            res = grapes.scalars().all()
            res = [GrapeInDB(**r.__dict__) for r in res]
            return res
        except Exception as e:
            raise e

    async def create_sector(session: AsyncSession, sector: Sector):
        try:
            sector = SectorModel(**sector.dict())
            session.add(sector)
            await session.commit()
        except Exception as e:
            raise e
        
    async def get_sector(session: AsyncSession, sector_id: uuid.UUID) -> SectorInDB:
        try:
            sector = await session.get(SectorModel, sector_id)
            return SectorInDB(**sector.dict())
        except Exception as e:
            raise e
        
    async def get_sectors(session: AsyncSession) -> List[SectorInDB]:
        try:
            sectors = await session.execute(select(SectorModel))
            res = sectors.scalars().all()
            res = [SectorInDB(**r.__dict__) for r in res]
            return res
        except Exception as e:
            raise e
        
    async def get_fields(session: AsyncSession) -> List[FieldInDB]:
        try:
            fields = await session.execute(select(FieldModel))
            res = fields.scalars().all()
            res = [FieldInDB(**r.__dict__) for r in res]
            return res
        except Exception as e:
            raise e
        
    async def create_field(session: AsyncSession, field: Field):
        field = FieldModel(**field.dict())
        session.add(field)
        await session.commit()