import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '3',
        '5 7',
        '2 5 7',
        '1 4 3',
        '2 3 5',
        '1 3 2',
        '1 5 4',
        '3 4 6',
        '1 2 1',
        '4 6',
        '1 2 1000000000',
        '2 3 1000000000',
        '3 4 1000000000',
        '4 1 1000000000',
        '1 1 1',
        '2 3 1000000000',
        '6 7',
        '1 2 1',
        '2 3 1',
        '3 1 1',
        '4 5 2',
        '5 6 2',
        '6 4 2',
        '1 4 100000',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '10\n' +
                         '4 1 1 1 1\n' +
                         '3000000000\n' +
                         '1 1 2 2\n' +
                         '100006\n' +
                         '2 1 2 2 1 2\n')


if __name__ == '__main__':
    unittest.main()
