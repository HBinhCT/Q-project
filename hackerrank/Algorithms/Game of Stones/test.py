import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.gameOfStones(1), 'Second')
        self.assertEqual(solution.gameOfStones(2), 'First')
        self.assertEqual(solution.gameOfStones(3), 'First')
        self.assertEqual(solution.gameOfStones(4), 'First')
        self.assertEqual(solution.gameOfStones(5), 'First')
        self.assertEqual(solution.gameOfStones(6), 'First')
        self.assertEqual(solution.gameOfStones(7), 'Second')
        self.assertEqual(solution.gameOfStones(10), 'First')


if __name__ == '__main__':
    unittest.main()
