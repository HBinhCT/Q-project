import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '60 7',
        '1 13 5 6 3 5 10 7 1 8 9 3 1 4 11 9 7 9 1 11 13 11 8 4 11 11 10 2 10 13 12 8 11 1 9 4 10 8 7 1 3 2 10 12 5 5 10 10 7 7 7 12 4 2 1 7 12 9 5 5',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(), '2\n')


if __name__ == '__main__':
    unittest.main()
