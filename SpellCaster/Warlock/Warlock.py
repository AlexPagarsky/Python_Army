from SpellCaster.SpellCaster import SpellCaster
from Unit.Soldier.Soldier import Soldier
from Spell import Fireball, Lightning, Heal
from SpellCaster.Warlock.Demon import Demon
from config import *


class Warlock(SpellCaster):

    def __init__(self, name: str = "Warlock",
                 hp: int = Hp.WARLOCK_HP.value,
                 mp: int = Mp.WARLOCK_MP.value,
                 dmg: int = Dmg.WARLOCK_DMG.value):
        SpellCaster.__init__(self, name, hp, mp, dmg)
        self.spellbook.add(
            Fireball.Fireball(),
            Lightning.Lightning(),
            Heal.Heal()
        )
        self.demons = list()

    def summon(self):
        self.demons.append(Demon(self))
        self.magic_state.spend_mana(SpellCost.DEMON_SUMM_COST.value)

    def unsummon(self):
        self.demons.pop()

    def unsummon_all(self):
        self.demons.clear()

    def command_to_attack(self, target):
        for demon in self.demons:
            demon.attack(target)

    def __str__(self) -> str:
        out = str(self.name + ", "
                  + str(self.hp) + "/" + str(self.hp_limit) + " HP, "
                  + str(self.mp) + "/" + str(self.mp_limit) + " MP, "
                  + str(self.dmg) + " DMG")

        if len(self.demons) != 0:
            out += ", " + str(len(self.demons)) + " demons summoned"

        return out


if __name__ == "__main__":
    war = Warlock()
    sold = Soldier()

    print(war, '\n', sold)

    war.summon()
    war.summon()

    war.command_to_attack(sold)
    print(war, '\n', sold)

    war.unsummon_all()

    print(war, '\n', sold)