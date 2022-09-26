import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '5',
        '10010',
        '6',
        '0 2 4',
        '0 2 3',
        '1 1',
        '0 0 4',
        '1 1',
        '0 0 3',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '2\n' +
                         '1\n' +
                         '2\n' +
                         '1\n')


if __name__ == '__main__':
    unittest.main()
