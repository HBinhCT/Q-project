import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '3 3',
        '2 3 7',
        '5 4 2',
        '3 7 11',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '4\n' +
                         '1 1\n' +
                         '2 1\n' +
                         '3 2\n' +
                         '3 3\n')


if __name__ == '__main__':
    unittest.main()
