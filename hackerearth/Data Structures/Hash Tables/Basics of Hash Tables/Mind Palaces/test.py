import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('sys.stdin.readline', side_effect=[
        '5 5',
        '-10 -5 -3 4 9',
        '-6 -2 0 5 10',
        '-4 -1 1 6 12',
        '2 3 7 8 13',
        '100 120 130 140 150',
        '3',
        '0',
        '-2',
        '170',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '1 2\n' +
                         '1 1\n' +
                         '-1 -1\n')


if __name__ == '__main__':
    unittest.main()
