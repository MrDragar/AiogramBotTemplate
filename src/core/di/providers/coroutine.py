from typing import Callable, Coroutine as _Coroutine, Any, Awaitable
import asyncio

from .provider import Provider, T


class Coroutine(Provider[Callable[..., Awaitable[T]]]):
    __kwargs: dict[str, Any]

    def __init__(self, provides: Callable[..., Awaitable[T]], **kwargs):
        super().__init__(provides)
        self.__kwargs = kwargs

    def __call__(self, *args, **kwargs) -> Awaitable[T]:
        return self._provides(*args, **kwargs, **self._provide_kwargs(**self.__kwargs))