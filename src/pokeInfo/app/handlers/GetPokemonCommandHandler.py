from ..commands.GetPokemonCommand import GetPokemonCommand
from ..repositories.GetPokemonUrlRepository import GetPokemonUrlRepository
from ..repositories.GetPokemonFromApiRepository import GetPokemonFromApiRepository

class GetPokemonCommandHandler:
    def __init__(self, get_pokemon_url_repo: GetPokemonUrlRepository, get_pokemon_from_api_repo: GetPokemonFromApiRepository):
        self.get_pokemon_url_repo = get_pokemon_url_repo
        self.get_pokemon_from_api_repo = get_pokemon_from_api_repo
    
    def handle(self, get_pokemon_command: GetPokemonCommand):
        url = self.get_pokemon_url_repo.get_url_by_name(get_pokemon_command.name)
        return self.get_pokemon_from_api_repo.fetch_pokeapi(url)