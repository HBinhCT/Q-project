import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.solve([7, 4, 5, 2, 3, -4, -3, -5]), 3)
        self.assertEqual(solution.solve([1, -4]), 1)
        self.assertEqual(solution.solve([4, 3, 2, 3, 1]), 1)
        self.assertEqual(solution.solve([7, 1, -2, -3, -4, 2, 0, -1]), 7)


if __name__ == '__main__':
    unittest.main()
