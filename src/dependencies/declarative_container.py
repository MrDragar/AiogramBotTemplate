from abc import ABC
from . import providers


class DeclarativeContainer(ABC):
    providers: dict[str, providers.Provider]

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(**args, **kwargs)
        obj.providers = {}
        for name, provider in obj.__dict__.items():
            obj.providers[name] = provider
            if not isinstance(obj, providers.Provider):
                raise TypeError("Container contains fields which are not a Provider")
        return obj

