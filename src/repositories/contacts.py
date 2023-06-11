from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.entities.contact import Contact, ContactCreate


class ContactRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, email: str, contact: ContactCreate):
        contact_db = Contact(client=email, **contact.dict())
        self.session.add(contact_db)
        await self.session.commit()
        await self.session.refresh(contact_db)

    async def get_by_email(self, email: str):
        stmt = select(Contact).where(Contact.client == email)
        result = await self.session.execute(stmt)
        return result.scalars().all()
