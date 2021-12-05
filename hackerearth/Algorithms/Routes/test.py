import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '1000',
        '4',
        '5',
        '1 2 1 2500',
        '1 3 1 3000',
        '1 4 2 7000',
        '2 4 1 3000',
        '3 4 1 2000',
        '1',
        '4',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '1->3->4 3 8000\n')


if __name__ == '__main__':
    unittest.main()
