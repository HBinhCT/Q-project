import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78',
        '2',
        '1 2 3 4 5',
        '100 11 12',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(), 'False\n')


if __name__ == '__main__':
    unittest.main()
