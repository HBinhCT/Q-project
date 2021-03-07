import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '4',
        'kalyan nobodyintheworld',
        'rahul allgirlsallhunontheplanet',
        'physicsguy nobodynobodylikesitbetter',
        'lal llaggyel',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         'We are only friends\n' +
                         'Love you too\n' +
                         'We are only friends\n' +
                         'Love you too\n')


if __name__ == '__main__':
    unittest.main()
