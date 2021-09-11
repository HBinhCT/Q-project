import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.beautifulTriplets(3, [1, 2, 4, 5, 7, 8, 10]), 3)

    def test_case_1(self):
        self.assertEqual(solution.beautifulTriplets(3, [1, 6, 7, 7, 8, 10, 12, 13, 14, 19]), 2)


if __name__ == '__main__':
    unittest.main()
