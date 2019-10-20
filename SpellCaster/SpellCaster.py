from Unit.Unit import Unit
from MagicState.MagicState import MagicState


class SpellCaster(Unit):

    def __init__(self, name : str, hp : int, mp : int, dmg : int):
        Unit.__init__(self, name, hp, dmg)
        self.magic_state = MagicState(mp=mp, mp_limit=mp)

    @property
    def mp(self) -> int:
        return self.magic_state.mp

    @property
    def mp_limit(self) -> int:
        return self.magic_state.mp_limit