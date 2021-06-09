import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '6',
        '5 2',
        '1 2',
        '2 3',
        '2 4',
        '1 5',
        '5 6',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '9\n' +
                         '5\n' +
                         '5\n' +
                         '8\n' +
                         '5\n')


if __name__ == '__main__':
    unittest.main()
