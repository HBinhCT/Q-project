import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('sys.stdin.readline', side_effect=[
        '5 4',
        '1 4 2 3 5',
        '0 5',
        '8 20',
        '3 3',
        '2 9',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(), '5 17 14 17 17 ')


if __name__ == '__main__':
    unittest.main()
