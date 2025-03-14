from src.domain.entities.user import Language, User
from src.domain.interfaces import IUnitOfWork, IUserRepository
from src.services.interfaces import IUserService


class UserService(IUserService):
    __user_repo: IUserRepository
    __uow: IUnitOfWork

    def __init__(self, user_repo: IUserRepository, uow: IUnitOfWork):
        self.__user_repo = user_repo
        self.__uow = uow

    async def create_user(
            self, user_id: int, username: str | None,
            fullname: str, language: Language
    ) -> User:
        user = User(
            id=user_id, username=username, fullname=fullname, language=language
        )
        async with self.__uow.atomic():
            await self.__user_repo.create_user(user)
        return user

    async def get_user_language(self, user_id: int) -> Language:
        async with self.__uow.atomic():
            user = await self.__user_repo.get_user(user_id=user_id)
        return user.language
