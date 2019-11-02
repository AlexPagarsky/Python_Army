from SpellCaster.SpellCaster import SpellCaster
from Spell import Fireball, Lightning, Heal
from config import *


class Healer(SpellCaster):

    def __init__(self, name : str = "Healer",
                 hp : int = Hp.HEALER_HP.value,
                 mp : int = Mp.HEALER_MP.value,
                 dmg : int = Dmg.HEALER_DMG.value):
        SpellCaster.__init__(self, name, hp, mp, dmg)
        self.spellbook.add(
            Fireball.Fireball(SpellDmg.FIREBALL_DMG.value//2),
            Lightning.Lightning(SpellDmg.LIGHTNING_DMG.value//2),
            Heal.Heal()
        )