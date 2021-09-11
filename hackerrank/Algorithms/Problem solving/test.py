import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.problemSolving(2, [5, 4, 7]), 2)
        self.assertEqual(solution.problemSolving(1, [5, 3, 4, 5, 6]), 1)


if __name__ == '__main__':
    unittest.main()
