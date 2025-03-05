from typing import Any

from provider import Provider


class Dict(Provider[dict]):
    def __init__(self, **provides: dict[str, Any]):
        super().__init__(provides)

    def __call__(self) -> dict[str, Any]:
        return self._provide_kwargs(**self._provides)
