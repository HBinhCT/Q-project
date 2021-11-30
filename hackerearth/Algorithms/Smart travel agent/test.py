import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '7 10',
        '1 2 30',
        '1 3 15',
        '1 4 10',
        '2 4 25',
        '2 5 60',
        '3 4 40',
        '3 6 20',
        '4 7 35',
        '5 7 20',
        '6 7 30',
        '1 7 99',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '1 2 4 7\n' +
                         '5\n')


if __name__ == '__main__':
    unittest.main()
