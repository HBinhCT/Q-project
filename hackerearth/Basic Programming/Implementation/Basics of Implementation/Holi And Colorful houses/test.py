import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '2',
        '5 2',
        'RRRGG',
        '1 5',
        '3 2',
        '5 2',
        'GGRGG',
        '2 5',
        '3 1',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '1\n' +
                         '0\n' +
                         '0\n' +
                         '1\n')


if __name__ == '__main__':
    unittest.main()
