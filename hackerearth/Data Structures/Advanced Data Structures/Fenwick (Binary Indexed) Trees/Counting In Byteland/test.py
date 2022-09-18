import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '10 6',
        '1 0 0 6 6',
        '1 9 9 9 10',
        '1 8 5 9 5',
        '2 3 4 5 9 10 9',
        '1 6 6 1 23',
        '2 0 0 0 8 9 10',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '6\n' +
                         '10\n')


if __name__ == '__main__':
    unittest.main()
