from abc import ABC, abstractmethod
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from .entities import User


class IUnitOfWork(ABC):
    @abstractmethod
    @asynccontextmanager
    async def atomic(self) -> AsyncGenerator[None, None]:
        ...


class IUserRepository(ABC):
    @abstractmethod
    async def create_user(self, user: User) -> User:
        ...

    @abstractmethod
    async def get_user(self, user_id: int) -> User:
        ...

