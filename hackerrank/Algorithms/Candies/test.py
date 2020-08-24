import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.candies(3, [1, 2, 2]), 4)

    def test_case_1(self):
        self.assertEqual(solution.candies(10, [2, 4, 2, 6, 1, 7, 8, 9, 2, 1]), 19)

    def test_case_2(self):
        self.assertEqual(solution.candies(8, [2, 4, 3, 5, 2, 6, 4, 5]), 12)


if __name__ == '__main__':
    unittest.main()
