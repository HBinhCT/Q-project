import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', return_value='1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9')
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '[ 1.  2.  3.  4.  5.  6.  7.  8.  9.]\n'
                         + '[  2.   3.   4.   5.   6.   7.   8.   9.  10.]\n'
                         + '[  1.   2.   3.   4.   6.   7.   8.   9.  10.]\n')


if __name__ == '__main__':
    unittest.main()
