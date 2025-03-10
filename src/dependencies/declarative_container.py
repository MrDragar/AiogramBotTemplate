from abc import ABC
from . import providers


class DeclarativeContainer(ABC):
    providers: dict[str, providers.Provider]

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls, *args, **kwargs)
        providers_dict = {}
        for name, provider in obj.__dict__.items():
            if not isinstance(provider, providers.Provider):
                raise TypeError(f"Container contains fields which are not a Provider {provider} {name}")
            providers_dict[name] = provider
        obj.providers = providers_dict
        return obj

