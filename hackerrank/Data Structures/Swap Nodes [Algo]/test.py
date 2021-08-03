import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertListEqual(
            list(solution.swapNodes(
                [
                    [2, 3],
                    [-1, -1],
                    [-1, -1],
                ],
                [1, 1],
            )),
            [
                [3, 1, 2],
                [2, 1, 3],
            ],
        )

    def test_case_1(self):
        self.assertListEqual(
            list(solution.swapNodes(
                [
                    [2, 3],
                    [4, 5],
                    [6, -1],
                    [-1, 7],
                    [8, 9],
                    [10, 11],
                    [12, 13],
                    [-1, 14],
                    [-1, -1],
                    [15, -1],
                    [16, 17],
                    [-1, -1],
                    [-1, -1],
                    [-1, -1],
                    [-1, -1],
                    [-1, -1],
                    [-1, -1],
                ],
                [2, 3],
            )),
            [
                [14, 8, 5, 9, 2, 4, 13, 7, 12, 1, 3, 10, 15, 6, 17, 11, 16],
                [9, 5, 14, 8, 2, 13, 7, 12, 4, 1, 3, 17, 11, 16, 6, 10, 15],
            ],
        )

    def test_case_2(self):
        self.assertListEqual(
            list(solution.swapNodes(
                [
                    [2, 3],
                    [4, -1],
                    [5, -1],
                    [6, -1],
                    [7, 8],
                    [-1, 9],
                    [-1, -1],
                    [10, 11],
                    [-1, -1],
                    [-1, -1],
                    [-1, -1],
                ],
                [2, 4],
            )),
            [
                [2, 9, 6, 4, 1, 3, 7, 5, 11, 8, 10],
                [2, 6, 9, 4, 1, 3, 7, 5, 10, 8, 11],
            ],
        )


if __name__ == '__main__':
    unittest.main()
