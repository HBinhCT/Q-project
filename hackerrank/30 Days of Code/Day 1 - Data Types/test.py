import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '12',
        '4.0',
        'is the best place to learn and practice coding!'
    ])
    def test_case_0(self, input_values=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '16' + '\n' +
                         '8.0' + '\n' +
                         'HackerRank is the best place to learn and practice coding!' + '\n')


if __name__ == '__main__':
    unittest.main()
