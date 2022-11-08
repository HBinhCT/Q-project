import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '31415926',
        '7',
        '2 2',
        '3 1',
        '1 1',
        '4 3',
        '5 2',
        '8 2',
        '7 3',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(), '6992511\n')


if __name__ == '__main__':
    unittest.main()
