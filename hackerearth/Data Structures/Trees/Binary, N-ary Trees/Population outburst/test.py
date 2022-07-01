import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '9 2',
        '1 2',
        '2 1',
        '5 2',
        '4 1',
        '10 0',
        '15 0',
        '21 0',
        '23 1',
        '42 100',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '0 1 1\n' +
                         '0 1 2\n' +
                         '1 2 1\n' +
                         '1 2 2\n' +
                         '2 2 1\n' +
                         '5 3 1\n' +
                         '5 3 2\n' +
                         '4 3 1\n' +
                         '23 4 1\n')


if __name__ == '__main__':
    unittest.main()
