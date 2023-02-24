import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '3',
        '3 4',
        '2 0',
        '2 1',
        '4 0',
        '2 3',
        '1 0',
        '2 1',
        '2 1',
        '2 0',
        '3 2',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '3\n' +
                         '2\n' +
                         '0\n')


if __name__ == '__main__':
    unittest.main()
