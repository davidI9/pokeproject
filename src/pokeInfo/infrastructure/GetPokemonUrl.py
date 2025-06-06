from ..app.repositories.GetPokemonUrlRepository import GetPokemonUrlRepository
import sqlite3

class GetPokemonUrl(GetPokemonUrlRepository):
    def get_url_by_name(self, name: str) -> str:
        connect = sqlite3.connect("src/pokeInfo/infrastructure/database.sqlite")
        cursor = connect.cursor()
        cursor.execute("SELECT url FROM pokes WHERE name = ?", (name,))
        
        response = cursor.fetchone()
        if(response):
            url = response[0]
            connect.close()
            return url
        else:
            raise RuntimeError("Pokemon query could not be resolved, please ensure you are providing a real pokemon name.")