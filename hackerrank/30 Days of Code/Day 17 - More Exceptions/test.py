import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '4',
        '3 5',
        '2 4',
        '-1 -2',
        '-1 3',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '243' + '\n' +
                         '16' + '\n' +
                         'n and p should be non-negative' + '\n' +
                         'n and p should be non-negative' + '\n')


if __name__ == '__main__':
    unittest.main()
