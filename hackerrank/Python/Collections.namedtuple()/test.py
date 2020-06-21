import io
import unittest
from contextlib import redirect_stdout
from importlib import reload
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '5',
        'ID         MARKS      NAME       CLASS',
        '1          97         Raymond    7',
        '2          50         Steven     4',
        '3          91         Adrian     9',
        '4          72         Stewart    5',
        '5          80         Peter      6',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(), '78.00\n')

    @patch('builtins.input', side_effect=[
        '5',
        'MARKS      CLASS      NAME       ID',
        '92         2          Calum      1',
        '82         5          Scott      2',
        '94         2          Jason      3',
        '55         8          Glenn      4',
        '82         2          Fergus     5',
    ])
    def test_case_1(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
            reload(solution)
        self.assertEqual(text_trap.getvalue(), '81.00\n')


if __name__ == '__main__':
    unittest.main()
