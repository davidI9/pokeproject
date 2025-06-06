from ..app.repositories.GetPokemonFromApiRepository import GetPokemonFromApiRepository
import httpx


class GetPokemonFromApi(GetPokemonFromApiRepository):
    def __init__(self, url):
        self.url = url
    
    def fetch_pokeapi(self):
        queried_pokemon = httpx.get(self.url)
        return queried_pokemon