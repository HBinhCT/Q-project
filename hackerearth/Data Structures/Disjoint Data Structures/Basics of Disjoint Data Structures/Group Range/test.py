import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '5',
        '5 8 12 6 1',
        '3',
        '1 3',
        '2 4',
        '5 5',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '5 12\n' +
                         '6 8\n' +
                         '1 1\n')


if __name__ == '__main__':
    unittest.main()
