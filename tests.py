from Unit.Soldier import Soldier
from Unit.Rogue import Rogue
from Unit.Berserker import Berserker
from Unit.Werewolf import Werewolf
from Unit.Vampire import Vampire
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


if __name__ == "__main__":
    unittest.main()