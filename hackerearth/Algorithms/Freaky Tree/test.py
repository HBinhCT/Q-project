import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '1',
        '7',
        '1 2 0',
        '1 3 1',
        '2 4 0',
        '2 5 1',
        '3 6 1',
        '3 7 0',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(), '2\n')


if __name__ == '__main__':
    unittest.main()
