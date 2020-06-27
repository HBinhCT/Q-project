import unittest
import solution


class TestQ(unittest.TestCase):
    def setUp(self):
        solution.lc, solution.mod = 26, 1000000007

    def test_case_0(self):
        solution.array, solution.factorial, solution.inverse_factorial = solution.initialize('week')
        self.assertEqual(solution.answerQuery(1, 4), 2)
        self.assertEqual(solution.answerQuery(2, 3), 1)

    def test_case_1(self):
        solution.array, solution.factorial, solution.inverse_factorial = solution.initialize('abab')
        self.assertEqual(solution.answerQuery(1, 4), 2)


if __name__ == '__main__':
    unittest.main()
