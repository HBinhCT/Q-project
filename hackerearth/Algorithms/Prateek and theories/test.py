import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '1',
        '5',
        '1 10',
        '2 4',
        '3 5',
        '11 12',
        '12 13'
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(), '3\n')


if __name__ == '__main__':
    unittest.main()
