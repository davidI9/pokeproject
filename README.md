# PokeApi implementation.

This code setups a server in your local host that makes you able to obtain some simple and interesting data from any pokemon queried by its name.

Coded with hexagonal arquitechture (Truly not my best work but is honest work, if you want to see my real skills with hexagonal, check the rest of my repos).
Used Python with FastApi and httpx.
Database -> sqlite.

# Setup.
As easy as throwing 
``` bash
uv sync # sync dependencies

uvicorn src.pokeInfo.infrastructure.pokeinfoAPI:app --reload # starts the endpoint server
```
on the root directory of the project.
The only endpoint may be accesed as 
``` bash
http://localhost:8000/pokemon/THE-NAME-OF-THE-POKEMON # change this for the name of the pokemon you want
```
It returns a giant json with the main info about the pokemon (types, stats, moves, habilities, etc)

This is cool if you want to implement it with a frontend (im not doing that for now lol).
Love all the feedback!
