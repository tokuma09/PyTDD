import unittest

from src.Money import Money


class TestMoney(unittest.TestCase):
    """test class
    """
    def test_multiplication(self):

        five = Money.dollar(5)
        self.assertEqual(Money.dollar(10), five.times(2), "should be 10")
        self.assertEqual(Money.dollar(15), five.times(3), "should be 15")

    def test_equality(self):
        self.assertTrue(Money.dollar(5) == Money.dollar(5))
        self.assertFalse(Money.dollar(5) == Money.dollar(6))

        self.assertTrue(Money.franc(5) == Money.franc(5))
        self.assertFalse(Money.franc(5) == Money.franc(6))

        self.assertFalse(Money.dollar(5) == Money.franc(5))

    def test_franc_multiplication(self):

        five = Money.franc(5)

        self.assertEqual(Money.franc(10), five.times(2), "should be 10")
        self.assertEqual(Money.franc(15), five.times(3), "should be 15")

    def test_currency(self):
        self.assertEqual("USD", Money.dollar(1).currency)
        self.assertEqual("CHF", Money.franc(1).currency)
