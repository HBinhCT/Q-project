import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('sys.stdin.readline', side_effect=[
        '6 8',
        '2 3 7',
        '4 1 20',
        '5 1 5',
        '6 5 18',
        '3 6 10',
        '2 4 8',
        '5 4 7',
        '5 2 5',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         'all\n' +
                         'none\n' +
                         'none\n' +
                         'none\n' +
                         'all\n' +
                         'all\n')


if __name__ == '__main__':
    unittest.main()
