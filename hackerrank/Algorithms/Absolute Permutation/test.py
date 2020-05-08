import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(list(solution.absolutePermutation(2, 1)), [2, 1])
        self.assertEqual(list(solution.absolutePermutation(3, 0)), [1, 2, 3])
        self.assertEqual(list(solution.absolutePermutation(3, 2)), [-1])

    def test_case_1(self):
        self.assertEqual(list(solution.absolutePermutation(2, 1)), [2, 1])
        self.assertEqual(list(solution.absolutePermutation(10, 5)), [6, 7, 8, 9, 10, 1, 2, 3, 4, 5])
        self.assertEqual(list(solution.absolutePermutation(7, 5)), [-1])
        self.assertEqual(list(solution.absolutePermutation(2, 1)), [2, 1])
        self.assertEqual(list(solution.absolutePermutation(2, 0)), [1, 2])
        self.assertEqual(list(solution.absolutePermutation(2, 0)), [1, 2])
        self.assertEqual(list(solution.absolutePermutation(1, 0)), [1])
        self.assertEqual(list(solution.absolutePermutation(10, 5)), [6, 7, 8, 9, 10, 1, 2, 3, 4, 5])
        self.assertEqual(list(solution.absolutePermutation(10, 0)), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(list(solution.absolutePermutation(6, 0)), [1, 2, 3, 4, 5, 6])

    def test_case_bonus(self):
        self.assertEqual(list(solution.absolutePermutation(100, 2)), [
            3, 4, 1, 2, 7, 8, 5, 6, 11, 12, 9, 10, 15, 16, 13, 14, 19, 20, 17, 18, 23, 24, 21, 22, 27, 28, 25, 26, 31,
            32, 29, 30, 35, 36, 33, 34, 39, 40, 37, 38, 43, 44, 41, 42, 47, 48, 45, 46, 51, 52, 49, 50, 55, 56, 53, 54,
            59, 60, 57, 58, 63, 64, 61, 62, 67, 68, 65, 66, 71, 72, 69, 70, 75, 76, 73, 74, 79, 80, 77, 78, 83, 84, 81,
            82, 87, 88, 85, 86, 91, 92, 89, 90, 95, 96, 93, 94, 99, 100, 97, 98
        ])


if __name__ == '__main__':
    unittest.main()
