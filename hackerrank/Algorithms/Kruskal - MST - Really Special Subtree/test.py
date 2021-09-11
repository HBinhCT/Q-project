import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.kruskals(
            4,
            [1, 1, 4, 2, 3, 3],
            [2, 3, 1, 4, 2, 4],
            [5, 3, 6, 7, 4, 5],
        ), 12)

    def test_case_1(self):
        self.assertEqual(solution.kruskals(
            5,
            [1, 1, 1, 1, 2, 3, 4],
            [2, 3, 4, 5, 3, 4, 5],
            [20, 50, 70, 90, 30, 40, 60],
        ), 150)


if __name__ == '__main__':
    unittest.main()
