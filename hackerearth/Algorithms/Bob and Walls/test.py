import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '4',
        '5',
        '1 3 2 5 4',
        '5',
        '1 2 3 4 5',
        '5',
        '5 4 3 2 1',
        '5',
        '1 4 3 2 5',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '3\n' +
                         '5\n' +
                         '1\n' +
                         '3\n')


if __name__ == '__main__':
    unittest.main()
