from src.dependencies import DeclarativeContainer, providers
from src.services.database.database import Database, IDatabase
from src.services.database.unit_of_work import UnitOfWork, IUnitOfWork
from src.services.database.user_service import UserService, IUserService


class Container(DeclarativeContainer):
    database: providers.Singleton[IDatabase] = providers.Singleton(
        Database, "db.sqlite3"
    )
    uow: providers.Singleton[IUnitOfWork] = providers.Singleton(
        UnitOfWork, database=database
    )
    user_service: providers.Factory[IUserService] = providers.Factory(
        UserService, uow=uow
    )
