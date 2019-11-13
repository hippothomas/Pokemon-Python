import sys
import time

from bo.Zone import ZonePokemon
from menu import MenuInventaire
from menu import MenuEquipe
from menu import MenuPokedex
from menu import MenuExplorer
from services import playerJson

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
    print("\nTu as choisi l'option : " + str(getChoice[menuChoice - 1]) + "\n")

    if (menuChoice == 1):
        MenuInventaire.menuInventaire(player)

    elif (menuChoice == 2):
        MenuEquipe.getEquipe(player)
        menuMain(player)

    elif (menuChoice == 3):
        MenuPokedex.getPokedex(player)

    elif (menuChoice == 4):
        zone = ZonePokemon()
        print("Vous arrivez dans une zone ", zone.name)
        MenuExplorer.menuExplorer(player, zone)

    elif (menuChoice == 5):
        print("\nSauvegarde de la partie ...")
        time.sleep(3)
        playerJson.savePlayer(player)
        print("\nPartie sauvegardée !\n")
        menuMain(player)

    elif (menuChoice == 6):
        exitChoice = input('\033[93m' + "Voulez-vous vraiment quitter le jeu ? [y/n]")

        if (exitChoice == "y"):
            sys.exit(0)

        elif (exitChoice =="n"):
            menuMain(player)
