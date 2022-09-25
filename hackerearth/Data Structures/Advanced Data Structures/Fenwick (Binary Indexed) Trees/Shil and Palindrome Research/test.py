import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '5 4',
        'ababb',
        '2 2 3',
        '1 3 b',
        '2 1 4',
        '2 1 5',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         'no\n' +
                         'no\n' +
                         'yes\n')


if __name__ == '__main__':
    unittest.main()
