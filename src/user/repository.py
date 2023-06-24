from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.user.model import User, Role as RoleDB
from src.user.schema import ResponseUser, Role 
from typing import List


class UserRepository():

    async def get_all(session: AsyncSession, body) -> List[ResponseUser]:
        async with session.begin():
            # Make request with filter from body if it is not None
            stmt = select(User)
            if body not in [None, {}]:
                if body.name is not None:
                    stmt = stmt.where(User.name == body.name)
                if body.surname is not None:
                    stmt = stmt.where(User.surname == body.surname)
                if body.role is not None:
                    stmt = stmt.where(User.role == body.role)
            result = await session.execute(stmt)
            respones =  result.scalars().all()
            return [ResponseUser(**res.__dict__) for res in respones]
            

    async def get(session: AsyncSession, user_id: int) -> ResponseUser:
        async with session.begin():
            stmt = select(User).where(User.id == user_id)
            result = await session.execute(stmt)
            respones =  result.scalars().first()
            return ResponseUser(**respones.__dict__)
        
    async def create(session: AsyncSession, user):
        async with session.begin():
            user_db = User()
            user_db.name = user.name
            user_db.surname = user.surname
            user_db.role = user.role
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