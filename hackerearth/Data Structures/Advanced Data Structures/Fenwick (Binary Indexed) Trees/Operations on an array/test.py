import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('sys.stdin.readline', side_effect=[
        '7 1',
        '2 1 3 1 1 4 5',
        '5',
        '1 1 2 1',
        '1 2 3 1',
        '1 4 5 1',
        '2 2 2',
        '1 1 2 3',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '2\n' +
                         '2\n' +
                         '4\n' +
                         '-1\n')


if __name__ == '__main__':
    unittest.main()
