import time

import menu.MenuStart as MenuStart
import menu.MenuMain as MenuMain
import menu.MenuSauvegarde as MenuSauvegarde
from services import playerJson

if MenuSauvegarde.checkSauvegarde():
    print("Une sauvergarde existe déjà")
    try:
        choix = input("Voulez-vous charger la partie existante ? [y/n]")
        if (choix == "y"):
            print("Chargement de la partie ...")
            time.sleep(1)
            player = playerJson.loadPlayer()

        else:
            print("Partie Supprimée, nouvelle partie ...")
            time.sleep(1)
            # Dialog Professeur Chen
            username = MenuStart.menuDialogueStart()
            # Choix du starter
            player = MenuStart.menuStarter(username)
    except:
        print("\nVeuillez choisir une action valide")
else:
    print("Nouvelle partie ...")
    time.sleep(1)
    # Dialog Professeur Chen
    username = MenuStart.menuDialogueStart()
    # Choix du starter
    player = MenuStart.menuStarter(username)

# Main menu
# (Inventaire/Equipe/Pokedex/Explorer/Sauvegarder/Quitter)
MenuMain.menuMain(player)
