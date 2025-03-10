from asyncio import current_task
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    async_sessionmaker, create_async_engine, AsyncSession,
    async_scoped_session, AsyncEngine
)
from sqlalchemy.orm import declarative_base, DeclarativeBase

Base: DeclarativeBase = declarative_base()


class Database:
    __engine: AsyncEngine
    __session_maker: async_sessionmaker
    __database_session: async_scoped_session

    def __init__(self, db_url: str):
        self.__engine = create_async_engine(
            self.get_sqlite_url(db_url), echo=True
        )
        self.__session_maker = async_sessionmaker(
            bind=self.__engine,
            autoflush=False,
            class_=AsyncSession
        )
        self.__database_session = async_scoped_session(
            self.__session_maker, current_task
        )

    @asynccontextmanager
    async def session(self) -> AsyncGenerator[AsyncSession]:
        session = self.__database_session()
        try:
            yield session
        except Exception as ex:
            await session.rollback()
            raise ex
        finally:
            await session.close()

    async def create_database(self):
        async with self.__engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    @staticmethod
    def get_sqlite_url(db_path) -> str:
        return f"sqlite+aiosqlite:///{db_path}"
