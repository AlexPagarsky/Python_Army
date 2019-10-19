from State.State import *
from config.config import *


class Werewolf_turned_state(State):

    def __init__(self, name : str = "Werewolf",
                 hp : int = Hp.WEREWOLF_BASE_HP.value,
                 dmg : int = Dmg.WEREWOLF_BASE_DMG.value):
        State.__init__(self, name=name, hp=hp, dmg=dmg)

    def take_magic_damage(self, dmg : int):
        pass
        # if self.type == "undead":
        #     self.take_damage(dmg*2)
        # else:
        #     self.take_damage(dmg)