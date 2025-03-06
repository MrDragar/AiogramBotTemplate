from provider import Provider, T
from typing import Callable as _Callable, Any


class Callable(Provider[_Callable[..., T]]):
    __kwargs:  dict[Any, ...]

    def __init__(self, provides: _Callable[..., T], **kwargs):
        super().__init__(provides)
        self.__kwargs = kwargs
        
    def __call__(self) -> _Callable[..., T]:
        return lambda *args, **kwargs: (self._provides(
            *args, **kwargs, self._provide_kwargs(**self.__kwargs)
        ))
