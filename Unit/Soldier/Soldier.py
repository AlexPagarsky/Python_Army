from Unit.Unit import Unit
from config.config import *


class Soldier(Unit):

    def __init__(self, name : str = "Soldier", hp : int = Hp.SOLDIER_HP, dmg : int = Dmg.SOLDIER_DMG):
        Unit.__init__(self, name, hp, dmg)


if __name__ == '__main__':
    sold = Soldier()
    print(sold.is_alive())
