import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.nonDivisibleSubset(3, [1, 7, 2, 4]), 3)

    def test_case_1(self):
        self.assertEqual(
            solution.nonDivisibleSubset(7, [278, 576, 496, 727, 410, 124, 338, 149, 209, 702, 282, 718, 771, 575, 436]),
            11)


if __name__ == '__main__':
    unittest.main()
