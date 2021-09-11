import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.longestIncreasingSubsequence([2, 7, 4, 3, 8]), 3)

    def test_case_1(self):
        self.assertEqual(solution.longestIncreasingSubsequence([2, 4, 3, 7, 4, 5]), 4)


if __name__ == '__main__':
    unittest.main()
