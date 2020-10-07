import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '3',
        '0110000000000000000000000000000000000000',
        '5',
        '0010000000000000000000000000000000000000',
        '5',
        '0100000000100000001000100000101000001000',
        '16807',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '8\n' +
                         '15\n' +
                         '26866\n')


if __name__ == '__main__':
    unittest.main()
