import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('sys.stdin.readline', side_effect=[
        '5',
        '1 1',
        '2 2',
        '3 6',
        '4 7',
        '1000 1000',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         'Yes\n' +
                         'Yes\n' +
                         'No\n' +
                         'Yes\n' +
                         'No\n')


if __name__ == '__main__':
    unittest.main()
