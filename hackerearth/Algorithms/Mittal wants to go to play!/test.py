import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('sys.stdin.readline', side_effect=[
        '1',
        '5 5',
        '1 2 2',
        '2 3 4',
        '3 4 5',
        '4 5 1',
        '1 4 7',
        '3',
        '4 20',
        '5 21',
        '3 5',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '6\n' +
                         '5\n' +
                         '0\n')


if __name__ == '__main__':
    unittest.main()
