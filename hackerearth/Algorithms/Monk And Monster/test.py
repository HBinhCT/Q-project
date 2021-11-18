import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '3',
        'aaaaa',
        'aa',
        '5',
        '1 6 3 10 2 ',
        'qwer',
        'asd',
        '4',
        '1 2 3 4 ',
        'oksirok',
        'ok',
        '7',
        '4 2 5 11 12 4 6',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '16\n' +
                         '0\n' +
                         '8\n')


if __name__ == '__main__':
    unittest.main()
