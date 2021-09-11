import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '1',
        '7',
        '1 2 3 4 5 6 7',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            pass
        self.assertEqual(text_trap.getvalue(), '1 2 3 7 6 5 4\n')


if __name__ == '__main__':
    unittest.main()
