from Unit.Soldier import Soldier
from Unit.Rogue import Rogue
from Unit.Berserker import Berserker
from Unit.Vampire import Vampire
from Unit.Werewolf import Werewolf

from SpellCaster.Wizard import Wizard
from SpellCaster.Healer import Healer
from SpellCaster.Necromancer import Necromancer
from SpellCaster.Warlock import Warlock
from SpellCaster.Priest import Priest

from config import *
import exceptions
import unittest


class TestSold(unittest.TestCase):

    def test_attk(self):
        sold = Soldier.Soldier()
        sold2 = Soldier.Soldier()
        sold.attack(sold2)
        self.assertLess(sold2.hp, sold.hp)
        with self.assertRaises(exceptions.AttacksItself):
            sold.attack(sold)

    def test_turnable(self):
        sold = Soldier.Soldier()
        self.assertEqual(sold.turnable, True)

    def test_is_alive(self):
        sold = Soldier.Soldier()
        self.assertEqual(sold.is_alive(), True)
        sold.take_damage(100000)
        self.assertEqual(sold.is_alive(), False)


class TestRogue(unittest.TestCase):

    def test_turnable(self):
        rog = Rogue.Rogue()
        self.assertEqual(rog.turnable, True)

    def test_atk(self):
        rog = Rogue.Rogue()
        sold = Soldier.Soldier()
        rog.attack(sold)
        self.assertEqual(rog.hp, Hp.ROGUE_HP.value)

    def test_cattk(self):
        rog = Rogue.Rogue()
        sold = Soldier.Soldier()
        sold.attack(rog)
        self.assertLess(rog.hp, Hp.ROGUE_HP.value)


class TestBerserker(unittest.TestCase):

    def test_turnable(self):
        ber = Berserker.Berserker()
        self.assertEqual(ber.turnable, True)

    def test_atk(self):
        ber = Berserker.Berserker()
        sold = Soldier.Soldier()
        sold.attack(ber)
        self.assertLess(ber.hp, ber.hp_limit)

    def test_magattk(self):
        ber = Berserker.Berserker()
        wiz = Wizard.Wizard()
        wiz.cast_spell("Fireball", ber)
        self.assertEqual(ber.hp, ber.hp_limit)


class TestVampire(unittest.TestCase):

    def test_turnable(self):
        vamp = Vampire.Vampire()
        self.assertEqual(vamp.turnable, False)

    def test_lifesteal(self):
        vamp = Vampire.Vampire()
        sold = Soldier.Soldier()
        sold.attack(vamp)
        sold.attack(vamp)
        self.assertEqual(vamp.hp, 55)


class TestWerewolf(unittest.TestCase):

    def test_turnable(self):
        woof = Werewolf.Werewolf()
        self.assertEqual(woof.turnable, False)

    def test_turn(self):
        woof = Werewolf.Werewolf()
        woof.turn()
        self.assertEqual(woof.hp_limit, Hp.WEREWOLF_BASE_HP.value+50)
        self.assertEqual(woof.dmg, Dmg.WEREWOLF_BASE_DMG.value*2)

    def test_magattk(self):
        woof = Werewolf.Werewolf()
        wiz = Wizard.Wizard()
        woof.turn()
        wiz.cast_spell("Fireball", woof)
        self.assertEqual(woof.hp, 75)

    def test_except(self):
        woof = Werewolf.Werewolf()
        wof2 = Werewolf.Werewolf()
        sold = Soldier.Soldier()
        woof.take_damage(1000000)
        with self.assertRaises(exceptions.CantDoCauseDead):
            woof.attack(sold)
        with self.assertRaises(exceptions.TargetIsDead):
            wof2.attack(woof)
        with self.assertRaises(exceptions.CantTurn):
            wof2.turn(wof2)


class TestWizard(unittest.TestCase):

    def test_turnable(self):
        wiz = Wizard.Wizard()
        self.assertEqual(wiz.turnable, True)

    def test_attk(self):
        wiz = Wizard.Wizard()
        sold = Soldier.Soldier()
        wiz.attack(sold)
        self.assertEqual(sold.hp, sold.hp_limit - 15)

    def test_mana(self):
        wiz = Wizard.Wizard()
        sold = Soldier.Soldier()
        sold.state.hp = 100000
        wiz.cast_spell("Fireball", sold)
        wiz.cast_spell("Fireball", sold)
        wiz.cast_spell("Fireball", sold)
        with self.assertRaises(exceptions.OutOfMana):
            wiz.cast_spell("Fireball", sold)

    def test_except(self):
        wiz = Wizard.Wizard()
        wiz2 = Wizard.Wizard()
        sold = Soldier.Soldier()
        with self.assertRaises(exceptions.AttacksItself):
            wiz.cast_spell("Fireball", wiz)
        with self.assertRaises(exceptions.CantDoCauseDead):
            wiz.take_damage(100000)
            wiz.cast_spell("Fireball", sold)
        with self.assertRaises(exceptions.TargetIsDead):
            wiz2.attack(wiz)
        with self.assertRaises(exceptions.TargetIsDead):
            wiz2.cast_spell("Lightning", wiz)


class TestHealer(unittest.TestCase):

    def test_turnable(self):
        hel = Healer.Healer()
        self.assertEqual(hel.turnable, True)

    def test_attk(self):
        hel = Healer.Healer()
        sold = Soldier.Soldier()
        hel.attack(sold)
        self.assertEqual(sold.hp, sold.hp_limit - 5)

    def test_except(self):
        hel = Healer.Healer()
        hel2 = Healer.Healer()
        hel3 = Healer.Healer()
        hel2.take_damage(100000)
        with self.assertRaises(exceptions.TargetIsDead):
            hel.cast_spell("Heal", hel2)
        with self.assertRaises(exceptions.CantDoCauseDead):
            hel2.cast_spell("Heal", hel)
        with self.assertRaises(exceptions.AttacksItself):
            hel.attack(hel)
        with self.assertRaises(exceptions.OutOfMana):
            hel.cast_spell("Heal", hel3)
            hel.cast_spell("Heal", hel3)
            hel.cast_spell("Heal", hel3)
            hel.cast_spell("Heal", hel3)
            hel.cast_spell("Heal", hel3)
            print(hel, hel3)


if __name__ == "__main__":
    unittest.main()
