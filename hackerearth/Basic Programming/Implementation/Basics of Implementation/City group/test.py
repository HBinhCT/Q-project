import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '10 6',
        '0',
        '1 1',
        '2 2 4',
        '0',
        '2 3 5',
        '5 6 8 7 9 10',
        '4',
        '7 10',
        '1 2',
        '1 5',
        '6 2',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '0\n' +
                         '1\n' +
                         '3\n' +
                         '3\n')


if __name__ == '__main__':
    unittest.main()
