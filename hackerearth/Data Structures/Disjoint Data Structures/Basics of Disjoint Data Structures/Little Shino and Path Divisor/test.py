import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('sys.stdin.readline', side_effect=[
        '5 2',
        '1 2 10',
        '1 3 6',
        '3 4 15',
        '3 5 15',
        '5',
        '3',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '4\n' +
                         '6\n')


if __name__ == '__main__':
    unittest.main()
