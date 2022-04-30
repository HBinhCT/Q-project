import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '3',
        '0 3 1',
        '1 5 3',
        '2',
        '2 1',
        '3 3',
        '3 1',
        '1 3',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         'YES\n' +
                         'NO\n')


if __name__ == '__main__':
    unittest.main()
