import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '1',
        '3 2',
        '1 KITKAT',
        '2 FIVESTAR KITKAT',
        '1 KITKAT',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(), 'Yes\n')


if __name__ == '__main__':
    unittest.main()
