import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('sys.stdin.readline', side_effect=[
        '5',
        'banana 10',
        'biscuit 5',
        'apple 10',
        'mango 1',
        'juice 14',
        '5',
        '+ banana',
        '+ apple',
        '? 1',
        '+ mango',
        '? 0',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '2\n' +
                         '3\n')


if __name__ == '__main__':
    unittest.main()
