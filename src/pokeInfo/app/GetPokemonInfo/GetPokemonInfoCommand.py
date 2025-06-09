from ...domain.entities.pokemon import Pokemon

class GetPokemonInfoCommand:
    def __init__(self, raw_pokemon: dict):
        self.raw_pokemon= raw_pokemon