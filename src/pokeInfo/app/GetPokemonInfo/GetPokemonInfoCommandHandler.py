from ...domain.entities.pokemon import Pokemon
from .mappers.PokemonMapper import pokemon_mapper
from .GetPokemonInfoCommand import GetPokemonInfoCommand

class GetPokemonInfoCommandHandler:
    def handle(self, get_pokemon_info_command: GetPokemonInfoCommand) -> Pokemon:
        pokemon = pokemon_mapper(get_pokemon_info_command.raw_pokemon)
        return pokemon