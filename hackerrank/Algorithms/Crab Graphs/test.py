import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.crabGraphs(8, 2, [
            [1, 4],
            [2, 4],
            [3, 4],
            [5, 4],
            [5, 8],
            [5, 7],
            [5, 6],
        ]), 6)
        self.assertEqual(solution.crabGraphs(6, 3, [
            [1, 2],
            [2, 3],
            [3, 4],
            [4, 5],
            [5, 6],
            [6, 1],
            [1, 4],
            [2, 5],
        ]), 6)


if __name__ == '__main__':
    unittest.main()
