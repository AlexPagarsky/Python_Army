from enum import Enum


class Hp(Enum):
    SOLDIER_HP = 100
    ROGUE_HP = 70
    BERSERKER_HP = 120
    VAMPIRE_HP = 80
    WEREWOLF_BASE_HP = 100
    WIZARD_HP = 60
    HEALER_HP = 50
    PRIEST_HP = 50
    WARLOCK_HP = 70
    DEMON_HP = 50


class Mp(Enum):
    WIZARD_MP = 100
    HEALER_MP = 120
    PRIEST_MP = 90
    WARLOCK_MP = 90


class Dmg(Enum):
    SOLDIER_DMG = 20
    ROGUE_DMG = 35
    BERSERKER_DMG = 50
    VAMPIRE_DMG = 25
    WEREWOLF_BASE_DMG = 25
    WIZARD_DMG = 15
    HEALER_DMG = 5
    PRIEST_DMG = 5
    WARLOCK_DMG = 20
    DEMON_DMG = 30


class SpellDmg(Enum):
    FIREBALL_DMG = 50
    LIGHTNING_DMG = 80
    HEAL_REG = 40
    BLESS_REG = 80


class SpellCost(Enum):
    FIREBALL_COST = 30
    LIGHTNING_COST = 50
    HEAL_COST = 30
    BLESS_COST = 45
    DEMON_SUMM_COST = 30