import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '2',
        '3',
        '11',
        '00',
        '00000',
        '5',
        '01',
        '1111',
        '0001',
        '11',
        '01',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '1\n' +
                         '10\n')


if __name__ == '__main__':
    unittest.main()
