from sqlalchemy.orm import Mapped, mapped_column

from src.domain.entities.user import Language, User
from src.infrastructure.database import Base


class UserORM(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column("id", primary_key=True)
    username: Mapped[str] = mapped_column("username", nullable=True)
    fullname: Mapped[str] = mapped_column("fullname")
    language: Mapped[Language] = mapped_column("language", default=Language.ENGLISH)

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
