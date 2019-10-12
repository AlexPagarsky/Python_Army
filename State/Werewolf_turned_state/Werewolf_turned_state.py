from State.State import *
from config.config import *


class Werewolf_turned_state(State):

    def __init__(self, name : str = "Werewolf",
                 hp : int = Hp.WEREWOLF_BASE_HP.value,
                 dmg : int = Dmg.WEREWOLF_BASE_DMG.value):
        State.__init__(self, name=name, hp=hp, dmg=dmg)
