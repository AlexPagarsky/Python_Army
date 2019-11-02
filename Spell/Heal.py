from Spell.AbstractSpell import AbstractSpell
from config import *


class Heal(AbstractSpell):

    def __init__(self, regen : int = SpellDmg.HEAL_REG.value,
                 cost : int = SpellCost.HEAL_COST.value):
        AbstractSpell.__init__(self, regen, cost)

    def damage(self, target):
        target.add_hp(self.dmg)
