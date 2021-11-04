import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '3',
        'delhi',
        'bengaluru',
        'hyderabad',
        '0 10 20',
        '10 0 55',
        '20 55 0',
        '4',
        'bengaluru',
        'delhi',
        'hyderabad',
        'bengaluru',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(), '95\n')


if __name__ == '__main__':
    unittest.main()
