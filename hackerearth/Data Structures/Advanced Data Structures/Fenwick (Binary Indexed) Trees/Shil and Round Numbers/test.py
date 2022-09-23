import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('sys.stdin.readline', side_effect=[
        '5 5 ',
        '1 2 33 456 111',
        '1 1 2',
        '1 1 5',
        '2 1 6',
        '2 2 1000',
        '1 1 5',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '2\n' +
                         '4\n' +
                         '3\n')


if __name__ == '__main__':
    unittest.main()
