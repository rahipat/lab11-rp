https://github.com/rahipat/lab11-rp

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(3, 5), -2)
        self.assertEqual(subtract(0, 0), 0)

    def test_div_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(5, 0)

    def test_logarithm(self):
        self.assertEqual(logarithm(8, 2), 3)
        self.assertEqual(logarithm(100, 10), 2)
        self.assertAlmostEqual(logarithm(9, 3), 2)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(10, 1)

    def test_mul(self):
        self.assertEqual(mul(2, 3), 6)
        self.assertEqual(mul(-2, 3), -6)
        self.assertEqual(mul(0, 5), 0)

    def test_div(self):
        self.assertEqual(div(6, 3), 2)
        self.assertEqual(div(-6, 3), -2)
        self.assertAlmostEqual(div(7, 2), 3.5)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(-5, 10)

    def test_hypotenuse(self):
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(5, 12), 13)
        self.assertAlmostEqual(hypotenuse(8, 15), 17)

    def test_square_root(self):
        self.assertEqual(square_root(9), 3)
        with self.assertRaises(ValueError):
            square_root(-4)

    def test_exp(self):
        self.assertEqual(exp(2, 3), 8)
        self.assertEqual(exp(5, 0), 1)
        self.assertEqual(exp(3, 2), 9)

# Do not touch this
if __name__ == "__main__":
    unittest.main()
