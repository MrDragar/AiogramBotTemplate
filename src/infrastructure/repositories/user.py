from sqlalchemy import select

from src.domain.entities.user import User
from src.domain.interfaces import IUserRepository
from ..interfaces import IDatabaseUnitOfWork
from ..models.user import UserORM


class UserRepository(IUserRepository):
    __uow: IDatabaseUnitOfWork

    def __init__(self, uow: IDatabaseUnitOfWork):
        self.__uow = uow

    async def create_user(self, user: User) -> User:
        session = self.__uow.get_session()
        user_orm = UserORM.from_domain(user)
        session.add(user_orm)
        await session.commit()

    async def get_user(self, user_id: int) -> User:
        session = self.__uow.get_session()
        stmt = select(UserORM).where(UserORM.id == user_id)
        user_orm = await session.scalar(stmt)
        return user_orm.to_domain()
