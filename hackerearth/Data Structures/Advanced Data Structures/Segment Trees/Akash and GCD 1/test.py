import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('sys.stdin.readline', side_effect=[
        '3',
        '3 4 3',
        '6',
        'C 1 2',
        'C 1 3',
        'C 3 3',
        'U 1 4',
        'C 1 3',
        'C 1 2',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '13\n' +
                         '18\n' +
                         '5\n' +
                         '21\n' +
                         '16\n')


if __name__ == '__main__':
    unittest.main()
