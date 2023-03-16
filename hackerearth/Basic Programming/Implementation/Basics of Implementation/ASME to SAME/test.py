import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '3',
        '4',
        '???n',
        'aman',
        '4',
        'aacb',
        'aabc',
        '3',
        '?po',
        'oyo',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         'Yes\n' +
                         'Yes\n'
                         'No\n')


if __name__ == '__main__':
    unittest.main()
