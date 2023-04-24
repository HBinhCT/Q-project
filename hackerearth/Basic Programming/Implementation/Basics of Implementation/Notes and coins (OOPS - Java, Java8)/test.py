import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '7',
        'Note 83',
        'Coin 19',
        'Coin 85',
        'Note 8',
        'Note 30',
        'Coin 56',
        'Coin 53',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         'Coins :\n' +
                         '19\n' +
                         '85\n' +
                         '56\n' +
                         '53\n' +
                         'Notes :\n' +
                         '83\n' +
                         '8\n' +
                         '30\n')


if __name__ == '__main__':
    unittest.main()
