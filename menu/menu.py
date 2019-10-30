import time
import random
from bo.Zone import *

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
    print("Bien le bonjour! Bienvenue dans le monde magique des Pokémon! Mon nom est Chen! \n"
          "Les gens souvent m'appellent le Prof Pokémon! Ce monde est peuplé de créatures du nom de Pokémon! \n"
          "Pour certains, les Pokémon sont des animaux domestiques, pour d'autres, \n"
          "ils sont un moyen de combattre. Pour ma part... L'étude des Pokémon est ma profession. \n")
    username = str(input("Tout d'abord, quel est ton nom ? "))

    print("OK! Ton nom est donc " + username + " ! \n"
                                               "Un tout nouveau monde de rêves, d'aventures et de Pokémon t'attend! \n\n")

    time.sleep(3)
    print("Des Pokémon sauvages infestent les hautes herbes! \n"
          "Il te faut un Pokémon pour te protéger... Choisis en un ! \n")
    time.sleep(3)


def menuStarter(starter):
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
    print("Super ! tu as choisis " + starter[starterChoice - 1].nom + " prend en soin !\n")
    return starter[starterChoice - 1]

def menuMain():

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
    print("Tu as choisi l'option : " + str(getChoice[menuChoice]))

    if (menuChoice == 4):

        subChoice1 = "Commencer a explorer"
        subChoice2 = "Retour au menu"

        getSubChoice = [subChoice1,
                     subChoice2]

        print("╔══════════════════════════════╗")
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
        print("Tu as choisi l'option : " + str(getSubChoice[subChoice]))

        if (subChoice == 1):
            menuExplorer()

        if (subChoice == 2):
            menuMain()

def menuExplorer():

    choice1 = "Changer de zone"
    choice2 = "Aller en ville"
    choice3 = "Chasser des pokémons"
    choice4 = "Combattre un dresseur"
    choice5 = "Menu principal"

    getChoice = [choice1,
                 choice2,
                 choice3,
                 choice4]

    print("╔══════════════════════════════╗")
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
    print("Tu as choisi l'option : " + str(getChoice[menuChoice]))

    if (menuChoice == 1):
        zone = ZonePokemon()
        print("TTTTTTTTTTTTTTTESSSSSSSSSSSST")
        print(zone.name)

    if (menuChoice == 5):
        menuMain()