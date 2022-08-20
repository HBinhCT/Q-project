import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '10 20',
        '5 1 5',
        '2 1 2 5',
        '3 3 6 9',
        '4 3 4',
        '4 6 8',
        '4 6 9',
        '3 3 7 8',
        '5 2 7',
        '2 3 7 5',
        '4 6 7',
        '4 2 6',
        '5 10 10',
        '3 9 9 7',
        '3 1 7 4',
        '4 2 6',
        '3 2 9 1',
        '3 6 9 8',
        '4 9 10',
        '3 1 7 6',
        '5 7 10',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '0\n' +
                         '18\n' +
                         '9\n' +
                         '9\n' +
                         '8\n' +
                         '1\n' +
                         '4\n' +
                         '0\n' +
                         '24\n' +
                         '14\n' +
                         '12\n')


if __name__ == '__main__':
    unittest.main()
