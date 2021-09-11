import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.intervalSelection([[1, 2], [2, 3], [2, 4]]), 2)
        self.assertEqual(solution.intervalSelection([[1, 5], [1, 5], [1, 5]]), 2)
        self.assertEqual(solution.intervalSelection([[1, 10], [1, 3], [4, 6], [7, 10]]), 4)
        self.assertEqual(solution.intervalSelection([[1, 10], [1, 3], [3, 6], [7, 10]]), 3)


if __name__ == '__main__':
    unittest.main()
