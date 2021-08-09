import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '1',
        '3 3',
        '1 2 1234567',
        '2 3 2345678',
        '1 3 3456789',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(), '896631161\n')


if __name__ == '__main__':
    unittest.main()
