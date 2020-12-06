import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '5 5',
        '13 345 193 44444 100303',
        '1 2',
        '1 4',
        '2 1',
        '2 4',
        '1 5',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '11\n' +
                         '18\n' +
                         '2\n' +
                         '13\n' +
                         '20\n')


if __name__ == '__main__':
    unittest.main()
