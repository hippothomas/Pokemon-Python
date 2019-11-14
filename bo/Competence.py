import requests


class Competence:
    name = ""
    power = 0

    def __init__(self, data):
        comp_json = requests.get(str(data)).json()
        self.name = comp_json['name']
        self.power = comp_json['power']
        if self.power is None:
            self.power = 0

    def __str__(self):
        return "Competence :{ 'name': " + str(self.name) + "; 'power': " + str(self.power) + "}"
