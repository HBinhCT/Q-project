import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '1',
        '5',
        '10 5 15 8 6',
        '1 2',
        '1 3',
        '1 4',
        '3 5',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(), '5\n')


if __name__ == '__main__':
    unittest.main()
