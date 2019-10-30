from Spell.AbstractSpell import AbstractSpell
from config import *


class Lightning(AbstractSpell):

    def __init__(self, dmg : int = SpellDmg.LIGHTNING_DMG.value,
                 cost : int = SpellCost.LIGHTNING_COST.value):
        AbstractSpell.__init__(self, dmg, cost)

    def damage(self, target):
        if target.__class__.__name__ == "Werewolf":
            target.take_magic_damage(self.dmg*2)
        else:
            target.take_magic_damage(self.dmg)
