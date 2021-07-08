import io
import unittest
from contextlib import redirect_stdout
from importlib import reload
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '7',
        '3 5 2 1 4 6 7',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(), '3\n')

    @patch('builtins.input', side_effect=[
        '1',
        '15',
    ])
    def test_case_1(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
            reload(solution)
        self.assertEqual(text_trap.getvalue(), '0\n')

    @patch('builtins.input', side_effect=[
        '5',
        '3 1 7 5 4',
    ])
    def test_case_2(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
            reload(solution)
        self.assertEqual(text_trap.getvalue(), '3\n')


if __name__ == '__main__':
    unittest.main()
