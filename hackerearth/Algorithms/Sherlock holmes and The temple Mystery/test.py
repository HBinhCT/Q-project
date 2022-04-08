import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '3',
        '5',
        '4 3 5 5 3',
        '4',
        '1 2 3 4',
        '2',
        '1 2',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         'YES\n' +
                         'YES\n' +
                         'NO\n')


if __name__ == '__main__':
    unittest.main()
