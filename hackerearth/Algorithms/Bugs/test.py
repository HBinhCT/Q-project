import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '10',
        '1 1',
        '1 7',
        '2',
        '1 9',
        '1 21',
        '1 8',
        '1 5',
        '2',
        '1 9',
        '2',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         'Not enough enemies\n' +
                         '9\n' +
                         '9\n')


if __name__ == '__main__':
    unittest.main()
