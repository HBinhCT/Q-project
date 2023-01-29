import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '6 5',
        '#itsmylife',
        '2 3',
        '1 25',
        '3 15',
        '4 10',
        '5 25',
        '6 5',
        '#itsnow',
        '1 4',
        '4 100',
        '1 25',
        '2 25',
        '3 25',
        '4 25',
        '#ornever',
        '2 2',
        '5 30',
        '3 10',
        '1 25',
        '4 15',
        '#iaintgonna',
        '1 3',
        '2 150',
        '1 50',
        '2 50',
        '3 50',
        '#liveforever',
        '2 2',
        '5 13',
        '6 25',
        '4 25',
        '1 13',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '1 2 75\n' +
                         '1 4 13\n' +
                         '3 4 12\n' +
                         '3 5 18\n' +
                         '3 6 20\n')


if __name__ == '__main__':
    unittest.main()
