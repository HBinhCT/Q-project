import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('sys.stdin.readline', side_effect=[
        '3',
        '5 1',
        '1 1 1 1 1 ',
        '5 2',
        '1 3 1 1 3 ',
        '3 4 ',
        '1000 1000 1000',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '3\n' +
                         '1\n' +
                         '0\n')


if __name__ == '__main__':
    unittest.main()
