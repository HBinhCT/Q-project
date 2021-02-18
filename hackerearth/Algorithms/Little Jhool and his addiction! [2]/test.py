import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '3',
        '2 1',
        '4 2',
        '6 4',
        '1 6 6 7 1 8',
        '4 0',
        '2 6 4 3',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '0\n' +
                         'Chick magnet Jhool!\n' +
                         '4\n' +
                         'Lucky chap!\n' +
                         '1\n' +
                         'No more girlfriends!\n')


if __name__ == '__main__':
    unittest.main()
