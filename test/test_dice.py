import unittest
from dice.dice import Dice


class TestDiceMethods(unittest.TestCase):

    def setUp(self):
        self.dice = Dice()

    def tearDown(self):
        self.dice = None

    def test_roll(self):
        self.assertEqual(0, self.dice.last_roll())
        roll = self.dice.roll()
        self.assertEqual(roll, self.dice.last_roll())

    def test_history(self):
        self.assertEqual([], self.dice.history)
        roll = self.dice.roll()
        self.assertEqual([roll], self.dice.history)

        roll2 = self.dice.roll()
        self.assertEqual([roll,roll2], self.dice.history)

    def test_average_roll_empty(self):
        self.assertEqual(0, self.dice.average_roll())

    def test_average_roll_one_value(self):
        roll = self.dice.roll()
        self.assertEqual(roll, self.dice.average_roll())

    def test_average_roll_multiple_values(self):
        rolls = []
        rolls.append(self.dice.roll())
        rolls.append(self.dice.roll())
        rolls.append(self.dice.roll())


if __name__ == '__main__':
    unittest.main()
