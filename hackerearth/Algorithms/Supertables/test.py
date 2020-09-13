import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '4',
        '3 5 2',
        '3 5 3',
        '2 3 4',
        '2 3 6',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '5\n' +
                         '6\n' +
                         '6\n' +
                         '9\n')


if __name__ == '__main__':
    unittest.main()
