from .GetRawPokemonFromApi import GetRawPokemonFromApi
from .GetRawPokemonUrl import GetRawPokemonUrl
from ...app.GetRawPokemon.GetRawPokemonCommand import GetRawPokemonCommand
from ...app.GetRawPokemon.GetRawPokemonCommandHandler import GetRawPokemonCommandHandler

def get_raw_pokemon_info(name: str) -> dict:
    url_repo = GetRawPokemonUrl()
    api_repo = GetRawPokemonFromApi()
    
    command = GetRawPokemonCommand(name)
    handler = GetRawPokemonCommandHandler(url_repo, api_repo)
    
    queried_pokemon = handler.handle(command)
    return queried_pokemon
