import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.roadsAndLibraries(3, 2, 1, [[1, 2], [3, 1], [2, 3]]), 4)
        self.assertEqual(solution.roadsAndLibraries(6, 2, 5, [
            [1, 3],
            [3, 4],
            [2, 4],
            [1, 2],
            [2, 3],
            [5, 6],
        ]), 12)

    def test_case_1(self):
        self.assertEqual(solution.roadsAndLibraries(6, 2, 3, [[1, 2], [1, 3], [4, 5], [4, 6]]), 12)

    def test_case_2(self):
        self.assertEqual(solution.roadsAndLibraries(5, 6, 1, [[1, 2], [1, 3], [1, 4]]), 15)


if __name__ == '__main__':
    unittest.main()
