import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.farVertices(5, 1, [[1, 2], [1, 3], [1, 4], [1, 5]]), 3)

    def test_case_1(self):
        self.assertEqual(solution.farVertices(5, 2, [[1, 2], [1, 3], [1, 4], [1, 5]]), 0)


if __name__ == '__main__':
    unittest.main()
