import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '1 4',
        '1 2 3 4',
        '5 6 7 8',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '[[ 6  8 10 12]]' + '\n' +
                         '[[-4 -4 -4 -4]]' + '\n' +
                         '[[ 5 12 21 32]]' + '\n' +
                         '[[0 0 0 0]]' + '\n' +
                         '[[1 2 3 4]]' + '\n' +
                         '[[    1    64  2187 65536]]' + '\n')


if __name__ == '__main__':
    unittest.main()
