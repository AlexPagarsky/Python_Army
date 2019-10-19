from Unit.Unit import Unit
from config.config import *
import Ability.Vampire_ability.Vampire_ability as vamp_ab

class Vampire(Unit):

    def __init__(self, name : str = "Vampire",
                 hp : int = Hp.VAMPIRE_HP.value,
                 dmg : int = Dmg.VAMPIRE_DMG.value):
        Unit.__init__(self, name, hp, dmg)
        self.ability = vamp_ab.Vampire_ability(self)
        self.state.type = "undead"


if __name__ == "__main__":
    tes = Vampire()
    print(tes)