import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '2',
        '3 3 7',
        '2 3 1',
        '6 1 9',
        '8 2 3',
        '3 4 9',
        '2 3 4 1',
        '6 5 5 3',
        '5 2 3 4',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '6\n' +
                         '-1\n')


if __name__ == '__main__':
    unittest.main()
