import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '3',
        '5',
        '1 2 3 5 6',
        '9',
        '9 8 5 6 3 2 1 4 7',
        '1',
        '2',
        '5',
        '3 6 5 4 1',
        '7',
        '1 2 3 5 6 8 9',
        '3',
        '9 8 2',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         'True\n'
                         + 'False\n'
                         + 'False\n')


if __name__ == '__main__':
    unittest.main()
