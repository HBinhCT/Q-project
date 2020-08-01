import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('sys.stdin.readline', side_effect=[
        '2',
        '9',
        '7 7 3 3 3 2 2 2 1',
        '8 8 7 7 5 5 4 3 2',
        '6',
        '6 5 4 4 4 4',
        '2 2 2 2 2 2',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(), '5\n0\n')


if __name__ == '__main__':
    unittest.main()
