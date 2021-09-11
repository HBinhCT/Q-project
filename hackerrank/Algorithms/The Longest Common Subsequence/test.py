import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertIn(
            solution.longestCommonSubsequence([1, 2, 3, 4, 1], [3, 4, 1, 2, 1, 3]),
            [[1, 2, 3], [1, 2, 1], [3, 4, 1]]
        )

    def test_case_1(self):
        self.assertIn(
            solution.longestCommonSubsequence(
                [3, 9, 8, 3, 9, 7, 9, 7, 0],
                [3, 3, 9, 9, 9, 1, 7, 2, 0, 6]
            ),
            [[3, 3, 9, 9, 7, 0], [3, 9, 9, 9, 7, 0]]
        )


if __name__ == '__main__':
    unittest.main()
