from Unit.Soldier.Soldier import Soldier
from config import *


class Demon(Soldier):

    def __init__(self, owner, name : str = "Demon"):
        Soldier.__init__(self, name,
                         Hp.DEMON_HP.value,
                         Dmg.DEMON_DMG.value)
        self.owner = owner
