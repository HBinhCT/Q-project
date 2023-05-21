import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('sys.stdin.readline', side_effect=[
        '9',
        'Tom 6',
        'Jim 7',
        'Tom 19',
        'Phil 8',
        'Rick 12',
        'Jim 22',
        'Rick 18',
        'Phil 22',
        'Tom 36',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '1 Tom\n' +
                         '2 Jim\n' +
                         '3 Phil\n' +
                         '4 Rick\n')


if __name__ == '__main__':
    unittest.main()
