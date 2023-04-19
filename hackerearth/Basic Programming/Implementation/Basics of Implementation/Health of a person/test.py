import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '2',
        '6 5',
        '2 1 6 4 3 7',
        '2 3 7 3 4',
        '3 3',
        '2 1 3',
        '2 2 2',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '1\n' +
                         '1\n' +
                         '3\n' +
                         '-1\n' +
                         '5\n' +
                         '3\n' +
                         '1\n' +
                         '1\n' +
                         '-1\n')


if __name__ == '__main__':
    unittest.main()
