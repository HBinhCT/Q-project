import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '3',
        '120',
        '121',
        '231',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         'The streak lives still in our heart!\n' +
                         'The streak is broken!\n' +
                         'The streak is broken!\n')


if __name__ == '__main__':
    unittest.main()
