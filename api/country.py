import requests

class CountryAPI:

    def __init__(self, country):

        self.url = f"https://restcountries.com/v3.1/name/{country}"