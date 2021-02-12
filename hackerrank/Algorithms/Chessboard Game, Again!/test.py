import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.chessboardGame([
            [5, 4],
            [5, 8],
            [8, 2],
        ]), 'First')
        self.assertEqual(solution.chessboardGame([
            [7, 1],
            [7, 2],
            [7, 3],
            [7, 4],
            [7, 4],
            [7, 4],
        ]), 'Second')


if __name__ == '__main__':
    unittest.main()
