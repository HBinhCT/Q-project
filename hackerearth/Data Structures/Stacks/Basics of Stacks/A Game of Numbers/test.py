import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '8',
        '3',
        '7',
        '1',
        '7',
        '8',
        '4',
        '5',
        '2',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(), '1 4 4 4 -1 2 -1 -1\n')


if __name__ == '__main__':
    unittest.main()
