import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '5',
        '2',
        '11',
        '11',
        '4',
        '0101',
        '0110',
        '0110',
        '0101',
        '4',
        '1001',
        '0000',
        '0000',
        '1001',
        '5',
        '01110',
        '01010',
        '10001',
        '01010',
        '01110',
        '5',
        '00100',
        '01010',
        '10001',
        '01010',
        '01110',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         'YES\n' +
                         'NO\n' +
                         'YES\n' +
                         'YES\n' +
                         'NO\n')


if __name__ == '__main__':
    unittest.main()
