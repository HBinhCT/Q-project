import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('sys.stdin.readline', side_effect=[
        '3',
        'abc',
        'def',
        'abc',
        '3',
        '1 2 abc',
        '1 3 abc',
        '1 2 hgj',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '1\n' +
                         '2\n' +
                         '0\n')


if __name__ == '__main__':
    unittest.main()
