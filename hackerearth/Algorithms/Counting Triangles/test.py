import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('sys.stdin.readline', return_value='5')
    @patch('sys.stdin.readlines', return_value=[
        '7 6 5',
        '5 7 6',
        '8 2 9',
        '2 3 4',
        '2 4 3',
    ])
    def test_case_0(self, input_mock=None, inputs_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(), '1\n')


if __name__ == '__main__':
    unittest.main()
