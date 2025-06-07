from .GetRawPokemonCommand import GetRawPokemonCommand
from .repositories.GetRawPokemonUrlRepo import GetRawPokemonUrlRepository
from .repositories.GetRawPokemonFromApiRepo import GetRawPokemonFromApiRepository

class GetRawPokemonCommandHandler:
    def __init__(self, get_raw_pokemon_url_repo: GetRawPokemonUrlRepository, get_raw_pokemon_from_api_repo: GetRawPokemonFromApiRepository):
        self.get_raw_pokemon_url_repo = get_raw_pokemon_url_repo
        self.get_raw_pokemon_from_api_repo = get_raw_pokemon_from_api_repo
    
    def handle(self, get_pokemon_command: GetRawPokemonCommand):
        poke_url = self.get_pokemon_url_repo.get_url_by_name(get_pokemon_command.name)
        return self.get_pokemon_from_api_repo.fetch_pokeapi(poke_url)