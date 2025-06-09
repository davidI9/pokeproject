from ....domain.entities.pokemon import Pokemon
from ....domain.value_objects.moves_list import MoveList
from ....domain.value_objects.abilities_list import AbilitiesList
from ....domain.value_objects.types_list import TypesList
from ....domain.value_objects.stats_list import StatsList
from ....domain.value_objects.sprite import Sprite


def pokemon_mapper(raw_pokemon: dict) -> Pokemon:
    moves_list = MoveList(raw_pokemon['moves'])
    abilities_list = AbilitiesList(raw_pokemon['abilities'])
    types_list = TypesList(raw_pokemon['types'])
    stats_list = StatsList(raw_pokemon['stats'])
    name = raw_pokemon['name']
    sprite = Sprite(raw_pokemon['sprites']['front_default'])
    
    return Pokemon(moves_list, abilities_list, types_list, stats_list, name, sprite)

