import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '1',
        '1000 2000 3000 4000',
        '1 2 30 40',
        '110 10 7 8',
        '15 30 45 20',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(), 'Flash\n')


if __name__ == '__main__':
    unittest.main()
