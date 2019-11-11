import json
import random
from bo.Pokemon import Pokemon
from bo.Dresseur import Dresseur

JSON_ZONE_PATH = "./json/zone.json"
NOMBRE_ZONES_JSON = 5
ID_VILLE = NOMBRE_ZONES_JSON - 1


class Zone:
    id = ""
    type = ""
    name = ""


class ZoneVille(Zone):
    list_item = []

    def __init__(self):
        self.id = ID_VILLE
        with open(JSON_ZONE_PATH) as jsonFile:
            data = json.load(jsonFile)
            self.type = data["zones"][self.id]["type"]
            self.name = data["zones"][self.id]["name"]
            self.list_item = data["zones"][self.id]["list_item"]


class ZonePokemon(Zone):
    list_pokemon_id = []

    def __init__(self):
        self.id = random.randrange(0, NOMBRE_ZONES_JSON - 1)
        with open(JSON_ZONE_PATH) as jsonFile:
            data = json.load(jsonFile)
            self.type = data["zones"][self.id]["type"]
            self.name = data["zones"][self.id]["name"]
            self.list_item = data["zones"][self.id]["list_pokemon_id"]

    def getRandomPokemonByZone(self):
        with open(JSON_ZONE_PATH) as jsonFile:
            data = json.load(jsonFile)
            nbPokemonZone = len(data["zones"][self.id]["list_pokemon_id"])
            rand = random.randrange(nbPokemonZone)
            randomPoke = data["zones"][self.id]["list_pokemon_id"][rand]
            pokemon = Pokemon(randomPoke)
            print("\nUn pokémon sauvage apparait !\n")
            print("C'est un " + pokemon.nom + " !")
            return pokemon

    def getRandomDresseurByZone(self):
        with open(JSON_ZONE_PATH) as jsonFile:
            data = json.load(jsonFile)
            nbDresseurZone = len(data["zones"][self.id]["dresseurs"])
            rand = random.randrange(nbDresseurZone)
            randomDresseur = data["zones"][self.id]["dresseurs"][rand]
            dresseur = Dresseur(randomDresseur["name"])
            for poke in randomDresseur["list_pokemon_dresseur"]:
                dresseur.addPokeList(poke)
            print("\n Vous entrez en combat contre le dresseur " + dresseur.name + " !")
            return dresseur
