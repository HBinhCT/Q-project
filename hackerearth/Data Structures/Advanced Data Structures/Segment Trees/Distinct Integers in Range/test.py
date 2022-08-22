import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('sys.stdin.readline', side_effect=[
        '5',
        '1 2 3 4 5',
        '2 1 3 1 4',
        '2',
        '1 3 4 5',
        '1 3 3 5',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '4\n' +
                         '4\n')


if __name__ == '__main__':
    unittest.main()
