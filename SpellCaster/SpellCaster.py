from Unit.Unit import Unit
from MagicState.MagicState import MagicState
from MagicAbility.MagicAbility import MagicAbility
from SpellBook.SpellBook import SpellBook
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

    def __str__(self) -> str:
        return str(self.name + ", "
                   +  str(self.hp) + "/" + str(self.hp_limit) + " HP, "
                   + str(self.mp) + "/" +str(self.mp_limit) + " MP, "
                   + str(self.dmg) + " DMG")