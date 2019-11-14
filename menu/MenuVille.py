import menu.MenuAchat as MenuAchat

def menuVille(player, ville):
    choice1 = "Soigner ses pokémons"
    choice2 = "Aller à la boutique"
    choice3 = "Menu explorer"

    getChoice = [choice1,
                 choice2,
                 choice3]

    print("\nVous arrivez dans la zone : " + str(ville.name) + "\n")

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
            if menuChoice > 3 or menuChoice < 1:
                raise Exception()
            else:
                menuChoose = True
        except:
            print("\nVeuillez choisir une action valide")
    print("\nTu as choisi l'option : " + str(getChoice[menuChoice-1]))

    if (menuChoice == 1):
        for pokemon in player.poke_list:
            pokemon.heal()
        print("\nVos pokémons ont été soignés.\n")

    elif (menuChoice == 2):
        print("\nBienvenue dans la boutique !\n")
        MenuAchat.menuAchat(player)

    elif (menuChoice == 3):
        print("\nVous sortez de la ville.")