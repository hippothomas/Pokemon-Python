import requests

from bo.Competence import Competence


class Pokemon:
    id = ""
    nom = ""
    hp = 0
    hp_max = 0
    level = 0
    xp = 0
    evolution = 0
    evolves_to = 0
    evolve_lvl = 0
    base_xp = 0
    competence = []

    apiUrl = "https://pokeapi.co/api/v2/"
    getPokemon = str(apiUrl) + "pokemon/"

    # si load_comp = false on ne charge pas les compétences (pour limiter les appels API)
    def __init__(self, id_poke, load_comp=True):
        self.id = id_poke
        pokemon_json = requests.get(self.getPokemon + str(self.id)).json()
        # self.getEvolution()
        self.nom = str(pokemon_json['name']).capitalize()
        self.evolution = 1
        self.level = 5
        self.xp = 135
        self.base_xp = pokemon_json['base_experience']
        self.hp_max = self.getHpByLvl()
        self.hp = self.hp_max
        self.competence = []
        if load_comp:
            self.loadComp(pokemon_json)

    def __str__(self):
        comp_str = ""
        for i in range(0, len(self.competence)):
            comp_str += str(self.competence[i])
            if i != len(self.competence):
                comp_str += ", "
        comp_str = comp_str[:-2]
        return "Pokemon { 'id': " + str(self.id) + ", 'nom': " + self.nom + ", 'level': " + str(self.level) +\
               ", 'evolution': " + str(self.evolution) + ", 'hp' : " + str(self.hp) + "/" + str(self.hp_max) +\
               ", 'Competences': [" + comp_str + "]}"

    # Retourne le nombre d'hp d'un pokemon en fonction de son lvl et de son evolution
    def getHpByLvl(self):
        hp = (self.level * 1.5) + (self.evolution * 0.1)
        return round(hp)

    # Ajoute un level à un pokemon et change son max hp
    # Si un level est spécifié change le lvl du pokemon par celui donné
    # TODO faire évoluer si besoin
    def addLevel(self, level=None, evolve=True):
        if self.level == 100:
            return False
        self.level += 1
        if level is not None:
            self.level = level
        self.hp_max = self.getHpByLvl()
        # if level >= self.evolve_lvl and evolve and self.evolution == 1:
        #     self.evolveTo()

    # def evolveTo(self):
    #     poke_evolution = Pokemon(self.evolves_to)
    #     poke_evolution.getEvolution()
    #     self.id = poke_evolution.id
    #     self.nom = poke_evolution.nom
    #     self.base_xp = poke_evolution.base_xp
    #     self.competence = poke_evolution.competence
    #     self.evolve_lvl = poke_evolution.evolve_lvl
    #     self.evolves_to = poke_evolution.evolves_to
    #     self.evolution += 1
    #     self.heal()
    #
    # def getEvolution(self):
    #     poke_species = requests.get("https://pokeapi.co/api/v2/pokemon-species/" + str(self.id)).json()
    #     poke_chain = requests.get(poke_species['evolution_chain']['url']).json()
    #     evolve_species = requests.get(poke_chain['chain']['evolves_to'][0]['species']['url']).json()
    #     self.evolve_lvl = poke_chain['chain']['evolves_to'][0]['evolution_details'][0]['min_level']
    #     if self.evolve_lvl is None:
    #         if self.evolution == 1:
    #             self.evolve_lvl = 20
    #         if self.evolution == 2:
    #             self.evolve_lvl = 35
    #     self.evolves_to = evolve_species['id']

    # ajoute de l'xp au pokemon si le montant d'xp est supérieur à celui nécessaire lvl up
    def addXp(self, amount):
        if self.xp == 0:
            self.xp = self.getXpByLvl(False)
        self.xp += amount
        if self.xp >= self.getXpByLvl():
            self.addLevel()
            print("Vous passez niveau " + str(self.level))

    # Retourne l'xp nécessaire pour le prochain niveau
    def getXpByLvl(self, next_lvl=True):
        if next_lvl:
            lvl = self.level+1
        else:
            lvl = self.level
        return round((6 / 5 * (lvl ** 3)) - 15 * (lvl ** 2) + 100 * lvl - 140)

    # Retourne l'xp gagné en tuant le pokemon
    def getXpWin(self):
        return round((self.base_xp * self.level * 1.2) / 7)

    # Charge les compétences d'un pokémon
    def loadComp(self, poke_json):
        moves = poke_json['moves']
        for comp in moves:
            if len(self.competence) == 4:
                break
            else:
                url = comp['move']['url']
                competence = Competence(url)
                if competence.power > 0 and len(self.competence) < 4:
                    self.competence.append(competence)
        if len(self.competence) <= 1:
            url = "https://pokeapi.co/api/v2/move/33/"
            self.competence.append(Competence(url))

    # Retourne le nombre de dégâts que fait la compétence
    def getDmg(self, comp_atk: Competence):
        return round(comp_atk.power/100 * self.level)

    def heal(self):
        self.hp = self.hp_max
