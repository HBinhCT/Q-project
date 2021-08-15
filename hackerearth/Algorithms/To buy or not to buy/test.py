import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '1',
        '7 10',
        '1 2 5',
        '1 4 3',
        '1 5 12',
        '1 6 5',
        '4 5 1',
        '5 6 2',
        '5 3 1',
        '3 6 16',
        '4 7 1',
        '2 4 1',
        '5',
        '1 6',
        '2 4',
        '3 5',
        '3 6',
        '1 2',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(), '2/5\n')


if __name__ == '__main__':
    unittest.main()
