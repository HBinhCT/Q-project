import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '4 4',
        '1 2 3 4',
        '5 6 7 8',
        '9 10 11 12',
        '13 14 15 16',
        '3 3 5',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         'YES\n' +
                         '3\n' +
                         '3 3\n' +
                         '2 3\n' +
                         '1 3\n')


if __name__ == '__main__':
    unittest.main()
