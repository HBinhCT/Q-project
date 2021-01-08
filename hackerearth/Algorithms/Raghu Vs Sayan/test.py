import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '3',
        '15 20 3',
        '10 5 4',
        '3 10 2',
        '4 7',
        '10 8 3',
        '4 5 5',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         'Sayan Won\n' +
                         'Sayan Won\n' +
                         'Raghu Won\n')


if __name__ == '__main__':
    unittest.main()
