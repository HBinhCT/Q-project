import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '5 5',
        '1 100 2 3 5',
        'get 1 4 4',
        'update 2 3',
        'get 1 4 4',
        'get 1 4 100',
        'get 1 5 3',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '0\n' +
                         '3\n' +
                         '-1\n' +
                         '2\n')


if __name__ == '__main__':
    unittest.main()
