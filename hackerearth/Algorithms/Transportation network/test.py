import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '5 8',
        '1 1 2',
        '1 2 3',
        '2 1 3',
        '2 1 2',
        '1 3 4',
        '2 2 5',
        '1 4 5',
        '2 1 4',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         'NO\n' +
                         'NO\n' +
                         'NO\n' +
                         'YES\n' +
                         'NO\n' +
                         'YES\n' +
                         'NO\n' +
                         'YES\n')


if __name__ == '__main__':
    unittest.main()
