import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.verticalRooks([1, 2, 2], [3, 1, 1]), 'player-2')

    def test_case_1(self):
        self.assertEqual(solution.verticalRooks([3, 3, 3, 3], [4, 4, 4, 4]), 'player-1')


if __name__ == '__main__':
    unittest.main()
