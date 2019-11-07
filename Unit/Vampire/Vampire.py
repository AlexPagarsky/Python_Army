from Unit.Unit import Unit
from Unit.Soldier.Soldier import Soldier
from config import *
import Ability.VampireAbility.VampireAbility as Vab


class Vampire(Unit):

    def __init__(self, name : str = "Vampire",
                 hp : int = Hp.VAMPIRE_HP.value,
                 dmg : int = Dmg.VAMPIRE_DMG.value):
        Unit.__init__(self, name, hp, dmg)
        self.ability = Vab.VampireAbility(self)
        self.state.type = "undead"
        self.state.turnable = False


if __name__ == "__main__":
    vamp = Vampire()
    sold = Soldier()
    sold2 = Soldier()
    print(vamp, '\n', sold)
    vamp.ability.turn(sold)
    print(vamp, '\n', sold)
    sold.ability.turn(sold2)
    print(vamp, '\n', sold, '\n', sold2)