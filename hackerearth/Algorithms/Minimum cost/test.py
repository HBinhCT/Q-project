import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '6',
        '6',
        '1 4 3 2 5 6',
        '6',
        '3 2 6 5 4 1',
        '6',
        '3 6 2 4 1 5',
        '6',
        '5 4 6 3 2 1',
        '6',
        '1 6 5 4 2 3',
        '6',
        '5 1 3 6 2 4',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '3\n' +
                         '0\n' +
                         '0\n' +
                         '0\n' +
                         '1\n' +
                         '1\n')


if __name__ == '__main__':
    unittest.main()
