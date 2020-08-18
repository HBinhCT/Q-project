import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '10 4',
        '7 1 4 3 1 6 4 2 5 1',
        '3 4',
        '1 2',
        '2 7',
        '6 7',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '0\n' +
                         '1\n' +
                         '1\n' +
                         '2\n')


if __name__ == '__main__':
    unittest.main()
