class MenuEquipe:

    def __init__(self):
        None

def getEquipe(player):
    print("╔═════════════════════════════════════════════════════════╗")
    print("╠═════════════════ Votre equipe de pokemon ═══════════════╣")
    print("╠═════════════════════════════════════════════════════════╣")
    for i in range(len(player.poke_list)):
        print("║ " + str(i + 1) + " : {}".format(
            "Nom : " + player.poke_list[i].nom + " | HP : " + str(player.poke_list[i].hp) + " | Niveau : " + str(
                player.poke_list[i].level)) + " " * (22 - len(player.poke_list[i].nom)) + "║")
    print("╚═════════════════════════════════════════════════════════╝\n")

    try:
        int(input(""))
    except:
        pass
