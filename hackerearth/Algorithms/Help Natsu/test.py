import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '1',
        '10',
        'abcd',
        'bcd',
        'abc',
        'abc',
        'abc',
        'bcd',
        'bge',
        'dbaa',
        'bcd',
        'bge',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '1 abcd\n' +
                         '1 dbaa\n' +
                         '2 bge\n' +
                         '3 abc\n' +
                         '3 bcd\n')


if __name__ == '__main__':
    unittest.main()
