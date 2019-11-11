from bo.Pokemon import Pokemon
from bo.Competence import Competence


def attack(poke_atk: Pokemon, poke_def: Pokemon, comp: Competence):
    print(poke_atk.nom + " utilise " + comp.name + " sur " + poke_def.nom)
    degats = poke_atk.getDmg(comp)
    print("il lui inflige " + str(degats) + " de dégat")
    if degats >= poke_def.hp:
        poke_def.hp = 0
    else:
        poke_def.hp -= degats
    return poke_def.hp == 0
