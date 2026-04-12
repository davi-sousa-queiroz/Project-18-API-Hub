import requests

class JokeAPI:

    def __init__(self):

        self.url = "https://icanhazdadjoke.com/"
        self.headers = {
            "Accept": "text/plain"
        }

    def get_joke(self):

        response = requests.get(self.url, headers=self.headers)

        if response.status_code == 200:
            joke = response.text
            return joke

        else:
            return f"Error code {response.status_code}"

    def show_jokes(self, quantity):

        jokes = JokeAPI()

        for _ in range(quantity):
            input("Press enter for next joke")
            print(f"\n{jokes.get_joke()}")