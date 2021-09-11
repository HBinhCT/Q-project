import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.twoRobots(5, [
            [1, 5],
            [3, 2],
            [4, 1],
            [2, 4],
        ]), 11)
        self.assertEqual(solution.twoRobots(4, [
            [1, 2],
            [4, 3],
        ]), 2)


if __name__ == '__main__':
    unittest.main()
