import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.lonelyinteger([1]), 1)

    def test_case_1(self):
        self.assertEqual(solution.lonelyinteger([1, 1, 2]), 2)

    def test_case_2(self):
        self.assertEqual(solution.lonelyinteger([0, 0, 1, 2, 1]), 2)


if __name__ == '__main__':
    unittest.main()
