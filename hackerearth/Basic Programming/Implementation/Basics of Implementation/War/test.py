import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '3',
        '2',
        '1 5',
        '5 1',
        '4',
        '5 6 3 1',
        '10 3 5 6',
        '3',
        '15 20 50',
        '8 3 7',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         'Tie\n' +
                         'Alice\n' +
                         'Bob\n')


if __name__ == '__main__':
    unittest.main()
