import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '1',
        '4',
        '2 6 4 4',
        '5 7 1 7',
        '8 9 8 6',
        '7 7 7 9',
        '2',
        '3 8',
        '5 10',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '6\n' +
                         '4\n')


if __name__ == '__main__':
    unittest.main()
