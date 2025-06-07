from ...app.GetRawPokemon.repositories.GetRawPokemonFromApiRepo import GetRawPokemonFromApiRepository
import httpx


class GetRawPokemonFromApi(GetRawPokemonFromApiRepository):
    def fetch_pokeapi(self, poke_url: str):
        queried_pokemon = httpx.get(poke_url).json()
        return queried_pokemon