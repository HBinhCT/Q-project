import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('sys.stdin.readline', return_value='8')
    @patch('sys.stdin.readlines', return_value=[
        '1003 100 4 0 0 0',
        '1002 200 6 0 0 0',
        '1001 300 8 0 0 0',
        '1004 100 3 0 0 0',
        '1005 200 3 0 0 0',
        '1006 300 5 0 0 0',
        '1007 100 3 0 0 0',
        '999 100 4 0 0 0',
    ])
    def test_case_0(self, input_mock=None, inputs_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '1003 200\n' +
                         '1002 300\n' +
                         '1001 400\n' +
                         '999 200\n' +
                         '1007 150\n')


if __name__ == '__main__':
    unittest.main()
