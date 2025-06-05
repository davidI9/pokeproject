from ..commands.GetPokemonCommand import GetPokemonCommand
from ..repositories.GetPokemonUrlRepository import GetPokemonUrlRepository
from ..repositories.GetPokemonFromApiRepository import GetPokemonFromApiRepository

class GetPokemonCommandHandler:
    def __init__(self, get_pokemon_url_repository: GetPokemonUrlRepository, api_request: GetPokemonFromApiRepository):
        self.get_pokemon_url_repository = get_pokemon_url_repository
        self.api_request = api_request
    
    def handle(self, get_pokemon_command: GetPokemonCommand):
        url = self.get_pokemon_url_repository(get_pokemon_command.name)
        return self.api_request.fetch_pokeapi(url)