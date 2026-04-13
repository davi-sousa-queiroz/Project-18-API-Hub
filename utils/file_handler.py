import json

class FileHandler:

    def __init__(self, file_name="data.json"):

        self.file_name = file_name

    def load(self):

        try:

            with open(self.file_name, "r") as file:
                return json.load(file)

        except FileNotFoundError:

            data = {

                "pokemon": [],
                "countries": [],
                "joke_count": 0

            }

            self.save(data)
            return data

    def save(self, data):

        with open(self.file_name, "w") as file:
            json.dump(data, file, indent=4)