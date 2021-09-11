import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.minimumDistances([7, 1, 3, 4, 1, 7]), 3)

    def test_case_1(self):
        self.assertEqual(solution.minimumDistances([1, 2, 3, 4, 10]), -1)


if __name__ == '__main__':
    unittest.main()
