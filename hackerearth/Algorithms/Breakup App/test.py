import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '4',
        'G: I want to go on 19',
        'M: No that is not possible lets go on 21',
        'G: No 19 is final and 21 is not',
        'M: OKAY as you wish',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(), 'Date\n')


if __name__ == '__main__':
    unittest.main()
