from State.Berserker_state.Berserker_state import *
from config import *


class Berserker(Unit):

    def __init__(self, name : str = "Berserker",
                 hp : int = Hp.BERSERKER_HP.value,
                 dmg : int = Dmg.BERSERKER_DMG.value):
        Unit.__init__(self, name, hp, dmg)
        self.state = Berserker_state(name, hp, dmg)


if __name__ == "__main__":
    beer = Berserker()
    print(beer)