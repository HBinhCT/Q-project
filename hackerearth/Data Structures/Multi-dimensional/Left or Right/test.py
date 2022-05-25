import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('sys.stdin.readline', side_effect=[
        '3 4',
        '1 2 3',
        '0 1 L',
        '1 3 L',
        '2 1 R',
        '1 5 L',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '0\n' +
                         '2\n' +
                         '1\n' +
                         '-1\n')


if __name__ == '__main__':
    unittest.main()
