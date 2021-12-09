import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '3',
        '3 2 2 3 2 1 1 2 3 3 ',
        '3',
        '171',
        '3 2 3 1 1 1 1 3 1 2 ',
        '2',
        '16',
        '3 3 3 1 3 1 1 2 3 2 ',
        '2',
        '43',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '6\n' +
                         '3\n' +
                         '4\n')


if __name__ == '__main__':
    unittest.main()
