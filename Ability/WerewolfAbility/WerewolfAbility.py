from Ability.Ability import Ability
from State.WerewolfState.WerewolfState import WerewolfState
from types import MethodType
from config import *
from exceptions import *


class WerewolfAbility(Ability):

    def __init__(self, owner):
        Ability.__init__(self, owner)

    def turn(self, target=None):
        if target is None:
            if self.owner.state.type == "human":
                self.owner.state.type = "undead"
                self.owner.state.dmg *= 2
                self.owner.state.hp_limit += 50
                self.owner.state.hp = self.owner.state.hp_limit
            else:
                self.owner.state.type = "human"
                self.owner.state.dmg = Dmg.WEREWOLF_BASE_DMG.value
                if self.owner.hp > Hp.WEREWOLF_BASE_HP.value:
                    self.owner.state.hp = self.owner.state.hp // self.owner.state.hp_limit * 100
                self.owner.state.hp_limit = Hp.WEREWOLF_BASE_HP.value
        else:
            if target.turnable:
                health = (target.hp // target.hp_limit) * Hp.WEREWOLF_BASE_HP.value
                target.state = WerewolfState()
                target.state.hp = health
                target.ability = WerewolfAbility(target)
                if hasattr(target, "magic_state"):
                    del target.magic_state
                    del target.spellbook
                    del target.magic_ability
            else:
                raise CantTurn(self.owner.__class__.__name__, target)