from abc import ABC, abstractmethod

class GetPokemonUrlRepository(ABC):
    @abstractmethod
    def get_url_by_name(name:str)->str:
        pass