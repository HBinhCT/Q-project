import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.chessboardGame(5, 2), 'Second')
        self.assertEqual(solution.chessboardGame(5, 3), 'First')
        self.assertEqual(solution.chessboardGame(8, 8), 'First')

    def test_case_1(self):
        self.assertEqual(solution.chessboardGame(7, 3), 'First')
        self.assertEqual(solution.chessboardGame(8, 12), 'First')
        self.assertEqual(solution.chessboardGame(9, 7), 'First')


if __name__ == '__main__':
    unittest.main()
