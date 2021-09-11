import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.balancedSums([1, 2, 3]), 'NO')
        self.assertEqual(solution.balancedSums([1, 2, 3, 3]), 'YES')

    def test_case_1(self):
        self.assertEqual(solution.balancedSums([1, 1, 4, 1, 1]), 'YES')
        self.assertEqual(solution.balancedSums([2, 0, 0, 0]), 'YES')
        self.assertEqual(solution.balancedSums([0, 0, 2, 0]), 'YES')


if __name__ == '__main__':
    unittest.main()
