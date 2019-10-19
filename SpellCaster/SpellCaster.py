from config.config import *
from Unit.Unit import Unit


class SpellCaster(Unit):

    def __init__(self, name : str, hp : int, mp : int, dmg : int):
        Unit.__init__(self, name, hp, dmg)
        self.magic_state = MagicState()