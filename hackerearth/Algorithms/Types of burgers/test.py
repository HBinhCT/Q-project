import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '2',
        '2 2 2 ',
        '7',
        '4 6',
        '1 5',
        '3 8',
        '6 3 2',
        '32',
        '6 9 8 8 1 8',
        '5 7 3',
        '9 3',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '100\n' +
                         '597\n')


if __name__ == '__main__':
    unittest.main()
