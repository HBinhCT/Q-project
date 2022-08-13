import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('sys.stdin.readline', side_effect=[
        '10 15',
        '9 10 2',
        '6 10 2',
        '4 9 1',
        '3 4 2',
        '7 6 1',
        '2 9 1',
        '1 7 1',
        '8 9 2',
        '5 4 1',
        '7 4 2',
        '3 8 1',
        '9 9 2',
        '3 6 1',
        '5 6 1',
        '6 8 1',
        '5',
        '4 4 9 4',
        '3 1 5 3',
        '3 8 8 1',
        '3 7 8 2',
        '7 5 9 3',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '2\n' +
                         '2\n' +
                         '1\n' +
                         '2\n' +
                         '2\n')


if __name__ == '__main__':
    unittest.main()
