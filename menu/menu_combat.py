from random import randint

from bo import Player
from bo.Pokemon import Pokemon


# Menu de combat
from services.combat import attack


def combat(player: Player, adversaire):
    if isinstance(adversaire, Pokemon):
        poke_fight = player.poke_list[0]
        print("Un pokémon sauvage apparait ! C'est un " + adversaire.nom)
        # TODO Ajouter le pokemon du combat au pokedex
        print("En avant " + poke_fight.nom)
        while True:
            error_opt = False
            # TODO Check adversaire dead / plus de poke dans la team
            # if not player.hasPokeAvailable():
            #     pass
            # elif adversaire.hp == 0:
            #     pass
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
                # TODO Ajouter le menu d'hippo
                print("Sac")
            elif opt == 3:  # CHANGE POKEMON
                if len(player.poke_list) < 2:
                    error_opt = True
                    print("Vous n'avez pas suffisament de pokémon")
                else:
                    # TODO Gérer les pokémons KO (💀) / le pokémon déjà en combat
                    poke_id = changePoke(player)
                    if not poke_id:
                        error_opt = True
                    else:
                        poke_fight = player.poke_list[poke_id]
                        print("A toi " + poke_fight.nom + " !")
            elif opt == 4:  # FUITE
                rnd = randint(0, 100);
                if rnd > 10:
                    break
                else:
                    print("Vous n'avez pas réussi à fuir !")
            # Si pas d'erreur dans le choix du joueur l'adversaire joue
            if not error_opt:
                actionPoke(adversaire, poke_fight)
    else:
        print("other")


def dspLifeFight(adversaire: Pokemon, poke_fight: Pokemon):
    life_adversaire = round((adversaire.hp / adversaire.hp_max) * 10)
    print(adversaire.nom + " sauvage - " + "◻" * (10 - life_adversaire) + "◼" * life_adversaire)
    life_player = round((poke_fight.hp / poke_fight.hp_max) * 10)
    print(poke_fight.nom + " - " + "◻" * (10 - life_player) + "◼" * life_player)
    # print("◻◼")
    # pass


# Action du pokemon adversaire
def actionPoke(poke_adversaire: Pokemon, poke_fight: Pokemon):
    print("Tour de l'adversaire")
    atk = randint(0, 3)
    attack(poke_adversaire, poke_fight, poke_adversaire.competence[atk])


# Action du dresseur adversaire
def actionTrainer():
    pass


def chooseAtk(poke_atk: Pokemon):
    comp1 = poke_atk.competence[0]
    comp2 = poke_atk.competence[1]
    comp3 = poke_atk.competence[2]
    comp4 = poke_atk.competence[3]
    print("╔══════════════╦══════════════════╗")
    print("║ 1 - " + comp1.name + " (" + str(poke_atk.getDmg(comp1)) + ") " +
          "║ 2 - " + comp2.name + " (" + str(poke_atk.getDmg(comp2)) + ")║")
    print("╠══════════════╬══════════════════╣")
    print("║ 3 - " + comp3.name + " (" + str(poke_atk.getDmg(comp3)) + ") " +
          "║ 4 - " + comp4.name + " (" + str(poke_atk.getDmg(comp4)) + ")║")
    print("╠══════════════╩══════════════════╣")
    print("║  0- Retour                      ║")
    print("╚═════════════════════════════════╝\n")
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
    pass


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
# @return int le pokémon choisis par l'utilisateur
def changePoke(player: Player):
    # Affiche la liste des pokémons
    print("╔═════════════════════════════╗")
    i = 0
    for pokemon in player.poke_list:
        # print(pokemon.nom)
        print("║ " + str(i + 1) + " - " + pokemon.nom + " " * (25 - len(str(i + 1) + pokemon.nom)) + "║")
        i += 1
    print("║                             ║")
    print("║ 0 - Retour                  ║")
    print("╚═════════════════════════════╝\n")
    poke_choose = -1
    try:
        poke_choose = int(input("Choisir un pokemon : "))
        if poke_choose > len(player.poke_list) or poke_choose < 0:
            raise Exception()
    except:
        print("Veuillez choisir un pokemon dans la liste")
        input("")

    if poke_choose == 0:
        return False
    else:
        return poke_choose - 1

