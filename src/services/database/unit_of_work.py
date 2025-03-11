from abc import abstractmethod, ABC
from contextlib import asynccontextmanager
from contextvars import ContextVar
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession

from src.services.database.database import IDatabase


class IUnitOfWork(ABC):
    @abstractmethod
    @asynccontextmanager
    async def atomic(self) -> AsyncGenerator[AsyncSession]:
        ...

    @abstractmethod
    def get_session(self) -> AsyncSession:
        ...


class UnitOfWork(IUnitOfWork):
    current_session: ContextVar[AsyncSession | None] =\
        ContextVar('current_session', default=None)

    def __init__(self, database: IDatabase):
        self.database = database

    @asynccontextmanager
    async def atomic(self) -> AsyncGenerator[None, None]:
        async with self.database.create_session() as session:
            token = self.current_session.set(session)
            try:
                yield
                await session.commit()
            except Exception:
                await session.rollback()
                raise
            finally:
                self.current_session.reset(token)

    def get_session(self) -> AsyncSession:
        session = self.current_session.get()
        if session is None:
            raise RuntimeError("Use 'async with uow.atomic()' to create session")
        return session
