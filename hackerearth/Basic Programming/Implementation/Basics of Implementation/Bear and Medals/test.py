import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '2',
        '4',
        '0 0 2',
        '1 2 1',
        '2 0 0',
        '0 2 0',
        '1',
        '0 1000 0',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '4\n' +
                         '1000\n')


if __name__ == '__main__':
    unittest.main()
