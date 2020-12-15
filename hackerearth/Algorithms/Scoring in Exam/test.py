import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '5 2',
        '2 3 9 4 5',
        '3 5 11 6 7',
        '5',
        '3',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '23\n' +
                         '18\n')


if __name__ == '__main__':
    unittest.main()
