from Unit.Unit import *
from config.config import *
from Ability.Vampire_ability.Vampire_ability import *


class Vampire(Unit):

    def __init__(self, name : str = "Vampire",
                 hp : int = Hp.VAMPIRE_HP,
                 dmg : int = Dmg.VAMPIRE_DMG):
        Unit.__init__(name, hp, dmg)
        self.ability = Vampire_ability(self)
        self.state.type = "undead"





if __name__ == "__main__":
    tes = Vampire()
    print(tes)