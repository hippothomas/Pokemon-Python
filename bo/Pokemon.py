import requests


class Pokemon:
    id = ""
    nom = ""
    hp = 0
    level = 0
    competence = []

    apiUrl = "https://pokeapi.co/api/v2/"
    getPokemon = str(apiUrl) + "pokemon/"

    def __init__(self, id):
        self.id = id
        pokemon_json = requests.get(self.getPokemon + str(id)).json()
        self.nom = pokemon_json['name']
        self.hp = 100
        self.level = 5

    def __str__(self):
        return self.nom
