import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.largestPermutation(1, [4, 2, 3, 5, 1]), [5, 2, 3, 4, 1])

    def test_case_1(self):
        self.assertEqual(solution.largestPermutation(1, [2, 1, 3]), [3, 1, 2])

    def test_case_2(self):
        self.assertEqual(solution.largestPermutation(1, [2, 1]), [2, 1])


if __name__ == '__main__':
    unittest.main()
