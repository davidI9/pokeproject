from ..app.repositories.GetPokemonFromApiRepository import GetPokemonFromApiRepository
import httpx


class GetPokemonFromApi(GetPokemonFromApiRepository):
    def fetch_pokeapi(self, url: str):
        queried_pokemon = httpx.get(url).json()
        return queried_pokemon