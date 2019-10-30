class Player:
    username = ""
    poke_list = []
    item_list = []
    pokedex = []
    monnaie = 0

    def __init__(self, username):
        self.username = username
        self.monnaie = 500
        self.poke_list = []
        item_list = []
        pokedex = []

    def addPokeList(self, pokemon):
        self.poke_list.append(pokemon)

    def addPokedex(self, pokemon):
        self.pokedex.append(pokemon)

