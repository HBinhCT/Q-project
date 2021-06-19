import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.arrayManipulation(
            5,
            [
                [1, 2, 100],
                [2, 5, 100],
                [3, 4, 100],
            ]
        ), 200)

    def test_case_1(self):
        self.assertEqual(solution.arrayManipulation(
            10,
            [
                [1, 5, 3],
                [4, 8, 7],
                [6, 9, 1],
            ]
        ), 10)

    def test_case_2(self):
        self.assertEqual(solution.arrayManipulation(
            10,
            [
                [2, 6, 8],
                [3, 5, 7],
                [1, 8, 1],
                [5, 9, 15],
            ]
        ), 31)


if __name__ == '__main__':
    unittest.main()
