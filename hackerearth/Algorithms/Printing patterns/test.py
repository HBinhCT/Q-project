import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', return_value='10 10 5 5')
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '5 5 5 5 5 5 5 5 5 5\n' +
                         '5 4 4 4 4 4 4 4 4 4\n' +
                         '5 4 3 3 3 3 3 3 3 4\n' +
                         '5 4 3 2 2 2 2 2 3 4\n' +
                         '5 4 3 2 1 1 1 2 3 4\n' +
                         '5 4 3 2 1 0 1 2 3 4\n' +
                         '5 4 3 2 1 1 1 2 3 4\n' +
                         '5 4 3 2 2 2 2 2 3 4\n' +
                         '5 4 3 3 3 3 3 3 3 4\n' +
                         '5 4 4 4 4 4 4 4 4 4\n')


if __name__ == '__main__':
    unittest.main()
