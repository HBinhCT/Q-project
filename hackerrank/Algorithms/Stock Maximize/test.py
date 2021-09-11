import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.stockmax([5, 3, 2]), 0)
        self.assertEqual(solution.stockmax([1, 2, 100]), 197)
        self.assertEqual(solution.stockmax([1, 3, 1, 2]), 3)

    def test_case_1(self):
        self.assertEqual(solution.stockmax([1, 2, 3, 4]), 6)
        self.assertEqual(solution.stockmax([5, 4, 3, 4, 5]), 4)


if __name__ == '__main__':
    unittest.main()
