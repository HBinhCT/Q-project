import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '4 4',
        '2 8 9 7',
        '5 8 1 7',
        '5 7 3 5',
        '4 8 7 4',
        '4',
        '1 2 4 2',
        '1 4 2 4',
        '1 1 4 2',
        '2 4 2 4',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '31\n' +
                         '14\n' +
                         '47\n' +
                         '7\n')


if __name__ == '__main__':
    unittest.main()
