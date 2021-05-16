import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '2',
        '4 6',
        '0 0 0 1 1 0 ',
        '1 1 0 0 0 0 ',
        '0 1 0 0 0 0 ',
        '0 0 1 0 0 0 ',
        '6 4',
        '1 1 1 1 ',
        '0 0 0 0 ',
        '0 1 0 0 ',
        '1 0 1 0 ',
        '1 0 0 0 ',
        '1 0 0 0',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '2 4\n' +
                         '2 5\n')


if __name__ == '__main__':
    unittest.main()
