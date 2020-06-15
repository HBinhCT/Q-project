import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '95 85',
        '85 95',
        '80 70',
        '70 65',
        '60 70',
    ])
    def test_case_0(self, input_values=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(), '78.288\n')


if __name__ == '__main__':
    unittest.main()
