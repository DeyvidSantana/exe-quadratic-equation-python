import unittest
import sys
sys.path.append('..')

from quadratic_equation import QuadraticEquation


class TestQuadraticEquation(unittest.TestCase):
    def test_discriminant(self):
        self.assertEqual(QuadraticEquation.discriminant(2, 4, 2), 0)

    def test_roots_equation(self):
        discriminant = QuadraticEquation.discriminant(3, 5, 2)
        self.assertEqual(QuadraticEquation.roots_equation(3, 5, discriminant), [-0.6, -1])


if __name__ == '__main__':
    unittest.main()