from abc import ABC


class AbstractSpell(ABC):

    def __init__(self, dmg : int, cost : int):
        self.dmg = dmg
        self.cost = cost

    def damage(self, target):
        pass
