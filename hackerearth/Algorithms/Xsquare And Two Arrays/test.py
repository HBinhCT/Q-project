import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('sys.stdin.readline', side_effect=[
        '5 5',
        '1 2 3 4 5',
        '5 4 3 2 1',
        '1 1 5',
        '2 1 5',
        '1 2 4',
        '2 2 4',
        '1 3 5',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '15\n' +
                         '15\n' +
                         '9\n' +
                         '9\n' +
                         '10\n')


if __name__ == '__main__':
    unittest.main()
