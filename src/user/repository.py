from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.user.model import User, Role as RoleDB
from src.user.schema import Role, ResponseUserDev
from typing import List

class UserRepository():

    async def get_all(session: AsyncSession) -> List[ResponseUserDev]:
        async with session.begin():
            stmt = select(User, RoleDB).join(RoleDB)
            result = await session.execute(stmt)
            respones =  result.scalars().all()
            for i in respones:
                print(i.__dict__)
            respones = [ResponseUserDev(**res.__dict__) for res in respones]
            for i in respones:
                stmt = select(RoleDB).where(RoleDB.id == int(i.role))
                result = await session.execute(stmt)
                role = result.scalars().first()
                i.role = None
                i.role = role.name
            return [ResponseUserDev(**res.__dict__) for res in respones]

            

    async def get(session: AsyncSession, user_id) -> ResponseUserDev:
        async with session.begin():
            stmt = select(User).where(User.id == user_id)
            result = await session.execute(stmt)
            respones =  result.scalars().first()
            respones = ResponseUserDev(**respones.__dict__)
            stmt = select(RoleDB).where(RoleDB.id == int(respones.role))
            result = await session.execute(stmt)
            role = result.scalars().first()
            respones.role = None
            respones.role = role.name
            return ResponseUserDev(**respones.__dict__)
        
    async def create(session: AsyncSession, user):
        async with session.begin():
            user_db = User()
            user_db.name = user.name
            user_db.surname = user.surname
            user_db.role = user.role
            user_db.age = user.age
            session.add(user_db)
            await session.commit()

    async def create_role(session: AsyncSession, role):
        async with session.begin():
            role_db = RoleDB()
            role_db.name = role.name
            role_db.description = role.description
            session.add(role_db)
            await session.commit()

    async def get_roles(session: AsyncSession) -> List[Role]:
        async with session.begin():
            stmt = select(RoleDB)
            result = await session.execute(stmt)
            respones =  result.scalars().all()
            return [Role(**res.__dict__) for res in respones]