from State.State import *
from config import *


class WerewolfState(State):

    def __init__(self, name : str = "Werewolf",
                 hp : int = Hp.WEREWOLF_BASE_HP.value,
                 dmg : int = Dmg.WEREWOLF_BASE_DMG.value):
        State.__init__(self, name=name, hp=hp, dmg=dmg)
        self.turnable = False

    def take_magic_damage(self, dmg : int):
        if self.type == "undead":
            self.take_damage(int(dmg*1.5))
        else:
            self.take_damage(dmg)