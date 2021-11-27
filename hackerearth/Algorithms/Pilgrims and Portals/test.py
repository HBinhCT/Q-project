import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('sys.stdin.readline', side_effect=[
        '1',
        '5 10 3',
        '1 2 10',
        '1 3 5',
        '1 4 10',
        '1 5 80',
        '2 3 9',
        '2 4 1',
        '2 5 20',
        '3 4 100',
        '3 5 2',
        '4 5 20',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(), '14\n')


if __name__ == '__main__':
    unittest.main()
