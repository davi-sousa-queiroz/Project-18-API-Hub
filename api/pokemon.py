import requests

class PokemonAPI:

    def __init__(self, name):

        self.name = name
        self.base_url = "https://pokeapi.co/api/v2/"

    def get_pokemon_info(self):

        url = f"{self.base_url}/pokemon/{self.name}"
        response = requests.get(url)

        if response.status_code == 200:

            pokemon_data = response.json()
            return pokemon_data

        else:

            print(f"Failed to retrieve data {response.status_code}")