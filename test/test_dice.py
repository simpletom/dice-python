import unittest
from dice.dice import Dice


class TestDiceMethods(unittest.TestCase):

    def test_roll(self):
        dice = Dice()
        roll = dice.roll()
        last_roll = dice.last_roll()
        self.assertEqual(roll, last_roll)

    def test_history(self):
        dice = Dice()
        self.assertEqual([], dice.history)
        dice.roll()
        self.assertEqual([1], dice.history)
