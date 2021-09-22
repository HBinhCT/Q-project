import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '5',
        'windows 2 32 100 100',
        'windows 4 64 10 52',
        'android 2 32 56 9',
        'ios 2 32 20 63',
        'windows 2 32 452 50',
        '2',
        'windows 2 32 500',
        'ios 4 32 100',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '100\n' +
                         '-1\n')


if __name__ == '__main__':
    unittest.main()
