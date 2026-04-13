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

            return f"Failed to retrieve data {response.status_code}"

    def show_pokemon_info(self):

        pokemon_API = PokemonAPI(self.name)

        pokemon_info = pokemon_API.get_pokemon_info()

        if pokemon_info:
            return [
                f"Name: {pokemon_info["name"].capitalize()}",
                f"ID: {pokemon_info["id"]}",
                f"Height: {pokemon_info["height"]}",
                f"Weight: {pokemon_info["weight"]}",
                f"Order: {pokemon_info["order"]}"
            ]