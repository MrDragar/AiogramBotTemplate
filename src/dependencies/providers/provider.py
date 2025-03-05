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

    @staticmethod
    def _provide_args(*args):
        return [arg() if isinstance(arg, Provider) else arg for arg in args]

    @staticmethod
    def _provide_kwargs(**kwargs):
        return {
            key: value() if isinstance(value, Provider) else value
            for key, value in kwargs.items()
        }
