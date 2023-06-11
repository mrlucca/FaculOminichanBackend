from typing import List
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Contact(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    client = Column(String, index=True)
    name = Column(String)
    photo = Column(String)
    phone = Column(String)


class ContactCreate(BaseModel):
    name: str
    photo: str
    phone: str


class ContactListCreate(BaseModel):
    email: str
    contacts: List[ContactCreate]
