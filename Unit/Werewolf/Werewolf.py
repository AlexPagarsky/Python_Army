from Unit.Unit import *
from State.WerewolfState.WerewolfState import WerewolfState
from Ability.WerewolfAbility.WerewolfAbility import WerewolfAbility
from Unit.Vampire.Vampire import Vampire
from Unit.Soldier.Soldier import Soldier
from config import *
from exceptions import *


class Werewolf(Unit):

    def __init__(self, name : str = "Werewolf",
                 hp : int = Hp.WEREWOLF_BASE_HP.value,
                 dmg : int = Dmg.WEREWOLF_BASE_DMG.value):
        Unit.__init__(self, name=name, hp=hp, dmg=dmg)
        self.state = WerewolfState(name, hp, dmg)
        self.ability = WerewolfAbility(self)
        self.state.type = "human"

    def turn(self, target=None):
        self.ability.turn(target)


if __name__ == "__main__":
    woof = Werewolf()
    sold = Soldier()
    vamp = Vampire()

    print(woof, '\n', sold)
    woof.turn(sold)
    sold.state.name = "Zmey"
    print(woof, '\n', sold)
    sold.ability.turn()
    sold.ability.turn()
    # sold.ability.turn()
    woof.turn()
    print(woof, sold)
    # sold.turn(vamp)
