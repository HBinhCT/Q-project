import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '2',
        '5',
        '2 5 2 4 3',
        '5',
        '5 4 2 3 1',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '5 4 3 2 2\n' +
                         '5 4 3 2 1\n')


if __name__ == '__main__':
    unittest.main()
