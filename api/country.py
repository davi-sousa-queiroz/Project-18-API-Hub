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
            languages = country_data["languages"]

            return [

                f"Capital: {country_data["capital"][0]}",
                f"Population: {country_data["population"]}",
                f"Currency: {currency_name} ({currency_symbol})",
                f"LANGUAGES:"

            ]