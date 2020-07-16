import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.quickestWayUp(
            [
                [32, 62],
                [42, 68],
                [12, 98],
            ],
            [
                [95, 13],
                [97, 25],
                [93, 37],
                [79, 27],
                [75, 19],
                [49, 47],
                [67, 17],
            ]), 3)
        self.assertEqual(solution.quickestWayUp(
            [
                [8, 52],
                [6, 80],
                [26, 42],
                [2, 72],
            ],
            [
                [51, 19],
                [39, 11],
                [37, 29],
                [81, 3],
                [59, 5],
                [79, 23],
                [53, 7],
                [43, 33],
                [77, 21]
            ]), 5)


if __name__ == '__main__':
    unittest.main()
