from Unit.Unit import Unit
from MagicState.MagicState import MagicState
from MagicAbility.MagicAbility import MagicAbility
from exceptions import *


class SpellCaster(Unit):

    def __init__(self, name : str, hp : int, mp : int, dmg : int):
        Unit.__init__(self, name, hp, dmg)
        self.magic_state = MagicState(mp=mp, mp_limit=mp)
        self.magic_ability = MagicAbility(self)

    @property
    def mp(self) -> int:
        return self.magic_state.mp

    @property
    def mp_limit(self) -> int:
        return self.magic_state.mp_limit

    def cast_spell(self, spell, target):
        self.magic_ability.cast_spell(spell, target)
