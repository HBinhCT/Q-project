import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.summingPieces([1, 3, 6]), 73)

    def test_case_1(self):
        self.assertEqual(solution.summingPieces([4, 2, 9, 10, 1]), 971)


if __name__ == '__main__':
    unittest.main()
