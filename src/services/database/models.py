import enum

from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import Mapped

from .database import Base


class Language(enum.Enum):
    english = 'en'
    russian = 'ru'
    ukrainian = 'uk'


class User(Base):
    id: Mapped[int] = Column("id", Integer, primary_key=True)
    username: Mapped[str] = Column("username", String, nullable=True)
    fullname: Mapped[str] = Column("fullname", String)
    language: Mapped[Language] = Column("language", Enum(Language), default=Language.english)

    __tablename__ = "users"
