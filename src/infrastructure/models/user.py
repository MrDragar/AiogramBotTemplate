from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import Mapped

from src.infrastructure.database import Base
from src.domain.entities.user import Language, User


class UserORM(Base):
    __tablename__ = "users"

    id: Mapped[int] = Column("id", Integer, primary_key=True)
    username: Mapped[str] = Column("username", String, nullable=True)
    fullname: Mapped[str] = Column("fullname", String)
    language: Mapped[Language] = Column("language", Enum(Language), default=Language.ENGLISH)

    def to_domain(self) -> User:
        return User(
            id=self.id,
            username=self.username,
            fullname=self.fullname,
            language=self.language
        )

    @classmethod
    def from_domain(cls, user: User) -> 'UserORM':
        return cls(
            id=user.id,
            username=user.username,
            fullname=user.fullname,
            language=user.language
        )
