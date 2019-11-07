class State:

    type = None

    def __init__(self, name : str, hp : int, dmg : int):
        self.name = name
        self.hp = hp
        self.hp_limit = hp
        self.dmg = dmg
        self.turnable = True

    def take_damage(self, dmg : int):
        self.hp -= dmg
        if self.hp <= 0: self.hp = 0

    def take_magic_damage(self, dmg : int):
        self.take_damage(dmg)

    def add_hp(self, hp):
        self.hp += hp
        if self.hp > self.hp_limit: self.hp = self.hp_limit
