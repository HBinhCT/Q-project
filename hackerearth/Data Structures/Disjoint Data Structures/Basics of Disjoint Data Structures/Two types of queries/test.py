import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('sys.stdin.readline', side_effect=[
        '10',
        'vwuhjdbgzp',
        '4',
        '1 a b',
        '2',
        '1 w z',
        '2',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '5\n' +
                         '4\n')


if __name__ == '__main__':
    unittest.main()
