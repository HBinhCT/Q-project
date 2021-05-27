import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '2',
        '2',
        '2 1',
        '3',
        '2 1',
        '2 3',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         'UNSAFE\n' +
                         'SAFE\n')


if __name__ == '__main__':
    unittest.main()
