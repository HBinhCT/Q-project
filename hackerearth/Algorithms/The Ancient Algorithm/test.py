import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('sys.stdin.readline', side_effect=[
        '2',
        '3',
        '1 1 1',
        '2 3 1000',
        'ARM',
        '4',
        '1 2 3 4',
        '0 1 1000',
        'AMAM',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '3 3 9 \n' +
                         '1 2 3 4 \n')


if __name__ == '__main__':
    unittest.main()
