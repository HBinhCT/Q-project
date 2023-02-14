import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '2',
        '3',
        '2 0 1',
        '5',
        '4 0 2 1 3',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '2 1 1\n' +
                         '4 0 2 1 1\n')


if __name__ == '__main__':
    unittest.main()
