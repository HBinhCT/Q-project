import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '2',
        '4',
        '3 150',
        '2 2 2',
        '2 3',
        '50 50',
        '3 4',
        '50 50',
        '4 4',
        '20 10',
        '2',
        '1 50',
        '2',
        '2 2',
        '50 50',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '4\n' +
                         '1\n')


if __name__ == '__main__':
    unittest.main()
