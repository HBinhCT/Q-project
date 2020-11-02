import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.nimGame([1, 1]), 'Second')
        self.assertEqual(solution.nimGame([2, 1, 4]), 'First')

    def test_case_1(self):
        self.assertEqual(solution.nimGame([3, 5]), 'First')
        self.assertEqual(solution.nimGame([1, 3, 5, 7]), 'Second')


if __name__ == '__main__':
    unittest.main()
