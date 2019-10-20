from Unit.Unit import *
from config import *


class Werewolf(Unit):

    def __init__(self, name : str = "Werewolf",
                 hp : int = Hp.WEREWOLF_BASE_HP.value,
                 dmg : int = Dmg.WEREWOLF_BASE_DMG.value):
        Unit.__init__(self, name=name, hp=hp, dmg=dmg)
        self.state.type = "human"

    def turn(self):
        if self.state.type == "human":
            self.state.type = "undead"
            self.state.dmg *= 2
            self.state.hp_limit += 50
            self.state.hp = self.state.hp_limit
        else:
            self.state.dmg = Dmg.WEREWOLF_BASE_DMG.value
            if self.hp > Hp.WEREWOLF_BASE_HP.value:
                self.state.hp = int(self.state.hp / self.state.hp_limit * 100)
            self.state.hp_limit = Hp.WEREWOLF_BASE_HP.value
            self.state.type = "human"



if __name__ == "__main__":
    test = Werewolf()
    print(test)
    test.turn()
    print(test)
    test.take_damage(40)
    print(test)
    test.turn()
    print(test)