import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.compareTriplets([5, 6, 7], [3, 6, 10]), [1, 1])

    def test_case_1(self):
        self.assertEqual(solution.compareTriplets([17, 28, 30], [99, 16, 8]), [2, 1])


if __name__ == '__main__':
    unittest.main()
