import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.boardCutting([2], [1]), 4)

    def test_case_1(self):
        self.assertEqual(solution.boardCutting([2, 1, 3, 1, 4], [4, 1, 2]), 42)


if __name__ == '__main__':
    unittest.main()
