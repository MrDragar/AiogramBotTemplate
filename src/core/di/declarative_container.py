from abc import ABC
from . import providers


class DeclarativeContainer(ABC):
    providers: dict[str, providers.Provider]

    def __init__(self):
        providers_dict = {}
        for name, provider in self.__dict__.items():
            if not isinstance(provider, providers.Provider):
                raise TypeError(f"Container contains fields which are not a Provider {provider} {name}")
            providers_dict[name] = provider
        self.providers = providers_dict
