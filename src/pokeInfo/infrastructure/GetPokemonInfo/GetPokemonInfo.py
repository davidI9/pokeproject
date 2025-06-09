from ..GetRawPokemon.GetRawPokemonInfo import get_raw_pokemon_info
from ...domain.entities.pokemon import Pokemon
from ...app.GetPokemonInfo.GetPokemonInfoCommand import GetPokemonInfoCommand
from ...app.GetPokemonInfo.GetPokemonInfoCommandHandler import GetPokemonInfoCommandHandler

def get_pokemon_info(name: str) -> Pokemon:
    get_pokemon_info_command = GetPokemonInfoCommand(get_raw_pokemon_info(name))
    get_pokemon_info_command_handler = GetPokemonInfoCommandHandler()
    pokemon_info = get_pokemon_info_command_handler.handle(get_pokemon_info_command)
    return pokemon_info

print(get_pokemon_info("pikachu").name)