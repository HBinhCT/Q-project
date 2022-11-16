import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('sys.stdin.readline', side_effect=[
        '5 5',
        '2 3 4 22 33',
    ])
    @patch('sys.stdin.readlines', return_value=[])
    def test_case_0(self, input_mock1=None, input_mock2=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(), '2\n')


if __name__ == '__main__':
    unittest.main()
