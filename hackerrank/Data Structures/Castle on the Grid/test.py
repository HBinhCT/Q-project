import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.minimumMoves(['.X.', '.X.', '...'], 0, 0, 0, 2), 3)

    def test_case_1(self):
        self.assertEqual(solution.minimumMoves(['...', '.X.', '.X.'], 2, 0, 0, 2), 2)

    def test_case_2(self):
        self.assertEqual(solution.minimumMoves(['...', '.X.', '.X.'], 2, 0, 2, 2), 3)


if __name__ == '__main__':
    unittest.main()
