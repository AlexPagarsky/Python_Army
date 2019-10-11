class State:

    type = None

    def __init__(self, name : str, hp : int, dmg : int):
        self.name = name
        self.hp = hp
        self.hp_limit = hp
        self.dmg = dmg
        self.turnable = False

    def take_damage(self, dmg : int):
        self.state.hp -= dmg
        if self.hp <= 0: self.state.hp = 0

    def take_magic_damage(self, dmg : int):
        self.take_damage(dmg)

    def add_hp(self, hp):
        self.hp += hp