import json

from bo.Player import Player
from bo.Pokemon import Pokemon


def loadPlayer():
    with open("./json/user.json") as json_file:
        data = json.load(json_file)
        player = Player(data["username"])
        pokelist = data["poke_list"]  # list d'id des pokemons du player
        pokedex = data["pokedex"]  # list d'id du pokedex
        for poke_id in pokelist:
            poke_add = Pokemon(poke_id)
            player.addPokeList(poke_add)
        for poke_id in pokedex:
            poke_add = Pokemon(poke_id)
            player.addPokedex(poke_add)
    return player


def savePlayer(player):
    data_player = {
        "username": player.username,
        "monnaie": 500,
        "item_list": [],
        "poke_list": [],
        "pokedex": []
    }
    for poke_id in player.poke_list:
        data_player["poke_list"].append(poke_id.id)
    for pokedex_id in player.pokedex:
        data_player["pokedex"].append(pokedex_id.id)
    with open("./json/user.json", 'w') as outfile:
        json.dump(data_player, outfile, indent=4)
