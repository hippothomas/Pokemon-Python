import random

from random import randint
from bo.Item import Item
from menu import MenuMain as MenuMain, menu_combat_dresseur
from bo import Player
from bo.Pokemon import Pokemon
from services.combat import attack


# Affiche la l'inventaire et permet d'en utiliser les objets
# @param player joueur
# @param pokemon pokemon appartenant au joueur actuellement sur le terrain
# @param adversaire pokemon adverse
# @return int le pokémon choisis par l'utilisateur
def menuInventaireCombat(player: Player, pokemon: Pokemon, adversaire: Pokemon, use_pokeball=True):
    captured = False
    print("\n╔══════════════════════════════╗")
    print("╠═════════ INVENTAIRE ═════════╣")
    print("╠══════════════════════════════╣")
    print("║                              ║")
    i = 0
    for item in player.getInventaire():
        print("║   " + str(i + 1) + " - " + item.name + "           ")
        i += 1
    print("║                              ║")
    print("║   1 - Utiliser un objet      ║")
    print("║   2 - Quitter                ║")
    print("║                              ║")
    print("╚══════════════════════════════╝\n")

    # L'utilisateur fait un choix
    choose = False
    while not choose:
        try:
            inputChoice = int(input("Votre choix: "))
            if inputChoice == 1 or inputChoice == 2:
                choose = True
            else:
                raise Exception()
        except:
            print("Veuillez faire un choix valide")

    if inputChoice == 1:
        # L'utilisateur choisi quel item utiliser
        chooseItem = False
        while not chooseItem:
            try:
                chooseItemId = int(input("Veuillez choisir un item : "))
            except:
                print("La saisie n'est pas valide !")
                chooseItemId = -1

            # Si l'item est bien dans l'inventaire
            if player.existInventaire(chooseItemId):
                chooseItem = True
                inventaire = player.getInventaire()
                item = player.item_list[chooseItemId - 1]
                # Si l'item est de type pokeball
                if item.type == 1 and not use_pokeball:
                    print("Vous ne pouvez pas capturer les pokémons de votre adversaire !")
                    return False
                if item.type == 1:
                    rnd = random.randint(0, 100);
                    # Test si la capture du pokémon est efficace
                    if rnd <= item.effect:
                        # Réussite
                        print("Votre " + item.name + " est très éfficace !")
                        print("Vous venez de capturer " + adversaire.nom)
                        player.addPokeList(adversaire)
                        captured = True
                    else:
                        # Echec
                        print("Votre " + item.name + " n'est très pas éfficace...")
                    # Passe le tour du joueur en cours
                # Si l'item est de type potion
                elif item.type == 2:
                    print("Vous utilisez " + item.name + "...")
                    oldhp = pokemon.hp
                    if (pokemon.hp + item.effect) >= 100:
                        pokemon.hp = 100
                    else:
                        pokemon.heal( item.effect)
                    print("Votre pokémon vient de gagné " + str(pokemon.hp - oldhp) + "hp grâce à " + item.name)

                # On retire 1 à la quantité de l'item utilisé
                player.useInventaire(chooseItemId - 1)
                if captured:
                    return "captured"
            else:
                print("Erreur ! L'item demandé n'existe pas !")


# Menu de combat
def combat(player: Player, adversaire):
    player.getInventaire()
    poke_fight = player.getFirstPokeAvailable()
    if isinstance(adversaire, Pokemon):
        adversaire.addLevel(player.getMoyenneLvlPokeRand())
        adversaire.heal()
        print("Un pokémon sauvage apparait ! C'est un " + adversaire.nom +
              " de niveau " + str(adversaire.level))
        player.addPokedex(adversaire)
        print("En avant " + poke_fight.nom)
        while True:
            error_opt = False
            if not player.hasPokeAvailable():
                print("Vous n'avez plus de pokémon pour vous battre ...")
                break
            else:
                if poke_fight.hp == 0:
                    poke_id = changePoke(player, False)
                    poke_fight = player.poke_list[poke_id]
            dspLifeFight(adversaire, poke_fight)
            opt = getOptionCombat()
            if opt == 1:  # ATTACK
                opt_atk = chooseAtk(poke_fight)
                if opt_atk == 0:
                    error_opt = True
                else:
                    attack(poke_fight, adversaire, poke_fight.competence[opt_atk-1])
                    input("")
            elif opt == 2:  # SAC
                if len(player.item_list) < 1:
                    print("Vous n'avez pas d'items à utiliser")
                    error_opt = True
                else:
                    opt_item = menuInventaireCombat(player, poke_fight, adversaire)
                    if opt_item == "captured":
                        break
                    if not opt_item:
                        error_opt = True
            elif opt == 3:  # CHANGE POKEMON
                if len(player.poke_list) < 2:
                    error_opt = True
                    print("Vous n'avez pas suffisament de pokémon")
                else:
                    # TODO pas choisir le pokémon déjà en combat
                    poke_id = changePoke(player)
                    if not poke_id:
                        error_opt = True
                    else:
                        poke_fight = player.poke_list[poke_id]
                        print("A toi " + poke_fight.nom + " !\n")
            elif opt == 4:  # FUITE
                rnd = randint(0, 100);
                if rnd > 10:
                    break
                else:
                    print("Vous n'avez pas réussi à fuir !")

            if adversaire.hp == 0:
                print("Vous avez battu " + adversaire.nom + " de niveau " + str(adversaire.level))
                earned_xp = adversaire.getXpWin()
                print("Vous avez gagné " + str(earned_xp) + " xp")
                poke_fight.addXp(earned_xp)
                break
            # Si pas d'erreur dans le choix du joueur l'adversaire joue
            if not error_opt:
                actionPoke(adversaire, poke_fight)
    else:
        print("Combat de dresseur ...")
        menu_combat_dresseur.combat(player, adversaire)


def dspLifeFight(adversaire: Pokemon, poke_fight: Pokemon):
    life_adversaire = round((adversaire.hp / adversaire.hp_max) * 10)
    print("\n" + adversaire.nom + " sauvage - " + "◻" * (10 - life_adversaire) + "◼" * life_adversaire)
    life_player = round((poke_fight.hp / poke_fight.hp_max) * 10)
    print(poke_fight.nom + " - " + "◻" * (10 - life_player) + "◼" * life_player)


# Action du pokemon adversaire
def actionPoke(poke_adversaire: Pokemon, poke_fight: Pokemon):
    print("Tour de l'adversaire")
    atk = randint(0, len(poke_adversaire.competence)-1)
    attack(poke_adversaire, poke_fight, poke_adversaire.competence[atk])


# Action du dresseur adversaire
def actionTrainer():
    pass


# Affiche les attaques du pokemon en combat
def chooseAtk(poke_atk: Pokemon):
    comp1 = poke_atk.competence[0]
    comp2 = poke_atk.competence[1]
    comp3 = poke_atk.competence[2]
    comp4 = poke_atk.competence[3]
    comp1_info = "1 - " + comp1.name + " (" + str(poke_atk.getDmg(comp1)) + ") "
    comp2_info = "2 - " + comp2.name + " (" + str(poke_atk.getDmg(comp2)) + ") "
    comp3_info = "3 - " + comp3.name + " (" + str(poke_atk.getDmg(comp3)) + ") "
    comp4_info = "4 - " + comp4.name + " (" + str(poke_atk.getDmg(comp4)) + ") "
    length = 0
    if len(comp1_info + comp2_info) > len(comp3_info + comp4_info):
        length = len(comp1_info + comp2_info)
    else:
        length = len(comp3_info + comp4_info)
    length += 3
    print("╔" + "═" * length + "╗")
    print("║ " + comp1_info +
          "║ " + comp2_info + "║")
    print("╠" + "═" * length + "╣")
    print("║ " + comp3_info +
          "║ " + comp4_info + "║")
    print("╠" + "═" * length + "╣")
    print("║  0- Retour" + " " * (length - 11) + "║")
    print("╚" + "═" * length + "╝\n")
    opt = -1
    opt_correct = False
    while not opt_correct:
        try:
            opt = int(input("Choisir une attaque : "))
            if opt > 4 or opt < 0:
                raise Exception()
            else:
                opt_correct = True
        except:
            print("Veuillez choisir une attaque valide")
    return opt


# Affiche le menu de combat
# @return int l'option choisie par l'utilisateur
def getOptionCombat():
    print("╔═════════════════════════════╗")
    print("╠═           Combat          ═╣")
    print("╠══════════════╦══════════════╣")
    print("║  1- Attaque  ║    2- Sac    ║")
    print("╠══════════════╬══════════════╣")
    print("║  3- Pokemon  ║    4- Fuite  ║")
    print("╚══════════════╩══════════════╝\n")
    opt = -1
    opt_correct = False
    while not opt_correct:
        try:
            opt = int(input("Choisir une option : "))
            if opt > 4 or opt < 1:
                raise Exception()
            else:
                opt_correct = True
        except:
            print("Veuillez choisir une option valide")

    return opt


# Affiche la liste des pokémons et demande à l'utilisateur d'en choisir un
# @param Player utilisateur
# @param boolean autorisé à retourner au menu d'attaque ou non
# @return int le pokémon choisis par l'utilisateur
def changePoke(player: Player, back_allowed=True):
    print("╔═════════════════════════════╗")
    i = 0
    for pokemon in player.poke_list:
        poke_info = str(i + 1) + " - " + pokemon.nom + " (hp:" + str(pokemon.hp) + "/" + str(pokemon.hp_max) + ")"
        print("║ " + poke_info + " " * (28 - len(poke_info)) + "║")
        i += 1
    print("║                             ║")
    if back_allowed:
        print("║ 0 - Retour                  ║")
    print("╚═════════════════════════════╝\n")
    poke_choose = -1
    poke_correct = False
    while not poke_correct:
        try:
            poke_choose = int(input("Choisir un pokemon : "))
            if poke_choose > len(player.poke_list) or poke_choose < 0:
                raise Exception()
            elif player.poke_list[poke_choose-1].hp == 0:
                raise Exception()
            poke_correct = True
        except:
            print("Veuillez choisir un pokemon valide")

    if back_allowed:
        if poke_choose == 0:
            return False
        else:
            return poke_choose - 1
    else:
        return poke_choose-1
