import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.runningTime([2, 1, 3, 1, 2]), 4)

    def test_case_1(self):
        self.assertEqual(solution.runningTime([1, 1, 2, 2, 3, 3, 5, 5, 7, 7, 9, 9]), 0)


if __name__ == '__main__':
    unittest.main()
