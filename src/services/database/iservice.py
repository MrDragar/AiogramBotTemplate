from abc import ABC, abstractmethod
from typing import Self

from sqlalchemy.ext.asyncio import AsyncSession


class IService(ABC):
    @abstractmethod
    def register_session(self, session: AsyncSession) -> Self:
        ...


class BaseService(IService, ABC):
    __session: AsyncSession | None

    def register_session(self, session: AsyncSession) -> Self:
        self.__session = session
        return self

    def _get_session(self) -> AsyncSession:
        if self.__session is None:
            raise ValueError(
                "Context not found. "
                "Use Service().register_session() to use context."
            )
        return self.__session
