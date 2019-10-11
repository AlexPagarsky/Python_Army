from Unit.Unit import *
from config.config import *


class Werewolf(Unit):

    def __init__(self, name : str, hp : int, dmg : int):
        Unit.__init__(name, hp, dmg)

