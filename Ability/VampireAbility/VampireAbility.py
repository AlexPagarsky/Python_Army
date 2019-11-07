from Ability.Ability import *
from Unit.Vampire import Vampire
from State.State import State
from Unit.Unit import Unit
from exceptions import *
from config import *


class VampireAbility(Ability):

    def __init__(self, owner : Vampire):
        Ability.__init__(self, owner)

    def attack(self, enemy : Unit):
        if enemy.is_alive():
            enemy.take_damage(self.owner.dmg)
            self.owner.add_hp(enemy.hp // 10)
            enemy.counter_attack(self)

    def counter_attack(self, enemy : Unit):
        if enemy.is_alive():
            enemy.take_damage(self.owner.dmg // 2)
            self.owner.add_hp(enemy.hp // 10)

    def turn(self, target):
        if target == self:
            raise CantTurn(self.owner.__class__.name, target)
        else:
            if target.turnable:
                target.state = State(name=target.name,
                                     hp=Hp.VAMPIRE_HP.value,
                                     dmg=Dmg.VAMPIRE_DMG.value)
                target.ability = VampireAbility(target)
                target.state.type = "undead"
                target.state.turnable = False
                if hasattr(target, "magic_ability"):
                    del target.magic_ability
                    del target.magic_state
                    del target.spellbook
                else:
                    raise CantTurn(self.__class__.__name__, target)