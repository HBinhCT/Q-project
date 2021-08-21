import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '4 3 4',
        '7 9 11',
        '2 3 1',
        '1 1 3',
        '2 1 4',
        '1 2 1',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '2\n' +
                         '3.6666666667\n' +
                         '7.0000000000\n' +
                         '3.6666666667\n' +
                         '3.6666666667\n')


if __name__ == '__main__':
    unittest.main()
