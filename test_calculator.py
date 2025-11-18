# https://github.com/rahipat/lab11-rp

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(5, 7), 12)
        self.assertEqual(add(-3, 2), -1)
        self.assertEqual(add(10, 0), 10)

    def test_subtract(self):
        self.assertEqual(subtract(10, 4), 6)
        self.assertEqual(subtract(2, 7), -5)
        self.assertEqual(subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(-3, 5), -15)
        self.assertEqual(mul(0, 8), 0)

    def test_divide(self):
        self.assertEqual(div(10, 2), 5)
        self.assertEqual(div(-12, 3), -4)
        self.assertAlmostEqual(div(9, 4), 2.25)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(8, 0)

    def test_logarithm(self):
        self.assertEqual(logarithm(16, 2), 4)
        self.assertEqual(logarithm(81, 3), 4)
        self.assertAlmostEqual(logarithm(27, 3), 3)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(15, 1)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(0, 2)
        with self.assertRaises(ValueError):
            logarithm(-8, 2)

    def test_hypotenuse(self):
        self.assertEqual(hypotenuse(6, 8), 10)
        self.assertEqual(hypotenuse(9, 12), 15)
        self.assertAlmostEqual(hypotenuse(7, 24), 25)

    def test_sqrt(self):
        self.assertEqual(square_root(16), 4)
        self.assertAlmostEqual(square_root(3), 1.7321, places=4)
        with self.assertRaises(ValueError):
            square_root(-9)

    def test_exp(self):
        self.assertEqual(exp(3, 2), 9)
        self.assertEqual(exp(2, 5), 32)
        self.assertEqual(exp(4, 0), 1)

# Do not touch this
if __name__ == "__main__":
    unittest.main()
