import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '2',
        '2 50',
        '80 40',
        '60 20',
        '5 100',
        '100 40',
        '50 40',
        '40 50',
        '60 20',
        '100 50',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '20 90\n' +
                         '90 210\n')


if __name__ == '__main__':
    unittest.main()
