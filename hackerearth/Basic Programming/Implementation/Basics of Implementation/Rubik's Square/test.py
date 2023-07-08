import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '5 3 4',
        '8 6 3 9 1 ',
        '7 4 6 4 6 ',
        '3 4 2 0 4 ',
        '0 5 3 3 9 ',
        '8 5 4 9 3 ',
        '5 2 1 ',
        '4 5 5 4',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '1 8 6 3 9\n' +
                         '6 7 4 4 9\n' +
                         '3 4 2 3 9\n' +
                         '0 5 3 6 4\n' +
                         '3 8 5 0 4\n')


if __name__ == '__main__':
    unittest.main()
