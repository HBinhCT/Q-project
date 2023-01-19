import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '4',
        '1000000000 https://www.google.com gg1 25',
        '1000000004 https://www.youtube.com yt 26',
        '1000000004 https://HackerEarth.com he 50 ',
        '1000000005 https://www.facebook.com F!B 25',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         'YES\n' +
                         'YES\n' +
                         'YES\n' +
                         'NO\n')


if __name__ == '__main__':
    unittest.main()
