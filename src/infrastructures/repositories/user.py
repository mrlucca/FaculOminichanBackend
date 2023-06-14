from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.entities.auth import User


class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, user: User):
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)

    async def exists_from_email(self, email: str) -> bool:
        stmt = select(User).where(User.email == email)
        result = await self.session.execute(stmt)
        return True if result.scalars().one_or_none() else False
