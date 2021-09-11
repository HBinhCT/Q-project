import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.minimumLoss([5, 10, 3]), 2)

    def test_case_1(self):
        self.assertEqual(solution.minimumLoss([20, 7, 8, 2, 5]), 2)


if __name__ == '__main__':
    unittest.main()
