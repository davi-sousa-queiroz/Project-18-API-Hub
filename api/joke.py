import requests

class JokeAPI:

    def __init__(self):

        self.url = "https://icanhazdadjoke.com/"
        self.headers = {
            "Accept": "text/plain"
        }