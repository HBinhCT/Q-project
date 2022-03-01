import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '2',
        '3 ',
        '3',
        '1 2 3     ',
        '2 4 8',
        '4 ',
        '8',
        '2 4 5 7',
        '4 9 7 5',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '8\n' +
                         '13\n')


if __name__ == '__main__':
    unittest.main()
