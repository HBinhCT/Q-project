import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.stones(3, 1, 2), [2, 3, 4])
        self.assertEqual(solution.stones(4, 10, 100), [30, 120, 210, 300])

    def test_case_1(self):
        self.assertEqual(solution.stones(7, 9, 11), [54, 56, 58, 60, 62, 64, 66])
        self.assertEqual(solution.stones(4, 8, 16), [24, 32, 40, 48])


if __name__ == '__main__':
    unittest.main()
