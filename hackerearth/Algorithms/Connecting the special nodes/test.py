import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '12 7 2',
        '1 2',
        '1 3',
        '4 5',
        '4 6',
        '5 7',
        '9 10',
        '11 12',
        '1 4',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(), '32 28\n')


if __name__ == '__main__':
    unittest.main()
