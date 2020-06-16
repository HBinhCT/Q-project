import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '9',
        '3 7 8 5 12 14 21 13 18',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(), '6' + '\n' + '12' + '\n' + '16' + '\n')


if __name__ == '__main__':
    unittest.main()
