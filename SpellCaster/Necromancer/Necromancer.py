from SpellCaster.SpellCaster import SpellCaster
from Unit.Soldier.Soldier import Soldier
from Observer.Observer import Observer
from config import *


class Necromancer(SpellCaster, Observer):

    def __init__(self, name : str = "Necromancer",
                 hp : int = Hp.NECROMANCER_HP.value,
                 mp : int = Mp.NECROMANCER_MP.value,
                 dmg : int = Dmg.NECROMANCER_DMG.value):
        SpellCaster.__init__(self, name, hp, mp, dmg)

    def update(self):
        self.add_hp(15)

    def attack(self, enemy):
        enemy.observers.add(self)
        self.ability.attack(enemy)


if __name__ == "__main__":
    nec = Necromancer(hp = 1200)
    nec2 = Necromancer()
    nec3 = Necromancer()
    sold = Soldier()

    print(nec, '\n', sold, '\n', "--------------------------")

    nec.attack(sold)
    nec2.attack(sold)
    nec3.attack(sold)

    print(nec, '\n', sold, '\n', "--------------------------")

    nec.attack(sold)

    print(nec, '\n', sold, '\n', "--------------------------2")

    nec.attack(sold)
    print(nec, '\n', sold, '\n', "--------------------------")


    print(nec, '\n', sold)