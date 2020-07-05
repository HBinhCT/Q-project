import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.cutTheTree(
            [100, 200, 100, 500, 100, 600],
            [
                [1, 2],
                [2, 3],
                [2, 5],
                [4, 5],
                [5, 6],
            ]
        ), 400)

    def test_case_1(self):
        self.assertEqual(solution.cutTheTree(
            [205, 573, 985, 242, 830, 514, 592, 263, 142, 915],
            [
                [2, 8],
                [10, 5],
                [1, 7],
                [6, 9],
                [4, 3],
                [8, 10],
                [5, 1],
                [7, 6],
                [9, 4],
            ]
        ), 99)


if __name__ == '__main__':
    unittest.main()
