from src.Dollar import Dollar
import unittest


class TestMoney(unittest.TestCase):
    """test class
    """
    def test_multiplication(self):

        five = Dollar(5)
        product = five.times(2)
        self.assertEqual(10, product.amount, "should be 10")

        product = five.times(3)
        self.assertEqual(15, product.amount, 'should be 15')


if __name__ == '__main__':
    unittest.main()
