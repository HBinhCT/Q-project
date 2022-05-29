import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '2',
        '5',
        '2 4 3 2 1',
        '6',
        '3 0 5 4 4 4',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '8\n' +
                         '16\n')


if __name__ == '__main__':
    unittest.main()
