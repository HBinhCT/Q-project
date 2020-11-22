import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '4',
        '4',
        '300 400 600 700',
        '2',
        '1321 2450',
        '3',
        '500 123 873',
        '4',
        '600 800 150 700',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '2200\n' +
                         '2450\n' +
                         '1496\n' +
                         '2400\n')


if __name__ == '__main__':
    unittest.main()
