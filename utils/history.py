class History:

    def __init__(self, data):

        self.data = data

    def view(self):

        print("\n========== HISTORY ===========")

        print("\nPokemon Searched: ")
        for pokemon in self.data["pokemon"]:
            print(f"- {pokemon}")

        print("\nCountries Searched: ")
        for c in self.data["countries"]:
            print(f"- {c}")

        print(f"\nJokes used: {self.data["joke_count"]}")