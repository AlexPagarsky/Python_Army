from Unit.Unit import Unit
from Ability.Ability import Ability



class Rogue_ability(Ability):
    def __init__(self, owner : Unit):
        Ability.__init__(self, owner)

    def attack(self, enemy : Unit):
        if enemy.is_alive():
            enemy.take_damage(self.owner.dmg)