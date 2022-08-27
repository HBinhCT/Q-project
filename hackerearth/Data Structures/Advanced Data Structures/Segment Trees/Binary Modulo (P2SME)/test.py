import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('sys.stdin.readline', side_effect=[
        '1',
        '01010101',
        '5',
        '0 1 3',
        '1 2 1',
        '0 2 5',
        '1 3 1',
        '0 0 7',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '0\n' +
                         '3\n' +
                         '2\n')


if __name__ == '__main__':
    unittest.main()
