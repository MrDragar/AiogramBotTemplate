from src.dependencies import DeclarativeContainer, providers
from src.database import Database


class Container(DeclarativeContainer):
    database = providers.Singleton(Database, "db.sqlite3")
