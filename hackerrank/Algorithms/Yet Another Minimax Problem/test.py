import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.anotherMinimaxProblem([1, 2, 3, 4]), 5)

    def test_case_1(self):
        self.assertEqual(solution.anotherMinimaxProblem([1, 3, 2]), 2)


if __name__ == '__main__':
    unittest.main()
