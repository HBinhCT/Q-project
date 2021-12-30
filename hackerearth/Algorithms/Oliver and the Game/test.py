import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('sys.stdin.readline', side_effect=[
        '9',
        '1 2',
        '1 3',
        '2 6',
        '2 7',
        '6 9',
        '7 8',
        '3 4',
        '3 5',
        '5',
        '0 2 8',
        '1 2 8',
        '1 6 5',
        '0 6 5',
        '1 9 1',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         'YES\n' +
                         'NO\n' +
                         'NO\n' +
                         'NO\n' +
                         'YES\n')


if __name__ == '__main__':
    unittest.main()
