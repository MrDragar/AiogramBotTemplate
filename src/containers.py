from src.dependencies import DeclarativeContainer, providers
from src.services.database.database import Database, IDatabase


class Container(DeclarativeContainer):
    database: providers.Singleton[IDatabase] = providers.Singleton(
        Database, "db.sqlite3"
    )
