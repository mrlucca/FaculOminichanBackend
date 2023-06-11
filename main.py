from fastapi import FastAPI
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

from src.controllers.contacts import ContactController

from src.entities.contact import Base, ContactCreate, ContactListCreate
from src.repositories.contacts import ContactRepository


DATABASE_URL = "sqlite+aiosqlite:///./contacts.db"
engine = create_async_engine(DATABASE_URL, future=True)
SessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

app = FastAPI()

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.on_event("shutdown")
async def shutdown():
    await engine.dispose()



@app.post("/contacts/{email}")
async def create_contact(email: str, contact: ContactCreate):
    contact_repository = ContactRepository(SessionLocal())
    controller = ContactController(contact_repository)
    return await controller.create_contact(email, contact)

@app.get("/contacts/{email}")
async def get_contacts(email: str):
    contact_repository = ContactRepository(SessionLocal())
    controller = ContactController(contact_repository)
    return await controller.get_contacts(email)

@app.post("/contact-list")
async def create_contact_list(contact_list: ContactListCreate):
    contact_repository = ContactRepository(SessionLocal())
    controller = ContactController(contact_repository)
    return await controller.create_contact_list(contact_list)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
