# ------------ UTILITY FILES -------------
from utils.file_handler import FileHandler
from utils.menu import menu
# ---------- API PYTHON FILES ------------
from api.country import CountryAPI
from api.joke import JokeAPI
from api.pokemon import PokemonAPI
# ----------------------------------------

# -------------- MODULES -----------------
import time
#-----------------------------------------

# --------------- WELCOME ----------------
print("======== WELCOME TO THE API HUB ===========")
# ----------------------------------------

# ------------ MAIN GAME LOOP ------------
def main():

    while True:

        menu()

        selection = input("\n>> ")

        if selection == "1":

            print("\nEnter a pokemon name to view stats and information!")

            try:

                name = input("\n>> ").lower()

                pokemon_search = PokemonAPI(name)

                show_pokemon_info = pokemon_search.show_pokemon_info()

                print(show_pokemon_info)

                time.sleep(1.5)

            except:

                print("\nSomething went wrong... is the pokemon name valid? Try again!")

                time.sleep(1.5)