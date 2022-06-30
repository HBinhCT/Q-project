import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '7',
        '1 2',
        '1 3',
        '2 4',
        '2 5',
        '3 6',
        '3 7',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertIn(tuple(map(int, text_trap.getvalue().strip().split())),
                      ((4, 6), (6, 4), (5, 6), (6, 5), (5, 7), (7, 5)))


if __name__ == '__main__':
    unittest.main()
