import enum

from sqlalchemy import Column, Integer, String, Enum

from .database import Base


class Languages(enum.Enum):
    english = 'en'
    russian = 'ru'
    ukrainian = 'uk'


class User(Base):
    id = Column("id", Integer, primary_key=True)
    username = Column("username", String, nullable=True)
    fullname = Column("fullname", String)
    language = Column("language", Enum(Languages), default=Languages.english)

    __tablename__ = "users"
