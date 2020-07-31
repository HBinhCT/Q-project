import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('sys.stdin.readline', side_effect=[
        '5 10',
        '50 40 30 20 10',
        '10',
        '20',
        '30',
        '40',
        '50',
        '60',
        '70',
        '80',
        '90',
        '100',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         'YES\n' +
                         'YES\n' +
                         'YES\n' +
                         'YES\n' +
                         'YES\n' +
                         'NO\n' +
                         'NO\n' +
                         'NO\n' +
                         'NO\n' +
                         'NO\n')


if __name__ == '__main__':
    unittest.main()
