from dataclasses import dataclass
from typing import Self
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String, index=True)
    password = Column(String, index=True)

    @classmethod
    def from_dto(cls, dto: 'CreateUser') -> Self:
        return cls(
            **dto.dict()
        )


class CreateUser(BaseModel):
    email: str
    password: str