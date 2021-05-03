import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '9 10',
        '1 2',
        '2 3',
        '1 7',
        '2 4',
        '3 4',
        '4 7',
        '7 8',
        '9 7',
        '7 6',
        '5 6',
        '3',
        '4 2',
        '5 3',
        '2 1',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '4\n' +
                         '4\n' +
                         '3\n')


if __name__ == '__main__':
    unittest.main()
