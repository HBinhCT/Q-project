import io
import unittest
from contextlib import redirect_stdout
from importlib import reload
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '6',
        '1 2 5 3 6 4',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(), '4 3 6 5 2 1\n')

    @patch('builtins.input', side_effect=[
        '15',
        '1 14 3 7 4 5 15 6 13 10 11 2 12 8 9',
    ])
    def test_case_1(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
            reload(solution)
        self.assertEqual(text_trap.getvalue(), '2 6 5 4 9 8 12 11 10 13 7 3 15 14 1\n')


if __name__ == '__main__':
    unittest.main()
