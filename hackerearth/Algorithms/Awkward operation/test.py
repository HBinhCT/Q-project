import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '5',
        '3',
        '5 -1 3',
        '4 1 2',
        '4',
        '3 2 -2 -3',
        '3 0 2 -5',
        '7',
        '-10 -3 3 -4 -1 7 2',
        '-15 1 1 3 0 2 2',
        '4',
        '1 -1 1 -1',
        '-1 1 -1 1',
        '7',
        '-10 -3 3 -4 -1 7 2',
        '-15 1 1 3 0 4 -2',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         'Yes\n' +
                         'Yes\n' +
                         'Yes\n' +
                         'No\n' +
                         'No\n')


if __name__ == '__main__':
    unittest.main()
