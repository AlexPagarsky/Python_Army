from exceptions import *


class MagicAbility:

    def __init__(self, owner):
        self.owner = owner

    def cast_spell(self, spell, target):
        if self.owner.is_alive() and self.owner.mp >= spell.cost:
            if self.owner != target:
                self.owner.magic_state.spend_mana(spell.cost)
                spell.damage(target)
            else:
                raise AttacksItself(self.owner.name+" tries to attack itself")
