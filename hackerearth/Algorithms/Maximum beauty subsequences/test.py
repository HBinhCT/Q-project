import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '6',
        'abdbca',
        '5',
        'a b 2',
        'a b 3',
        'b c 10',
        'b a 6',
        'a c 8',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(), '15\n')


if __name__ == '__main__':
    unittest.main()
