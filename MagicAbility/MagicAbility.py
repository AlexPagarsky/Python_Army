from exceptions import *


class MagicAbility:

    def __init__(self, owner):
        self.owner = owner

    def cast_spell(self, spell, target):
        if self.owner.is_alive():
            if self.owner.mp >= spell.cost:
                if self.owner != target:
                    if not target.is_alive():
                        raise TargetIsDead()
                    self.owner.magic_state.spend_mana(spell.cost)
                    spell.damage(target)
                else:
                    raise AttacksItself(self.owner.name+" tries to attack itself")
            else:
                raise OutOfMana()
        else:
            raise CantDoCauseDead(self.owner)
