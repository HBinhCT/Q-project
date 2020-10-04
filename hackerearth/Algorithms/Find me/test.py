import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '10 5',
        '79 72 46 40 6 79 17 28 84 27',
        '2',
        '9',
        '2',
        '5',
        '1',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '17\n' +
                         '84\n' +
                         '27\n' +
                         '72\n' +
                         '6\n')


if __name__ == '__main__':
    unittest.main()
