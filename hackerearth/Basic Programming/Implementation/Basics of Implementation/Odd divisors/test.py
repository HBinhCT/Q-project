import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '5',
        '1 100',
        '110 30',
        '12345 100000007',
        '10 28383',
        '100 5',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '1\n' +
                         '18\n' +
                         '50804693\n' +
                         '36\n' +
                         '4\n')


if __name__ == '__main__':
    unittest.main()
