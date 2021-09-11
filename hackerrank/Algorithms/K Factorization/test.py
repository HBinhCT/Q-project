import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.kFactorization(12, [2, 3, 4]), [1, 3, 12])

    def test_case_1(self):
        self.assertEqual(solution.kFactorization(15, [2, 10, 6, 9, 11]), [-1])

    def test_case_2(self):
        self.assertEqual(solution.kFactorization(72, [2, 4, 6, 9, 3, 7, 16, 10, 5]), [1, 2, 8, 72])


if __name__ == '__main__':
    unittest.main()
