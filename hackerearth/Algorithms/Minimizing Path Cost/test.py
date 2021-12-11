import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('sys.stdin.readline', side_effect=[
        '4 4',
        'Howrah Trivandram Vashi Mysore',
        'Howrah Trivandram 10',
        'Howrah Vashi 20',
        'Trivandram Mysore 100',
        'Mysore Vashi 50',
        '6',
        'Howrah Trivandram',
        'Howrah Vashi',
        'Howrah Mysore',
        'Trivandram Vashi',
        'Trivandram Mysore',
        'Mysore Vashi',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '10\n' +
                         '20\n' +
                         '70\n' +
                         '30\n' +
                         '80\n' +
                         '50\n')


if __name__ == '__main__':
    unittest.main()
