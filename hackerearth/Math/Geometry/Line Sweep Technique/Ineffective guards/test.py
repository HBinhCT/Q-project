import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('sys.stdin.readline', side_effect=[
        '3 3',
        '-1 -1',
        '-3 -1',
        '-100 -150',
        '0 0',
        '-2 0',
        '-94 -145',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(), '1\n')


if __name__ == '__main__':
    unittest.main()
