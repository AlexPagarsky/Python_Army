from Ability.Ability import *
from Unit.Vampire import Vampire


class Vampire_ability(Ability):

    def __init__(self, owner : Vampire):
        Ability.__init__(self, owner)

    def attack(self, enemy : Unit):
        if enemy.is_alive():
            enemy.take_damage(self.owner.dmg)
            self.owner.add_hp(int(enemy.hp/10))
            enemy.counter_attack(self)

    def counter_attack(self, enemy : Unit):
        if enemy.is_alive():
            enemy.take_damage(int(self.owner.dmg / 2))
            self.owner.add_hp(int(enemy.hp/10))
