import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.minTime([[2, 1, 8], [1, 0, 5], [2, 4, 5], [1, 3, 4]], [2, 4, 0]), 10)

    def test_case_1(self):
        self.assertEqual(solution.minTime([[0, 1, 4], [1, 2, 3], [1, 3, 7], [0, 4, 2]], [2, 3, 4]), 5)

    def test_case_2(self):
        self.assertEqual(solution.minTime([[0, 3, 3], [1, 4, 4], [1, 3, 4], [0, 2, 5]], [1, 3, 4]), 8)


if __name__ == '__main__':
    unittest.main()
