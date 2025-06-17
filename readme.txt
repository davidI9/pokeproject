#PokeApi implementation.

This code setups a server in your local host that makes you able to obtain more simple and interesting data from any pokemon queried by its name.

Coded with hexagonal arquitechture.
Used Python with FastApi and httpx.
Database -> sqlite.

#Setup.
As easy as typing "uvicorn src.pokeInfo.infrastructure.pokeinfoAPI:app --reload" on the root directory of the project.
The only endpoint may be accesed as /pokemon/?name=[name of the pokemon]
It returns a giant json with the main info about the pokemon (types, stats, moves, habilities, etc)

This is cool if you want to implement it with a frontend (im not doing that for now lol).
Love all the feedback!