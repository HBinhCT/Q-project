import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '2',
        '4 3 ',
        '0 100',
        '0 20',
        '30 50',
        '40 80',
        '6 4',
        '10 55',
        '10 20',
        '40 60',
        '55 60',
        '60 70',
        '75 95',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '1719 Cab was full\n' +
                         '1070\n')


if __name__ == '__main__':
    unittest.main()
