import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '6 1',
        '1 1 1',
        '1 1 1',
        '1 1 1',
        '10 11 10 0 0 1',
        '9 10 11 1 0 1',
        '10 9 10 0 2 1',
        '11 10 9 10 9 11',
        '9 10 11 9 99 11',
        '10 9 9 11 10 10',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '40 61 43 22 3 2\n' +
                         '59 90 62 34 6 5\n' +
                         '59 89 70 52 35 24\n' +
                         '59 89 78 159 152 133\n' +
                         '59 88 88 177 180 150\n' +
                         '38 58 59 149 150 130\n')


if __name__ == '__main__':
    unittest.main()
