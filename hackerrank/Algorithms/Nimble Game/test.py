import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.nimbleGame([0, 2, 3, 0, 6]), 'First')
        self.assertEqual(solution.nimbleGame([0, 0, 0, 0]), 'Second')


if __name__ == '__main__':
    unittest.main()
