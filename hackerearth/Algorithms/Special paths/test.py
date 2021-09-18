import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '4 5',
        '1 2',
        '2 3',
        '3 4',
        '4 1',
        '2 4',
        '8 5 6 1',
        '2 4',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(), '4\n')


if __name__ == '__main__':
    unittest.main()
