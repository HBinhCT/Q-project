import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('sys.stdin.readline', side_effect=[
        '3',
        '3 2 4 2',
        '3 3 6 3',
        '3 3 4 3',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         'Yes\n' +
                         'Yes\n' +
                         'No\n')


if __name__ == '__main__':
    unittest.main()
