import Unit


class Ability:

    def __init__(self, owner):
        self.owner = owner

    def attack(self, enemy : Unit):
        if enemy.is_alive() and enemy != self:
            enemy.take_damage(self.owner.dmg)
            enemy.counter_attack(self.owner)

    def counter_attack(self, enemy : Unit):
        if self.owner.is_alive() and enemy.is_alive():
            enemy.take_damage(self.owner.dmg // 2)