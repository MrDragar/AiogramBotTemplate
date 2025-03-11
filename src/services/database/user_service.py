from abc import ABC, abstractmethod

from sqlalchemy import select

from .models import User, Language
from .iservice import IService, BaseService


class IUserService(IService, ABC):
    @abstractmethod
    async def create_user(
            self, id: int, username: str | None,
            fullname: str, language: Language
    ) -> User:
        ...

    @abstractmethod
    async def get_user_language(self, id: int) -> Language:
        ...


class UserService(BaseService, IUserService):
    async def create_user(
            self, user_id: int, username: str | None,
            fullname: str, language: Language
    ) -> User:
        user = User(
            id=user_id, username=username, fullname=fullname, language=Language
        )
        self._get_session().add(user)
        await self._get_session().commit()
        return user

    async def get_user_language(self, user_id: int) -> Language:
        stmt = select(User).where(User.id == user_id)
        user = await self._get_session().scalar(stmt)
        if user is None:
            raise ValueError("User not found")
        return user.language
