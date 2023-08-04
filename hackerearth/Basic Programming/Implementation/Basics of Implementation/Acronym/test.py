import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '5',
        'hey',
        'girls',
        'i',
        'am',
        'single',
        '11',
        'hey all boys and girls welcome to hackerearth easy september challenge',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(), 'A.B.A.W.T.H.E.S.C\n')


if __name__ == '__main__':
    unittest.main()
