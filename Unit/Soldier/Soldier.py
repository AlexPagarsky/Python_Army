from Unit.Unit import Unit
from config import *


class Soldier(Unit):

    def __init__(self, name : str = "Soldier", hp : int = Hp.SOLDIER_HP.value, dmg : int = Dmg.SOLDIER_DMG.value):
        Unit.__init__(self, name, hp, dmg)


if __name__ == '__main__':
    sold = Soldier()
    print(sold)
