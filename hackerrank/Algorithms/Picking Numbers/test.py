import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.pickingNumbers([4, 6, 5, 3, 3, 1]), 3)

    def test_case_1(self):
        self.assertEqual(solution.pickingNumbers([1, 2, 2, 3, 1, 2]), 5)


if __name__ == '__main__':
    unittest.main()
