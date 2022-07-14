import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('sys.stdin.readline', side_effect=[
        '5 7',
        'aba',
        'broadway',
        'test',
        'why',
        'i',
        '1 tst',
        '1 text',
        '2 1 2',
        '1 caaabaaac',
        '1 qbpqfkd',
        '2 4 0',
        '1 wdwdsdubaa',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         'NO\n' +
                         'NO\n' +
                         'YES\n' +
                         'YES\n' +
                         'NO\n')


if __name__ == '__main__':
    unittest.main()
