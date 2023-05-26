import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '4',
        '1 2 3 3 ',
        '3 3 1 7',
        '3 4 8 9',
        '13 5 13 5',
        '5 7 12 9',
        '1 5 9 15',
        '7 9 10 12',
        '10 14 17 21',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         'YES\n' +
                         'INVALID\n' +
                         'NO\n' +
                         'NO\n')


if __name__ == '__main__':
    unittest.main()
