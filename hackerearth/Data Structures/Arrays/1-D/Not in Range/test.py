import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '5',
        '2 20',
        '23 200',
        '21 21',
        '101 2000',
        '2002 999998',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(), '2002023\n')


if __name__ == '__main__':
    unittest.main()
