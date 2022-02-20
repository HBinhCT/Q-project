import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '4',
        '2',
        '1 2',
        '3',
        '3 2 1',
        '5',
        '10 5 6 7 8',
        '4',
        '2 2 2 2',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '0\n' +
                         '2\n' +
                         '1\n' +
                         '3\n')


if __name__ == '__main__':
    unittest.main()
