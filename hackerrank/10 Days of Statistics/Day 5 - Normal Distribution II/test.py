import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '70 10',
        '80',
        '60',
    ])
    def test_case_0(self, input_values=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(), '15.87' + '\n' + '84.13' + '\n' + '15.87' + '\n')


if __name__ == '__main__':
    unittest.main()
