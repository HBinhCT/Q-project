import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('sys.stdin.readline', side_effect=[
        '4 4 2',
        '1 2 3 4',
        '5 6 7 8',
        '9 10 11 12',
        '13 14 15 16',
        '2 3 2 5',
        '3 2 2 -3',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '1 2 3 4\n' +
                         '5 6 12 13\n' +
                         '9 7 13 17\n' +
                         '13 11 12 16\n')


if __name__ == '__main__':
    unittest.main()
