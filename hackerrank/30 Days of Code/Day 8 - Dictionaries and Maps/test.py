import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '3',
        'sam 99912222',
        'tom 11122222',
        'harry 12299933',
        'sam',
        'edward',
        'harry',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         'sam=99912222' + '\n' +
                         'Not found' + '\n' +
                         'harry=12299933' + '\n')


if __name__ == '__main__':
    unittest.main()
