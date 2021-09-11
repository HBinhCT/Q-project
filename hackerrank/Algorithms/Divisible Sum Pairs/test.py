import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.divisibleSumPairs(6, 3, [1, 3, 2, 6, 1, 2]), 5)


if __name__ == '__main__':
    unittest.main()
