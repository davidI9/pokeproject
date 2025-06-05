import httpx

response = httpx.get('https://pokeapi.co/api/v2/pokemon/audino').json()

print(response["name"])