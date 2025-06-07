from abc import abstractmethod

class GetRawPokemonFromApiRepository:
    @abstractmethod
    def fetch_pokeapi(poke_url: str) -> dict:
        pass