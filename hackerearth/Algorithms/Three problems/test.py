import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('sys.stdin.readline', side_effect=[
        '1',
        '9',
        '5 1 3',
        '2 7 0',
        '10 8 10',
        '6 2 9',
        '2 10 7',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(), '56\n')


if __name__ == '__main__':
    unittest.main()
