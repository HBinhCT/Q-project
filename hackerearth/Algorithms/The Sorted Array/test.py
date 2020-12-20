import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '2',
        '4',
        '7 3 9 10',
        '3',
        '11 1 9',
    ])
    def test_case_0(self, input_mock=None, inputs_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         'YES\n' +
                         '4 6 9 10\n' +
                         'NO\n')


if __name__ == '__main__':
    unittest.main()
