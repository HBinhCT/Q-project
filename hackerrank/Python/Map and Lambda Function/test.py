import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(list(map(solution.cube, solution.fibonacci(5))), [0, 1, 1, 8, 27])

    def test_case_1(self):
        self.assertEqual(list(map(solution.cube, solution.fibonacci(6))), [0, 1, 1, 8, 27, 125])


if __name__ == '__main__':
    unittest.main()
