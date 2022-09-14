import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        'agcdgcaag',
        '5',
        '2 a',
        '1 c',
        '1 d',
        '3 g',
        '2 a',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(), 'aggc\n')


if __name__ == '__main__':
    unittest.main()
