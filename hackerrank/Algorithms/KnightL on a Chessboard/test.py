import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.knightlOnAChessboard(5),
                         [
                             [4, 4, 2, 8],
                             [4, 2, 4, 4],
                             [2, 4, -1, -1],
                             [8, 4, -1, 1],
                         ])


if __name__ == '__main__':
    unittest.main()
