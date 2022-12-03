import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('sys.stdin.readline', side_effect=[
        '2',
        '3',
        '5',
    ])
    def test_case_0(self, input_mock1=None, input_mock2=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '3 5\n' +
                         '20 30\n')


if __name__ == '__main__':
    unittest.main()
