import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.getWays(4, [1, 2, 3]), 4)

    def test_case_1(self):
        self.assertEqual(solution.getWays(10, [2, 5, 3, 6]), 5)


if __name__ == '__main__':
    unittest.main()
