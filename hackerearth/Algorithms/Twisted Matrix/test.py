import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '3',
        '2  5  12',
        '22 45 55',
        '1  6  8',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '1 2 5\n' +
                         '45 55 6\n' +
                         '22 12 8\n')


if __name__ == '__main__':
    unittest.main()
