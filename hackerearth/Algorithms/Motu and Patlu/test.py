import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '3',
        '5',
        '2 6 2 1 7',
        '4',
        '15 2 1 3',
        '5',
        '2 4 12 4 7',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '4 1\n' +
                         'Motu\n' +
                         '1 3\n' +
                         'Patlu\n' +
                         '3 2\n' +
                         'Motu\n')


if __name__ == '__main__':
    unittest.main()
