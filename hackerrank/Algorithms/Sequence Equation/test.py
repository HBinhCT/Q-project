import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.permutationEquation([2, 3, 1]), [2, 3, 1])

    def test_case_1(self):
        self.assertEqual(solution.permutationEquation([4, 3, 5, 1, 2]), [1, 3, 5, 4, 2])


if __name__ == '__main__':
    unittest.main()
