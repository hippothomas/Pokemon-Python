from bo.Pokemon import Pokemon
from bo.Competence import Competence


def attack(poke_atk: Pokemon, poke_def: Pokemon, comp: Competence):
    print(poke_atk.nom + " utilise " + comp.name + " sur " + poke_def.nom + "(hp:" + str(poke_def.hp) + ")")
    degats = round((poke_atk.level / 100) * comp.power)
    print("il inflige " + str(degats) + " de dégats à oddish (hp:" + str(poke_def.hp) + ")")
    if degats >= poke_def.hp:
        poke_def.hp = 0
        return True
    else:
        poke_def.hp -= degats
        return False