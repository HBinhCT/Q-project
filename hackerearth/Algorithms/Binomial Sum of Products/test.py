import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '3',
        '0 0 0 1',
        '4 5 1 2',
        '4 5 5 6',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '0\n' +
                         '74\n' +
                         '510\n')


if __name__ == '__main__':
    unittest.main()
