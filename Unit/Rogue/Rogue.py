from Unit.Unit import Unit
from Ability.Rogue_ability.Rogue_ability import *
from config.config import *

class Rogue(Unit):

    def __init__(self, name : str = "Rogue", hp : int = Hp.ROGUE_HP, dmg : int = Dmg.ROGUE_DMG):
        Unit.__init__(name, hp, dmg)
        self.ability = Rogue_ability(self)

