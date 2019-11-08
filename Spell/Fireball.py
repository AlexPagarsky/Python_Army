from Spell.AbstractSpell import AbstractSpell
from config import *


class Fireball(AbstractSpell):

    def __init__(self,
                 dmg : int = SpellDmg.FIREBALL_DMG.value,
                 cost : int = SpellCost.FIREBALL_COST.value):
        AbstractSpell.__init__(self, dmg, cost)

    def damage(self, target):
        target.take_magic_damage(self.dmg)
