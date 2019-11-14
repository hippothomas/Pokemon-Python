from random import randint
from bo.Item import Item


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
        id_search = pokemon.id
        found = False
        for poke in self.pokedex:
            if poke.id == id_search:
                found = True
                break
        if not found:
            self.pokedex.append(pokemon)
            return True
        else:
            return False

    def getInventaire(self):
        return self.item_list

    def setInventaire(self, list):
        self.item_list = list

    def addInventaire(self, item):
        # exist = False
        # i = 0
        # for it in self.item_list:
        #     if Item(it[1]) == item:
        #         exist = True
        #         self.item_list[i][0] = self.item_list[i][0] + 1
        #     i += 1
        #
        # if exist == False :
        #     self.item_list.append(item)
        items = self.getInventaire()
        items.append(item)

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

    def getMoyenneLvlPokeRand(self):
        i = 0
        lvl_total = 0
        for poke in self.poke_list:
            lvl_total = poke.level
            i += 1
        lvl_moyen = round(lvl_total/i)
        rnd_lvl = randint(lvl_moyen-2, lvl_moyen+2)
        if rnd_lvl < 3:
            return 3
        return rnd_lvl
