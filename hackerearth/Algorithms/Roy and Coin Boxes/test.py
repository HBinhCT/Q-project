import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '7',
        '4',
        '1 3',
        '2 5',
        '1 2',
        '5 6',
        '4',
        '1',
        '7',
        '4',
        '2',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '6\n' +
                         '0\n' +
                         '0\n' +
                         '4\n')


if __name__ == '__main__':
    unittest.main()
