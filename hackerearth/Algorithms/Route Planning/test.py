import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('sys.stdin.readline', side_effect=[
        '8 4',
        '2 5 4',
        '3 6 1 2',
        '4 4 2 1 3',
        '2 7 8',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '2 3 4 6 3 -1 -1\n')


if __name__ == '__main__':
    unittest.main()
