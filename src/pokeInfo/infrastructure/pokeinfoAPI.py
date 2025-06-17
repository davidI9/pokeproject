from fastapi import FastAPI
from .GetPokemonInfo.GetPokemonInfo import get_pokemon_info
from fastapi.responses import FileResponse

path = "src/pokeInfo/infrastructure/index.html"
app = FastAPI()

@app.get("/pokemon")
async def get_pokemon_by_name(name: str):
    return get_pokemon_info(name)

