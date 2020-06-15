import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '10',
        '10 9.8 8 7.8 7.7 1.7 6 5 1.4 2 ',
        '200 44 32 24 22 17 15 12 8 4',
    ])
    def test_case_0(self, input_values=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(), '0.903' + '\n')


if __name__ == '__main__':
    unittest.main()
