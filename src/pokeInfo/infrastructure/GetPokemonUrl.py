from ..app.repositories.GetPokemonUrlRepository import GetPokemonUrlRepository
import sqlite3

class GetPokemonUrl(GetPokemonUrlRepository):
    def get_url_by_name(name: str) -> str:
        connect = sqlite3.connect("src/pokeInfo/infrastructure/database.sqlite")
        cursor = connect.cursor
        
        path = #database correspondent url