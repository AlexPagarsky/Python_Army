from SpellCaster.SpellCaster import SpellCaster
from Spell.Fireball import Fireball
from Spell.Lightning import Lightning
from config import *
##
from Unit.Werewolf.Werewolf import Werewolf
##


class Wizard(SpellCaster):

    def __init__(self, name : str = "Wizard",
                 hp : int = Hp.WIZARD_HP.value,
                 mp : int = Mp.WIZARD_MP.value,
                 dmg : int = Dmg.WIZARD_DMG.value):
        SpellCaster.__init__(self, name, hp, mp, dmg)


if __name__ == "__main__":
    wiz = Wizard()
    woof = Werewolf()

    print(wiz)
    print(woof)

    # wiz.cast_spell(Fireball(), woof)
    wiz.cast_spell(Lightning(), woof)
    print(wiz)
    print(woof)
