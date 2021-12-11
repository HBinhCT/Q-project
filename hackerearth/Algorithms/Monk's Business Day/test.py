import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '2',
        '5 6',
        '1 2 2',
        '2 3 -1',
        '3 4 -7',
        '4 5 0',
        '2 3 -7',
        '3 5 6',
        '5 8',
        '1 5 10',
        '2 3 -6',
        '5 2 5',
        '4 5 9',
        '1 5 1',
        '2 4 -10',
        '2 3 -2',
        '4 1 1',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         'No\n' +
                         'Yes\n')


if __name__ == '__main__':
    unittest.main()
