from typing import Callable, overload

from provider import Provider, T


class Singleton(Provider[T]):
    def __init__(self, provides: Callable[..., T], *args, **kwargs):
        super().__init__(provides(*args, **kwargs))

    def __call__(self) -> T:
        return self._provides

