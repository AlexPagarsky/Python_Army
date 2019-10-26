from Spell.AbstractSpell import AbstractSpell
from config import *


class Fireball(AbstractSpell):

    def __init__(self,
                 dmg : int = SpellDmg.FIREBALL_DMG.value,
                 cost : int = SpellCost.FIREBALL_COST.value):
        AbstractSpell.__init__(self, dmg, cost)

    def damage(self, target):
        if target.__class__.__name__ == "Werewolf":
            target.take_magic_damage(self.dmg*2)
        else:
            target.take_magic_damage(self.dmg)
