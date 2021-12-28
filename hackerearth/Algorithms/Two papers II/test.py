import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '5 4',
        '3 5 1',
        '4 5 1',
        '1 2 0',
        '5 1 1',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(), 'YES\n')


if __name__ == '__main__':
    unittest.main()
