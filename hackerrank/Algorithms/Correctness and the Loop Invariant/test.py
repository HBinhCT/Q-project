import unittest
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=['6', '4 1 3 5 6 2'])
    def test_case_0(self, input_values=None):
        import solution
        sample = [4, 1, 3, 5, 6, 2]
        solution.insertion_sort(sample)
        self.assertEqual(sample, [1, 2, 3, 4, 5, 6])


if __name__ == '__main__':
    unittest.main()
