import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('sys.stdin.readline', side_effect=[
        '2',
        '5 3',
        '3 5 1 2 1',
        '5 3',
        '3 1 2 1 2',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '53211\n' +
                         '32211\n')


if __name__ == '__main__':
    unittest.main()
