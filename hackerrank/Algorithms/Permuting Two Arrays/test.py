import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.twoArrays(10, [2, 1, 3], [7, 8, 9]), 'YES')
        self.assertEqual(solution.twoArrays(5, [1, 2, 2, 1], [3, 3, 3, 4]), 'NO')

    def test_case_1(self):
        self.assertEqual(solution.twoArrays(10, [7, 6, 8, 4, 2], [5, 2, 6, 3, 1]), 'NO')


if __name__ == '__main__':
    unittest.main()
