import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.shortestReach(4, [[1, 2, 24], [1, 4, 20], [3, 1, 3], [4, 3, 12]], 1), [24, 3, 15])

    def test_case_1(self):
        self.assertEqual(solution.shortestReach(5, [[1, 2, 10], [1, 3, 6], [2, 4, 8]], 2), [10, 16, 8, -1])


if __name__ == '__main__':
    unittest.main()
