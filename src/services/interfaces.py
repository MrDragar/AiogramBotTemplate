from abc import ABC, abstractmethod

from src.domain.entities.user import Language, User


class IUserService(ABC):
    @abstractmethod
    async def create_user(
            self, id: int, username: str | None,
            fullname: str, language: Language
    ) -> User:
        ...

    @abstractmethod
    async def get_user_language(self, id: int) -> Language:
        ...
