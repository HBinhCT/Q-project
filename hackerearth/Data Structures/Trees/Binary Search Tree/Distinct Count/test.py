import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '4',
        '4 1',
        '1 4 2 5',
        '4 2',
        '4 2 1 5',
        '4 3',
        '5 2 4 1',
        '4 4',
        '1 2 4 5',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         'Average\n' +
                         'Average\n' +
                         'Average\n' +
                         'Good\n')


if __name__ == '__main__':
    unittest.main()
