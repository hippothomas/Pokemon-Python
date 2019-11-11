import menu.MenuStart as MenuStart
import menu.MenuMain as MenuMain

# Dialog Professeur Chen
username = MenuStart.menuDialogueStart()

# Choix du starter
player = MenuStart.menuStarter(username)

# Main menu
# (Inventaire/Equipe/Pokedex/Explorer/Sauvegarder/Quitter)
MenuMain.menuMain(player)