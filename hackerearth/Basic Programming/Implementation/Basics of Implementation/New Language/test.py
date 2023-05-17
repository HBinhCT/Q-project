import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '9',
        '1+1',
        '10+5',
        '10*10',
        '9*2',
        '9*9',
        '9*10',
        '90-1',
        '90/2',
        '79/2',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '2\n' +
                         '15\n' +
                         '100\n' +
                         '17\n' +
                         '71\n' +
                         '90\n' +
                         '79\n' +
                         '40\n' +
                         '39\n')


if __name__ == '__main__':
    unittest.main()
