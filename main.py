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

        elif selection == "2":

            print("\nEnter a Country to view stats and information!")

            try:

                country = input("\n>> ").lower()

                country_search = CountryAPI(country)

                country_search.show_country_info()

                time.sleep(1.5)

                country_search.languages_and_time()

                time.sleep(2)

            except:

                print("Something went wrong... Is the country name valid? Try again!")

        elif selection == "3":

            joke_generator = JokeAPI()

            time.sleep(1)

            print("\nNeed some humor huh 😂? How many jokes would you like?")

            quantity = int(input("\n>> "))

            joke_generator.show_jokes(quantity)

            time.sleep(1.8)

if __name__ == "__main__":
    main()