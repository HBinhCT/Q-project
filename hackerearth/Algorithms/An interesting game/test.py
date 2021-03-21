import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '2',
        '4',
        '4 2 8 6',
        '6 5 7 8',
        '6',
        '7 8 2 6 10 3',
        '9 1 3 10 2 4',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '-4\n' +
                         '8\n')


if __name__ == '__main__':
    unittest.main()
