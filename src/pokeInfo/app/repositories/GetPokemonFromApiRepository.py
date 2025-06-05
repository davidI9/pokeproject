from abc import abstractmethod
from ...domain.entities.pokemon import Pokemon

class GetPokemonFromApiRepository:
    @abstractmethod
    def fetch_pokeapi(url: str) -> Pokemon:
        pass