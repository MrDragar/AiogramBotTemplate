from dataclasses import dataclass
from enum import Enum


class Language(str, Enum):
    ENGLISH = 'en'
    RUSSIAN = 'ru'
    UKRAINIAN = 'uk'


@dataclass
class User:
    id: int
    username: str | None
    fullname: str
    language: Language = Language.ENGLISH
