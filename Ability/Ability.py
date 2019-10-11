import Unit

class Ability:

    def __init__(self, owner : Unit):
        self.owner = owner

    def attack(self, enemy : Unit):
        if enemy.is_alive():
            enemy.take_damage(self.owner.dmg)
            enemy.counter_attack(self)

    def counter_attack(self, enemy : Unit):
        if enemy.is_alive():
            enemy.take_damage(int(self.owner.dmg / 2))