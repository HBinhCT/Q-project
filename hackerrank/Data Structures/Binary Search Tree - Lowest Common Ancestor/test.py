import io
import unittest
from contextlib import redirect_stdout
from importlib import reload
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '6',
        '4 2 3 1 7 6',
        '1 7',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(), '4\n')

    @patch('builtins.input', side_effect=[
        '2',
        '1 2',
        '1 2',
    ])
    def test_case_1(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
            reload(solution)
        self.assertEqual(text_trap.getvalue(), '1\n')

    @patch('builtins.input', side_effect=[
        '7',
        '5 3 8 2 4 6 7',
        '7 3',
    ])
    def test_case_2(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
            reload(solution)
        self.assertEqual(text_trap.getvalue(), '5\n')


if __name__ == '__main__':
    unittest.main()
