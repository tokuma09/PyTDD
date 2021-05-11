from src.Dollar import Dollar
from src.Franc import Franc
import unittest


class TestMoney(unittest.TestCase):
    """test class
    """
    def test_multiplication(self):

        five = Dollar(5)
        self.assertEqual(Dollar(10), five.times(2), "should be 10")
        self.assertEqual(Dollar(15), five.times(3), "should be 15")

    def test_equality(self):
        self.assertTrue(Dollar(5).equals(Dollar(5)))
        self.assertFalse(Dollar(5).equals(Dollar(6)))

        self.assertTrue(Franc(5).equals(Franc(5)))
        self.assertFalse(Franc(5).equals(Franc(6)))

    def test_franc_multiplication(self):
        five = Franc(5)

        self.assertEqual(Franc(10), five.times(2), "should be 10")
        self.assertEqual(Franc(15), five.times(3), "should be 15")


if __name__ == '__main__':
    unittest.main()
