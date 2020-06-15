import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '10',
        '64630 11735 14216 99233 14470 4978 73429 38120 51135 67060',
    ])
    def test_case_0(self, input_values=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(), '43900.6' + '\n' + '44627.5' + '\n' + '4978' + '\n')


if __name__ == '__main__':
    unittest.main()
