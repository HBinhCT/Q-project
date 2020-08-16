import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('sys.stdin.readline', side_effect=[
        '5 5',
        '11111',
        '00010',
    ])
    @patch('sys.stdin.readlines', return_value=[
        '1',
        '2',
        '3',
        '4',
        '5',
    ])
    def test_case_0(self, input_mock=None, inputs_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         'NO\n' +
                         'NO\n' +
                         'NO\n' +
                         'NO\n' +
                         'YES\n')


if __name__ == '__main__':
    unittest.main()
