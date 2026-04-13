import requests

class CountryAPI:

    def __init__(self, country):

        self.url = f"https://restcountries.com/v3.1/name/{country}"

    def show_country_info(self):

        response = requests.get(self.url)

        if response.status_code == 200:

            data = response.json()

            country_data = data[0]

            currencies = country_data["currencies"]
            currency_code = list(currencies.keys())[0]
            currency_name = currencies[currency_code]["name"]
            currency_symbol = currencies[currency_code]["symbol"]

            print(f"\nCapital: {country_data["capital"][0]}",
                f"\nPopulation: {country_data["population"]}",
                f"\nCurrency: {currency_name} ({currency_symbol})",
                f"\nLANGUAGES:")

    def languages_and_time(self):

        response = requests.get(self.url)

        if response.status_code == 200:

            data = response.json()

            country_data = data[0]

            languages = country_data["languages"]

            for language in languages:
                print(language)

            print("TIME ZONES:")

            time_zones = country_data["timezones"]

            for time_zone in time_zones:
                print(time_zone)