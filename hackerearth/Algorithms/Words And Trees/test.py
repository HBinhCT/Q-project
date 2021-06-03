import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '8 3',
        'o v s l v p d i',
        '1 3',
        '8 3',
        '4 8',
        '6 1',
        '5 3',
        '7 6',
        '2 3',
        '7 ifwrxl',
        '4 eyljywnm',
        '3 llvse',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '6\n' +
                         '7\n' +
                         '2\n')


if __name__ == '__main__':
    unittest.main()
