import unittest

from src.Money import Money
from src.Bank import Bank
from src.Sum import Sum


class TestMoney(unittest.TestCase):
    """test class
    """
    def test_simple_addition(self):

        five = Money.dollar(5)
        sum_val = five.plus(five)

        bank = Bank()
        reduced = bank.reduce(sum_val, 'USD')
        self.assertEqual(Money.dollar(10), reduced)

    def test_plus_return_sum(self):
        five = Money.dollar(5)
        result = five.plus(five)

        sum_val: Sum = result

        self.assertEqual(five, sum_val.augend)
        self.assertEqual(five, sum_val.addend)

    def test_reduce_sum(self):

        sum_val = Sum(Money.dollar(3), Money.dollar(4))
        bank = Bank()

        result = bank.reduce(sum_val, 'USD')

        self.assertEqual(Money.dollar(7), result)

    def test_reduce_money(self):

        bank = Bank()
        result = bank.reduce(Money.dollar(1), 'USD')
        self.assertEqual(Money.dollar(1), result)

    def test_multiplication(self):

        five = Money.dollar(5)
        self.assertEqual(Money.dollar(10), five.times(2), "should be 10")
        self.assertEqual(Money.dollar(15), five.times(3), "should be 15")

    def test_equality(self):
        self.assertTrue(Money.dollar(5) == Money.dollar(5))
        self.assertFalse(Money.dollar(5) == Money.dollar(6))

        self.assertFalse(Money.dollar(5) == Money.franc(5))

    def test_currency(self):
        self.assertEqual("USD", Money.dollar(1).currency)
        self.assertEqual("CHF", Money.franc(1).currency)
