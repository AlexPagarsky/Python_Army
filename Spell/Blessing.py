from Unit.Unit import Unit
from Spell.AbstractSpell import AbstractSpell
from config import *


class Blessing(AbstractSpell):

    def __init__(self, regen : int = SpellDmg.BLESS_REG.value,
                 cost : int = SpellCost.BLESS_COST.value):
        AbstractSpell.__init__(self, regen, cost)

    def damage(self, target):
        if target.type == "Undead":
            target.take_magic_damage(self.dmg*2)
        else:
            target.add_hp(self.dmg)
