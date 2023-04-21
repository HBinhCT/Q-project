import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '6',
        'HackerEarth',
        'primeCheck',
        'OddOrEven',
        'random',
        'getRandom',
        'macOS',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         'hacker_earth\n' +
                         'prime_check\n' +
                         'odd_or_even\n' +
                         'random\n' +
                         'get_random\n' +
                         'mac_o_s\n')


if __name__ == '__main__':
    unittest.main()
