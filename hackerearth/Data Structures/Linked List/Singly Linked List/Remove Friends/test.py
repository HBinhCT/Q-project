import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '3',
        '3 1',
        '3 100 1',
        '5 2',
        '19 12 3 4 17',
        '5 3',
        '23 45 11 77 18',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '100 1\n' +
                         '19 12 17\n' +
                         '77 18\n')


if __name__ == '__main__':
    unittest.main()
