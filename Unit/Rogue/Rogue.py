from Unit.Unit import Unit
from Ability.Rogue_ability.Rogue_ability import *
from config.config import *

class Rogue(Unit):

    def __init__(self, name : str = "Rogue", hp : int = Hp.ROGUE_HP.value, dmg : int = Dmg.ROGUE_DMG.value):
        Unit.__init__(self, name, hp, dmg)
        self.ability = Rogue_ability(self)


if __name__ == "__main__":
    rog = Rogue()
    print(rog)