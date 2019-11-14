def menuInventaire(player):
    print("\n╔══════════════════════════════╗")
    print("╠═════════ INVENTAIRE ═════════╣")
    print("╠══════════════════════════════╣")
    print("║                              ║")
    i = 1
    for item in player.getInventaire():
        print("   - " + str(item.name) + " X1       ")
        i += 1
    print("║                              ║")
    print("╚══════════════════════════════╝\n")
    input("Appuyez sur une touche...")
