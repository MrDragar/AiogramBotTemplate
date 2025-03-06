from typing import Any

from .provider import Provider


class List(Provider[list[Any]]):
    def __init__(self, *provides: tuple[Any]):
        super().__init__(provides)

    def __call__(self) -> list[Any]:
        return self._provide_args(*self._provides)
