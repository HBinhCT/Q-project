import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '1',
        '5 2',
        '5 12 7 2 10',
        '1 2',
        '1 3',
        '2 4',
        '1 5',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(), 'Case 1: 9\n')


if __name__ == '__main__':
    unittest.main()
