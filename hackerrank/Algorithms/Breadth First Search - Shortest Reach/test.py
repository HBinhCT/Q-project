import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.bfs(4, 2, [[1, 2], [1, 3]], 1), [6, 6, -1])
        self.assertEqual(solution.bfs(3, 1, [[2, 3]], 2), [-1, 6])

    def test_case_1(self):
        self.assertEqual(solution.bfs(5, 3, [[1, 2], [1, 3], [3, 4]], 1), [6, 6, 12, -1])


if __name__ == '__main__':
    unittest.main()
