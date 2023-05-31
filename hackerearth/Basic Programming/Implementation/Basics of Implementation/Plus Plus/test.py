import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('sys.stdin.readline', side_effect=[
        '6 6',
        '4 0 8 4 3 0',
        '7 8 3 4 7 4',
        '9 2 6 0 5 8',
        '2 0 6 3 9 7',
        '1 5 0 5 6 3',
        '5 0 0 0 4 1',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(), '166\n')


if __name__ == '__main__':
    unittest.main()
