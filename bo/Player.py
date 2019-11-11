class Player:
    username = ""
    poke_list = []
    item_list = []
    pokedex = []
    monnaie = 0
    zone = ""

    def __init__(self, username):
        self.username = username
        self.monnaie = 500
        self.poke_list = []
        item_list = []
        pokedex = []

    def addPokeList(self, pokemon):
        self.poke_list.append(pokemon)

    def addPokedex(self, pokemon):
        # TODO Check que le pokemon est pas déjà dans le pokedex
        self.pokedex.append(pokemon)

    def getInventaire(self):
        return self.item_list

    def setInventaire(self, list):
        self.item_list = list

    def addInventaire(self, item):
        self.item_list.extend(item)

    def existInventaire(self, id):
        if 0 < id <= len(self.item_list):
            return True
        else:
            return False

    # Utilise un des item de l'inventaire
    def useInventaire(self, id):
        self.item_list[id][0] = self.item_list[id][0] - 1
        if self.item_list[id][0] == 0:
            self.removeFromInventaire(id)

    # Permet de supprimer un item de la l'inventaire
    def removeFromInventaire(self, id):
        self.item_list.remove(self.item_list[id])

    def hasPokeAvailable(self):
        poke_available = False
        for pokemon in self.poke_list:
            if pokemon.hp > 0:
                poke_available = True
        return poke_available

    def getFirstPokeAvailable(self):
        poke_return = None
        for pokemon in self.poke_list:
            if pokemon.hp > 0:
                poke_return = pokemon
                break
        return poke_return
