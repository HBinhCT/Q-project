import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]), 3)

    def test_case_1(self):
        self.assertEqual(solution.sockMerchant(10, [1, 1, 3, 1, 2, 1, 3, 3, 3, 3]), 4)


if __name__ == '__main__':
    unittest.main()
