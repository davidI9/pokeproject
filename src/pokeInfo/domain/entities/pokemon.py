from ..value_objects.moves_list import MoveList
from ..value_objects.abilities_list import AbilitiesList
from ..value_objects.types_list import TypesList
from ..value_objects.stats_list import StatsList
from ..value_objects.sprite import Sprite


class Pokemon:
    
    def __init__(self,  moves_list: MoveList, abillities_list: AbilitiesList, types_list: TypesList, stats_list: StatsList, name: str, sprite: Sprite):
        self.moves_list = moves_list
        self.abilities_list = abillities_list
        self.types_ist = types_list
        self.stats_list = stats_list
        self.name = name
        self.sprite = sprite