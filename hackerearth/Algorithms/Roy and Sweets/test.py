import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '5',
        '5 8',
        '3 6',
        '10 7',
        '4 6',
        '2 5',
        '2',
        '5',
        '8',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(), '100\n')


if __name__ == '__main__':
    unittest.main()
