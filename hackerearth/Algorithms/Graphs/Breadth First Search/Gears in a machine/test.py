import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('sys.stdin.readline', side_effect=[
        '8 8 3',
        '1 1 1 1 1 1 1 1',
        '1 2',
        '1 3',
        '2 4',
        '3 4',
        '4 5',
        '6 7',
        '7 8',
        '8 6',
        '1 5 1 1',
        '1 5 1 -1',
        '6 7 1 1',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         'NO\n' +
                         'YES\n' +
                         'NO\n')


if __name__ == '__main__':
    unittest.main()
