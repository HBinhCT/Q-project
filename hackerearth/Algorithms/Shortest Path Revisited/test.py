import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '5 6 1',
        '1 2 2',
        '1 3 6',
        '2 4 6',
        '2 5 8',
        '3 5 4',
        '4 5 1',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(), '0 0 0 2 2\n')


if __name__ == '__main__':
    unittest.main()