import requests

class PokemonAPI:

    def __innit__(self, name):

        self.name = name
        self.base_url = "https://pokeapi.co/api/v2/"