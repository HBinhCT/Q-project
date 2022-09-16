import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '6 3',
        '1 2 3 4 5 6',
        '1 4 5 2',
        '2 4 3',
        '1 4 5 2',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '21\n' +
                         '19\n')


if __name__ == '__main__':
    unittest.main()
