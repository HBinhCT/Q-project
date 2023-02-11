import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '3',
        '1 2 3 4',
        '4 4 4 4',
        '1 1000000000 1 1000000000',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '14\n' +
                         '0\n' +
                         '2011349\n')


if __name__ == '__main__':
    unittest.main()
