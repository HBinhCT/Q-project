import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('sys.stdin.readline', side_effect=[
        '2',
        '4 1',
        '2 15 36 43',
        '3 2',
        '27 30 35',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '41\n' +
                         '5\n')


if __name__ == '__main__':
    unittest.main()
