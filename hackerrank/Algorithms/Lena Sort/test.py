import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertIn(solution.lena(5, 6), [[2, 1, 4, 3, 5], [4, 2, 1, 3, 5]])
        self.assertEqual(solution.lena(5, 100), -1)

    def test_case_1(self):
        self.assertEqual(solution.lena(1, 0), [1])
        self.assertIn(solution.lena(4, 6), [[1, 2, 3, 4], [4, 3, 2, 1]])
        self.assertEqual(solution.lena(3, 2), [2, 1, 3])


if __name__ == '__main__':
    unittest.main()
