import unittest
from dice import dice


class TestDiceMethods(unittest.TestCase):

    def test_roll(self):
        dice.roll()
        last_roll = dice.last_roll()
