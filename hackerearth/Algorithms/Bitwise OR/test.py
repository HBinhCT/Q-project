import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '3',
        '5 7',
        '1 2 3 4 5',
        '4 15',
        '1 2 4 8',
        '4 16',
        '1 2 4 8',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '1\n' +
                         '3 4\n' +
                         '1\n' +
                         '1 4\n' +
                         '0\n')


if __name__ == '__main__':
    unittest.main()
