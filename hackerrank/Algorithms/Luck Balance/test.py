import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.luckBalance(
            3,
            [
                [5, 1],
                [2, 1],
                [1, 1],
                [8, 1],
                [10, 0],
                [5, 0],
            ]
        ), 29)

    def test_case_1(self):
        self.assertEqual(solution.luckBalance(
            5,
            [
                [13, 1],
                [10, 1],
                [9, 1],
                [8, 1],
                [13, 1],
                [12, 1],
                [18, 1],
                [13, 1],
            ]
        ), 42)

    def test_case_2(self):
        self.assertEqual(solution.luckBalance(
            2,
            [
                [5, 1],
                [4, 0],
                [6, 1],
                [2, 1],
                [8, 0],
            ]
        ), 21)


if __name__ == '__main__':
    unittest.main()
