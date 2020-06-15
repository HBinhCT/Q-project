import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '5',
        '10 40 30 50 20',
    ])
    def test_case_0(self, input_values=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(), '14.1' + '\n')


if __name__ == '__main__':
    unittest.main()
