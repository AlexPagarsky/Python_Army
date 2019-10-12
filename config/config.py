from enum import Enum


class Hp(Enum):
    SOLDIER_HP = 100
    ROGUE_HP = 70
    BERSERKER_HP = 120
    VAMPIRE_HP = 80
    WEREWOLF_BASE_HP = 100


class Dmg(Enum):
    SOLDIER_DMG = 20
    ROGUE_DMG = 35
    BERSERKER_DMG = 50
    VAMPIRE_DMG = 25
    WEREWOLF_BASE_DMG = 25
