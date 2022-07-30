import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('sys.stdin.readline', side_effect=[
        '1',
        '6 6',
        'J 1 3',
        '? 2 3',
        'J 3 6',
        '? 5 1',
        'J 1 5',
        '? 1 3',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(), '1 2\n')


if __name__ == '__main__':
    unittest.main()
