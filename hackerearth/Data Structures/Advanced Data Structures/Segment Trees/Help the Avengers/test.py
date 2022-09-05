import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '1',
        '10',
        '1 3 18 960 22 17 15 31 99 231',
        '5',
        'A 1 10',
        'C 3 17',
        'C 5 23',
        'A 1 10',
        'A 1 5',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '3\n' +
                         '5\n' +
                         '3\n')


if __name__ == '__main__':
    unittest.main()
