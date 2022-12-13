import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('sys.stdin.readline', side_effect=[
        '5',
        '1 4 6 2',
        '4 1 4 2',
        '8 2 1 2',
        '2 8 8 2',
        '1 2 1 3',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         'NO\n' +
                         'YES\n' +
                         'YES\n' +
                         'NO\n' +
                         'YES\n')


if __name__ == '__main__':
    unittest.main()
