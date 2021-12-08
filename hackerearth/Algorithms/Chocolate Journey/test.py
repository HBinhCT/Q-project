import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('sys.stdin.readline', side_effect=[
        '7 3 1 6',
        '1',
        '4 7 1',
        '3 5 7',
        '6 1 3',
        '6 2',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(), '-1\n')


if __name__ == '__main__':
    unittest.main()
