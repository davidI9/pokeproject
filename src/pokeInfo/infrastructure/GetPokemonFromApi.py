from ..app.repositories.GetPokemonFromApiRepository import GetPokemonFromApiRepository
from .GetPokemonUrl import GetPokemonUrl

class GetPokemonFromApi(GetPokemonFromApiRepository):
    def __init__(self, url):
        self.url = url
    
    def fetch_pokeapi(url):
        #fetch
        return #my fakin json