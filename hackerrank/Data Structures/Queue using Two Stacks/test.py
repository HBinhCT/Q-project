import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '10',
        '1 42',
        '2',
        '1 14',
        '3',
        '1 28',
        '3',
        '1 60',
        '1 78',
        '2',
        '2',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '14\n' +
                         '14\n')


if __name__ == '__main__':
    unittest.main()
