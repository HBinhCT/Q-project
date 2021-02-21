import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.permutationGame([1, 3, 2]), 'Alice')
        self.assertEqual(solution.permutationGame([5, 3, 2, 1, 4]), 'Bob')


if __name__ == '__main__':
    unittest.main()
