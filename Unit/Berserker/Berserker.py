from Unit.Unit import *
from config.config import *
from State.Berserker_state.Berserker_state import *

class Berserker(Unit):

    def __init__(self, name : str = "Berserker",
                 hp : int = Hp.BERSERKER_HP,
                 dmg : int = Dmg.BERSERKER_DMG):
        Unit.__init__(name, hp, dmg)
        self.state = Berserker_state()