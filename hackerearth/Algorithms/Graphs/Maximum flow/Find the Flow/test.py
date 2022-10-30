import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '10',
        'S A 8',
        'S B 10',
        'A B 4',
        'A C 8',
        'A D 5',
        'B D 2',
        'B C 5',
        'C T 4',
        'C D 3',
        'D T 12',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(), '14\n')


if __name__ == '__main__':
    unittest.main()
