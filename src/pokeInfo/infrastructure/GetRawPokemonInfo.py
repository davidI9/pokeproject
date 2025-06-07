from .GetPokemonFromApi import GetPokemonFromApi
from .GetPokemonUrl import GetPokemonUrl
from ..app.commands.GetPokemonCommand import GetPokemonCommand
from ..app.handlers.GetPokemonCommandHandler import GetPokemonCommandHandler

def get_raw_pokemon_info(name: str) -> dict:
    url_repo = GetPokemonUrl()
    api_repo = GetPokemonFromApi()
    
    command = GetPokemonCommand(name)
    handler = GetPokemonCommandHandler(url_repo, api_repo)
    
    queried_pokemon = handler.handle(command)
    print(type(queried_pokemon))
