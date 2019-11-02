from config import *
from Spell.Fireball import Fireball
from Spell.Lightning import Lightning


class SpellBook:

    def __init__(self, *args):
        self.add(*args)

    def create(self, spell : str):
        return getattr(self, spell)

    def add(self, *args):
        for spell in args:
            setattr(self, spell.__class__.__name__, spell)
