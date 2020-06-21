import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '10',
        '2 3 4 5 6 8 7 6 5 18',
        '6',
        '6 55',
        '6 45',
        '6 55',
        '4 40',
        '18 60',
        '10 50',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(), '200\n')


if __name__ == '__main__':
    unittest.main()
