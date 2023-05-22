import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('sys.stdin.readline', side_effect=[
        '1',
        '7',
        '9 2 10 7 11 8 11',
        '3',
        '1 7',
        '1 6',
        '4 6',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '1\n' +
                         '0\n' +
                         '1\n')


if __name__ == '__main__':
    unittest.main()
