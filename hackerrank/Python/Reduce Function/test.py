import unittest
from fractions import Fraction

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(sorted(solution.product([Fraction(*[1, 2]), Fraction(*[3, 4]), Fraction(*[10, 6])])), [5, 8])


if __name__ == '__main__':
    unittest.main()
