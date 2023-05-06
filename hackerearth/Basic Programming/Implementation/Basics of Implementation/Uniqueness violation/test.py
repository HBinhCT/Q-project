import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '1',
        '10',
        '15 15 12 13 13 13 1 1 1 1',
        '20 30 15 16 12 1 23 24 1 2',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(), '85\n')


if __name__ == '__main__':
    unittest.main()
