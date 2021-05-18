import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '2',
        '2 6',
        '5 6 1 3 10 2',
        '2 2 8 7 2 3',
        '1 3 76',
        '5 3',
        '5 4 10',
        '2 3 6',
        '5 5 8',
        '3 9 1',
        '5 8 3',
        '5 2 25',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         'YES\n' +
                         '64\n' +
                         'NO\n')


if __name__ == '__main__':
    unittest.main()
