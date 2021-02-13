import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.funGame([1, 3, 4], [5, 3, 1]), 'First')
        self.assertEqual(solution.funGame([1, 1], [1, 1]), 'Tie')
        self.assertEqual(solution.funGame([2, 2], [3, 3]), 'Second')


if __name__ == '__main__':
    unittest.main()
