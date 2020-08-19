import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('sys.stdin.readline', side_effect=[
        '6',
        '2 5 3 8 9 5',
        '3',
        '25',
        '30',
        '8',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         'Alice\n' +
                         'Bob\n' +
                         'Alice\n')


if __name__ == '__main__':
    unittest.main()
