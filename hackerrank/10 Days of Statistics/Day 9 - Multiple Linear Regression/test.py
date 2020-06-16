import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '2 7',
        '0.18 0.89 109.85',
        '1.0 0.26 155.72',
        '0.92 0.11 137.66',
        '0.07 0.37 76.17',
        '0.85 0.16 139.75',
        '0.99 0.41 162.6',
        '0.87 0.47 151.77',
        '4',
        '0.49 0.18',
        '0.57 0.83',
        '0.56 0.64',
        '0.76 0.18',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        res = list(map(lambda x: round(float(x), 1), text_trap.getvalue().split()))
        expect = list(map(lambda x: round(float(x), 1), ['105.22', '142.68', '132.94', '129.71']))
        self.assertEqual(res, expect)


if __name__ == '__main__':
    unittest.main()
