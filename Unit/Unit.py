from Observer.Observable import Observable
from State.State import State
from Ability.Ability import *


class Unit(Observable):

    def __init__(self, name : str, hp : int, dmg : int):
        self.state = State(name, hp, dmg)
        self.ability = Ability(self)
        self.observers = set()

    @property
    def hp(self) -> int:
        return self.state.hp

    @property
    def hp_limit(self) -> int:
        return self.state.hp_limit

    @property
    def name(self) -> str:
        return self.state.name

    @property
    def dmg(self) -> int:
        return self.state.dmg

    @property
    def turnable(self) -> bool:
        return self.state.turnable

    def is_alive(self) -> bool:
        return self.state.hp > 0

    def add_hp(self, hp : int):
        self.state.add_hp(hp)

    def take_damage(self, dmg : int):
        self.state.take_damage(dmg)
        if self.hp == 0:
            self.notify(self.observers)

    def take_magic_damage(self, dmg : int):
        self.state.take_magic_damage(dmg)
        if self.hp == 0:
            self.notify(self.observers)

    def attack(self, enemy):
        self.ability.attack(enemy)

    def counter_attack(self, enemy):
        self.ability.counter_attack(enemy)

    def __str__(self) -> str:
        return str(self.name + ", " +  str(self.hp) + "/" + str(self.hp_limit) + " HP, " + str(self.dmg) + " DMG")


if __name__ == '__main__':
    test = Unit("test", 122, 12)
    print(test.hp)
    print(test.is_alive())