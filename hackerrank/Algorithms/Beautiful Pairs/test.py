import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.beautifulPairs([1, 2, 3, 4], [1, 2, 3, 3]), 4)

    def test_case_1(self):
        self.assertEqual(solution.beautifulPairs([3, 5, 7, 11, 5, 8], [5, 7, 11, 10, 5, 8]), 6)


if __name__ == '__main__':
    unittest.main()
