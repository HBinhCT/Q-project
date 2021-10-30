import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '3',
        '4',
        'abc?',
        'abc?',
        '4',
        'aab?',
        'a?aa',
        '5',
        'aaa?a',
        'bbbb?',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         'YES\n' +
                         'YES\n' +
                         'NO\n')


if __name__ == '__main__':
    unittest.main()
