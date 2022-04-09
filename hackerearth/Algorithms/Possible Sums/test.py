import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '3',
        '3',
        '1 2 3',
        '5',
        '5 1 3 2 7',
        '4',
        '1 2 4 8',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '7\n' +
                         '19\n' +
                         '16\n')


if __name__ == '__main__':
    unittest.main()
