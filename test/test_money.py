from src.Dollar import Dollar
import unittest


class TestMoney(unittest.TestCase):
    """test class
    """
    def test_multiplication(self):

        five = Dollar(5)
        five.times(2)
        self.assertEqual(10, five.amount, "should be 10")
