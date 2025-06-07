from abc import ABC, abstractmethod

class GetRawPokemonUrlRepository(ABC):
    @abstractmethod
    def get_url_by_name(name:str)->str:
        pass