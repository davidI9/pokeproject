from ...app.GetRawPokemon.repositories.GetRawPokemonUrlRepo import GetRawPokemonUrlRepository
import sqlite3

class GetRawPokemonUrl(GetRawPokemonUrlRepository):
    def get_url_by_name(self, name: str) -> str:
        connect = sqlite3.connect("src/pokeInfo/infrastructure/database.sqlite")
        cursor = connect.cursor()
        cursor.execute("SELECT url FROM pokes WHERE name = ?", (name,))
        
        response = cursor.fetchone()
        if(response):
            poke_url = response[0]
            connect.close()
            return poke_url
        else:
            raise RuntimeError("Pokemon query could not be resolved, please ensure you are providing a real pokemon name.")