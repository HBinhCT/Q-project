import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.balancedForest(
            [1, 2, 2, 1, 1],
            [
                [1, 2],
                [1, 3],
                [3, 5],
                [1, 4],
            ],
        ), 2)
        self.assertEqual(solution.balancedForest(
            [1, 3, 5],
            [
                [1, 3],
                [1, 2],
            ],
        ), -1)

    def test_case_1(self):
        self.assertEqual(solution.balancedForest(
            [15, 12, 8, 14, 13],
            [
                [1, 2],
                [1, 3],
                [1, 4],
                [4, 5],
            ],
        ), 19)

    def test_case_2(self):
        self.assertEqual(solution.balancedForest(
            [12, 10, 8, 12, 14, 12],
            [
                [1, 2],
                [1, 3],
                [1, 4],
                [2, 5],
                [4, 6],
            ],
        ), 4)


if __name__ == '__main__':
    unittest.main()
