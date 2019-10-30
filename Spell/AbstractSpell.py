from abc import ABC, abstractmethod


class AbstractSpell(ABC):

    def __init__(self, dmg : int, cost : int):
        self.dmg = dmg
        self.cost = cost

    @abstractmethod
    def damage(self, target):
        pass

    @property
    def name(self) -> str:
        return self.__