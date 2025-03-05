from abc import ABC, abstractmethod
from typing import Callable, Generic, TypeVar

T = TypeVar("T")


class Provider(ABC, Generic[T]):
    _provides: Callable | object

    def __init__(self, provides: Callable[..., T] | T):
        self._provides = provides

    @abstractmethod
    def __call__(self) -> Callable[..., T] | T:
        ...
