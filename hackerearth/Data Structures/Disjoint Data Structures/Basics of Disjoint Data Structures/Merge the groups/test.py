import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '4',
        '5 3 2 9',
        '4',
        '2 4',
        '1 1 4',
        '2 4',
        '2 3',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '0\n' +
                         '4\n' +
                         '0\n')


if __name__ == '__main__':
    unittest.main()
