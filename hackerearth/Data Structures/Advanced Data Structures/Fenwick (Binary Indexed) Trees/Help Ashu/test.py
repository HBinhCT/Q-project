import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '6',
        '1 2 3 4 5 6',
        '4',
        '1 2 5',
        '2 1 4',
        '0 5 4',
        '1 1 6',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '2\n' +
                         '2\n' +
                         '4\n')


if __name__ == '__main__':
    unittest.main()
