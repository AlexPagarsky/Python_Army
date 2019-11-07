from Unit.Unit import Unit
from config import *
import Ability.VampireAbility.VampireAbility as Vab


class Vampire(Unit):

    def __init__(self, name : str = "Vampire",
                 hp : int = Hp.VAMPIRE_HP.value,
                 dmg : int = Dmg.VAMPIRE_DMG.value):
        Unit.__init__(self, name, hp, dmg)
        self.ability = Vab.VampireAbility(self)
        self.state.type = "undead"
        self.state.turnable = False


if __name__ == "__main__":
    tes = Vampire()
    print(tes)