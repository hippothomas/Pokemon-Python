import random
import time
import random
from bo.Zone import *

from bo.Player import Player

from bo.Item import Item


def menuDialogueStart():

    print("                                  ,'\\\n"
          "    _.----.        ____         ,'  _\   ___    ___     ____\n"
          "_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.\n"
          "\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |\n"
          " \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |\n"
          "   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |\n"
          "    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |\n"
          "     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |\n"
          "      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |\n"
          "       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |\n"
          "        \_.-'       |__|    `-._ |              '-.|     '-.| |   |\n"
          "                                `'                            '-._|\n")

    print("Bien le bonjour ! Bienvenue dans le monde magique des Pokémon! Mon nom est Chen !\n"
          "Les gens souvent m'appellent le Prof Pokémon ! Ce monde est peuplé de créatures du nom de Pokémon !\n"
          "Pour certains, les Pokémon sont des animaux domestiques, pour d'autres,\n"
          "ils sont un moyen de combattre. Pour ma part... L'étude des Pokémon est ma profession.\n")

    username = str(input("Tout d'abord, quel est ton nom ? "))

    print("OK! Ton nom est donc " + username + " ! \n"
          "Un tout nouveau monde de rêves, d'aventures et de Pokémon t'attend !\n")

    time.sleep(3)
    print("Des Pokémon sauvages infestent les hautes herbes !\n"
          "Il te faut un Pokémon pour te protéger... Choisis en un !\n")
    return username


def menuStarter(starter, player):

    print("╔══════════════════════════════╗")
    print("╠═══════ CHOIX STARTER ════════╣")
    print("╠══════════════════════════════╣")
    print("║                              ║")
    for i in range(len(starter)):
        print("║" + " " * 4 + str(i + 1) + " - " + starter[i].nom + " " * (22 - len(str(starter[i].nom))) + "║")
    print("║                              ║")
    print("╚══════════════════════════════╝\n")

    pokeChoose = False
    while not pokeChoose:
        try:
            starterChoice = int(input("Quel pokémon voulez vous choisir : "))
            if starterChoice > 3 or starterChoice <= 0:
                raise Exception()
            else:
                pokeChoose = True
        except:
            print("\nVeuillez choisir un pokémon valide")
    print("\nSuper ! tu as choisis " + starter[starterChoice - 1].nom + " prend en soin !\n")
    player.addPokeList(starter[starterChoice - 1])
    player.addPokedex(starter[starterChoice - 1])
    return starter[starterChoice - 1]

def menuInventaire(player):
    print("╔==============================╗")
    print("║========= INVENTAIRE =========║")
    print("║==============================║")
    print("║                              ║")
    i = 0
    for item in player.getInventaire():
        item_name = Item(item[1]).name
        print("║   " + str(i + 1) + " - " + str(item[0]) + "x" + item_name + "           ")
        i += 1
    print("║                              ║")
    print("╚==============================╝\n")


def menuInventaireCombat(player):
    print("╔==============================╗")
    print("║========= INVENTAIRE =========║")
    print("║==============================║")
    print("║                              ║")
    i = 0
    for item in player.getInventaire():
        item_name = Item(item[1]).name
        print("║   " + str(i + 1) + " - " + str(item[0]) + "x" + item_name + "           ")
        i += 1
    print("║                              ║")
    print("║   1 - Utiliser un item       ║")
    print("║   2 - Quitter                ║")
    print("║                              ║")
    print("╚==============================╝\n")

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
                item = Item(inventaire[chooseItemId - 1][1])
                # Si l'item est de type pokeball
                if item.type == 1:
                    rnd = random.randint(0, 100);
                    # Test si la capture du pokémon est efficace
                    if rnd <= item.effect:
                        # Réussite
                        print("Votre " + item.name + " est très éfficace !")
                        print("Vous venez de capturer ...")
                        # player.addPokeList(enemy)
                    else:
                        # Echec
                        print("Votre " + item.name + " n'est très pas éfficace...")
                    # Passe le tour du joueur en cours
                # Si l'item est de type potion
                elif item.type == 2:
                    print("Vous utilisez " + item.name + "...")
                    # oldhp = pokemon.hp
                    # if (pokemon.hp + item.effect) >= 100:
                    #    pokemon.hp = 100
                    # else:
                    #    pokemon.hp += item.effect
                    # print("Votre pokémon vient de gagné " + str(pokemon.hp - oldhp) + "hp grâce à " + item.name)

                # On retire 1 à la quantité de l'item utilisé
                player.useInventaire(chooseItemId - 1)
            else:
                print("Erreur ! L'item demandé n'existe pas !")

def menuMain(player):

    choice1 = "Inventaire"
    choice2 = "Equipe"
    choice3 = "Pokedex"
    choice4 = "Explorer"
    choice5 = "Sauvegarder"
    choice6 = "Quitter le jeu"

    getChoice = [choice1,
                 choice2,
                 choice3,
                 choice4,
                 choice5,
                 choice6]

    print("╔══════════════════════════════╗")
    print("╠═══════ MENU PRINCIPAL ═══════╣")
    print("╠══════════════════════════════╣")
    print("║                              ║")
    print("║   1 - Inventaire             ║")
    print("║   2 - Equipe                 ║")
    print("║   3 - Pokedex                ║")
    print("║   4 - Explorer               ║")
    print("║   5 - Sauvegarder            ║")
    print("║   6 - Quitter le jeu         ║")
    print("║                              ║")
    print("╚══════════════════════════════╝\n")

    menuChoose = False
    while not menuChoose:
        try:
            menuChoice = int(input("Quel action voulez-vous faire : "))
            if menuChoice > 6 or menuChoice <= 0:
                raise Exception()
            else:
                menuChoose = True
        except:
            print("\nVeuillez choisir une action valide")
    print("\nTu as choisi l'option : " + str(getChoice[menuChoice - 1]))

    if (menuChoice == 2):
        getEquipe(player)
        menuMain(player)

    if (menuChoice == 3):
        getPokedex(player)

    if (menuChoice == 4):

        subChoice1 = "Commencer a explorer"
        subChoice2 = "Retour au menu"

        getSubChoice = [subChoice1,
                     subChoice2]

        print("\n╔══════════════════════════════╗")
        print("║                              ║")
        print("║   1 - Commencer a explorer   ║")
        print("║   2 - Retour au menu         ║")
        print("║                              ║")
        print("╚══════════════════════════════╝\n")

        subChoose = False
        while not subChoose:
            try:
                subChoice = int(input("Quel action voulez-vous faire : "))
                if subChoice > 2 or subChoice <= 0:
                    raise Exception()
                else:
                    subChoose = True
            except:
                print("\nVeuillez choisir une action valide")
        print("\nTu as choisi l'option : " + str(getSubChoice[subChoice - 1]) + "\n")

        if (subChoice == 1):
            menuExplorer(player)

        elif (subChoice == 2):
            menuMain(player)

def menuExplorer(player):

    choice1 = "Changer de zone"
    choice2 = "Aller en ville"
    choice3 = "Chasser des pokémons"
    choice4 = "Combattre un dresseur"
    choice5 = "Menu principal"

    getChoice = [choice1,
                 choice2,
                 choice3,
                 choice4,
                 choice5]

    print("\n╔══════════════════════════════╗")
    print("╠══════ MENU EXPLORATION ══════╣")
    print("╠══════════════════════════════╣")
    print("║                              ║")
    print("║   1 - Changer de zone        ║")
    print("║   2 - Aller en Ville         ║")
    print("║   3 - Chasser des pokémons   ║")
    print("║   4 - Combattre un dresseur  ║")
    print("║   5 - Menu principal         ║")
    print("║                              ║")
    print("╚══════════════════════════════╝\n")

    menuChoose = False
    while not menuChoose:
        try:
            menuChoice = int(input("Quel action voulez-vous faire : "))
            if menuChoice > 5 or menuChoice <= 0:
                raise Exception()
            else:
                menuChoose = True
        except:
            print("\nVeuillez choisir une action valide")
    print("\nTu as choisi l'option : " + str(getChoice[menuChoice - 1]))

    if (menuChoice == 1):
        zone = ZonePokemon()
        print("\nVous arrivez dans la zone : " + str(zone.name) + "\n")
        menuExplorer(player)

    elif (menuChoice == 2):
        zone = ZoneVille()
        print("\nVous arrivez dans la zone : " + str(zone.name) + "\n")
        menuMain(player)

    elif (menuChoice == 5):
        menuMain(player)
        
def menuVille(player):

    choice1 = "Soigner ses pokémons"
    choice2 = "Aller à la boutique"
    choice3 = "Menu explorer"

    getChoice = [choice1,
                 choice2,
                 choice3]

    print("\n╔══════════════════════════════╗")
    print("╠═════════ MENU VILLE ═════════╣")
    print("╠══════════════════════════════╣")
    print("║                              ║")
    print("║   1 - Soigner ses pokémons   ║")
    print("║   2 - Aller à la boutique    ║")
    print("║   3 - Menu explorer          ║")
    print("║                              ║")
    print("╚══════════════════════════════╝\n")

    menuChoose = False
    while not menuChoose:
        try:
            menuChoice = int(input("Quel action voulez-vous faire : "))
            if menuChoice > 2 or menuChoice <= 0:
                raise Exception()
            else:
                menuChoose = True
        except:
            print("\nVeuillez choisir une action valide")
    print("\nTu as choisi l'option : " + str(getChoice[menuChoice - 1]))

    if (menuChoice == 1):
        print("\nVos pokémons ont été soignés.\n")
        menuExplorer(player)

    elif (menuChoice == 2):
        print("\nBienvenue dans la boutique !\n")

    elif (menuChoice == 3):
        menuExplorer(player)

def menuCombat(player):

    choice1 = "Combattre"
    choice2 = "Inventaire"
    choice3 = "Changer de pokémon"
    choice4 = "Fuir"

    getChoice = [choice1,
                 choice2,
                 choice3,
                 choice4]

    print("\n╔══════════════════════════════╗")
    print("╠═══════ MENU COMBATTRE ═══════╣")
    print("╠══════════════════════════════╣")
    print("║                              ║")
    print("║   1 - Combattre              ║")
    print("║   2 - Inventaire             ║")
    print("║   3 - Changer de pokémon     ║")
    print("║   4 - Fuir                   ║")
    print("║                              ║")
    print("╚══════════════════════════════╝\n")

    menuChoose = False
    while not menuChoose:
        try:
            menuChoice = int(input("Quel action voulez-vous faire : "))
            if menuChoice > 4 or menuChoice <= 0:
                raise Exception()
            else:
                menuChoose = True
        except:
            print("\nVeuillez choisir une action valide")
    print("\nTu as choisi l'option : " + str(getChoice[menuChoice - 1]))

    if (menuChoice == 1):
        print("lul")

    elif (menuChoice == 2):
        print("lul")

    elif (menuChoice == 3):
        print("lul")

    elif (menuChoice == 4):
        print("lul")

def getEquipe(player):

    print("╔═════════════════════════════════════════════════════════╗")
    print("╠═════════════════ Votre equipe de pokemon ═══════════════╣")
    print("╠═════════════════════════════════════════════════════════╣")
    for i in range(len(player.poke_list)):
        print("║ " + str(i+1) + " : {}".format("Nom : " + player.poke_list[i].nom + " | HP : " + str(player.poke_list[i].hp) + " | Niveau : " + str(player.poke_list[i].level)) + " " * (22 - len(player.poke_list[i].nom)) + "║")
    print("╚═════════════════════════════════════════════════════════╝\n")

    try:
        int(input(""))
    except:
        pass

def getPokedex(player):

    displayPokedex(1, 21, player)
    pageChoose = False
    while not pageChoose:
        try:
            print("Page 1|2|3|4|5|6|7|8\nQuitter 0")
            page = int(input("Choisir une option : "))
            if page > 3 or page < 0:
                raise Exception()
        except:
            print("Veuillez choisir une page valide")
        if page == 0:
            menuMain(player)
        elif page == 1:
            displayPokedex(1, 21, player)
        elif page == 2:
            displayPokedex(21, 41, player)
        elif page == 3:
            displayPokedex(41, 61, player)
        elif page == 4:
            displayPokedex(61, 81, player)
        elif page == 5:
            displayPokedex(81, 101, player)
        elif page == 6:
            displayPokedex(101, 121, player)
        elif page == 7:
            displayPokedex(121, 141, player)
        elif page == 8:
            displayPokedex(141, 151, player)


def displayPokedex(firstNum, lastNum, player):

    print("╔══════════════════════════════╗")
    print("╠════════ Votre pokedex ═══════╣")
    print("╠══════════════════════════════╣")
    for i in range(firstNum, lastNum):
        pokemon = pokemonIsFound(player.pokedex, i)
        print("║ " + str(i) + " : {}".format(
            "Nom : " + pokemon + " " * (
                          20 - (len(str(i)) + len(pokemon))) + "║"))
    print("╚══════════════════════════════╝\n")


def pokemonIsFound(pokedex, index):

    for i in range(len(pokedex)):
        if pokedex[i].id == index:
            return str(pokedex[i].nom)
        else:
            return "?"