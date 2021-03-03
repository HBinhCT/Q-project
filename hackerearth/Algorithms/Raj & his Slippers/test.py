import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '1',
        '5',
        '21:30',
        '06:00',
        '09:00',
        '25',
        '10',
        '07:00 10:00',
        '08:30 09:20',
        '12:00 13:45',
        '06:00 16:00',
        '12:05 15:00',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(), 'Case 1: 3\n')


if __name__ == '__main__':
    unittest.main()
