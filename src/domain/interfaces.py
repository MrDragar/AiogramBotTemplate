from abc import ABC, abstractmethod
from contextlib import _AsyncGeneratorContextManager

from .entities import User


class IUnitOfWork(ABC):
    @abstractmethod
    def atomic(self) -> _AsyncGeneratorContextManager[None, None]:
        ...


class IUserRepository(ABC):
    @abstractmethod
    async def create_user(self, user: User) -> User:
        ...

    @abstractmethod
    async def get_user(self, user_id: int) -> User:
        ...

