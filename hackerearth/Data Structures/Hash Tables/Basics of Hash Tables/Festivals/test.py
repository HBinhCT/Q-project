import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('sys.stdin.readline', side_effect=[
        '2',
        '6',
        'B 20',
        'A 2',
        'A 10',
        'A 10',
        'B 30',
        'A 30',
        '3',
        'abc 10',
        'xyz 15',
        'oop 8',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         'A 50\n' +
                         'xyz 15\n')


if __name__ == '__main__':
    unittest.main()
