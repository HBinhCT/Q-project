import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('sys.stdin.readline', side_effect=[
        '2',
        '6 6',
        '1 2 2',
        '2 5 5',
        '2 3 4',
        '1 4 1',
        '4 3 3',
        '3 5 1',
        '1 3 6',
        '10 10',
        '1 5 78',
        '1 8 221',
        '2 7 92',
        '2 8 159',
        '3 5 55',
        '3 6 179',
        '3 10 237',
        '4 8 205',
        '5 6 191',
        '8 10 157',
        '6 3 2',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         'No Train Found.\n' +
                         '692\n' +
                         '6 3 5 1 8 2\n')


if __name__ == '__main__':
    unittest.main()
