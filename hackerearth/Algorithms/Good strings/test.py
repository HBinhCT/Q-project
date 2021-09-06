import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '8',
        '(#(##)#)',
        '2 1',
        '4 2',
        '5 1',
        '7 3',
        '1 8 5',
        '3 6 3',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(), 'Yes\n')


if __name__ == '__main__':
    unittest.main()
