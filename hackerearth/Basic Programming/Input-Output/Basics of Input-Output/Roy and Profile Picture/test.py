import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '180',
        '3',
        '640 480',
        '120 300',
        '180 180',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         'CROP IT\n' +
                         'UPLOAD ANOTHER\n' +
                         'ACCEPTED\n')


if __name__ == '__main__':
    unittest.main()
