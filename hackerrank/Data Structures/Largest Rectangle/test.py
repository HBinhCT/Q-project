import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.largestRectangle([1, 2, 3, 4, 5]), 9)

    def test_case_1(self):
        self.assertEqual(solution.largestRectangle([1, 3, 5, 9, 11]), 18)

    def test_case_2(self):
        self.assertEqual(solution.largestRectangle([11, 11, 10, 10, 10]), 50)


if __name__ == '__main__':
    unittest.main()
