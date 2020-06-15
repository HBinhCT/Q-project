import unittest
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=['2', '3'])
    def test_case_0(self, input_values=None):
        import solution
        self.assertEqual(solution.solveMeFirst(2, 3), 5)

    @patch('builtins.input', side_effect=['100', '1000'])
    def test_case_1(self, input_values=None):
        import solution
        self.assertEqual(solution.solveMeFirst(100, 1000), 1100)


if __name__ == '__main__':
    unittest.main()
